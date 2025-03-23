import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY is not set. Please check your .env file.")

# Configure Gemini AI
genai.configure(api_key=API_KEY)

# Define dataset and model paths relative to the script's location
BASE_DIR = Path(__file__).resolve().parent.parent  # Adjust if running from a different directory
DATA_PATH = BASE_DIR / "data" / "k8s_with_anomalies.csv"  # Fixed typo in filename
OUTPUT_PATH = BASE_DIR / "data" / "root_cause_analysis.csv"

# Load the dataset with predicted failures
try:
    data = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    logging.error(f"Dataset not found at {DATA_PATH}. Please check the file path.")
    exit(1)

# Validate required columns
required_columns = [
    'pod_name', 'namespace', 'cpu_allocation_efficiency', 'memory_allocation_efficiency',
    'disk_io', 'network_latency', 'node_temperature', 'node_cpu_usage', 'node_memory_usage',
   'event_message', 'scaling_event', 'pod_lifetime_seconds', 'predicted_failure_label'
]
missing_columns = [col for col in required_columns if col not in data.columns]
if missing_columns:
    logging.error(f"Missing required columns in dataset: {missing_columns}")
    exit(1)

# Filter rows with predicted failures
failures = data[data['predicted_failure_label'].notnull()]

# Initialize the output CSV file
if not os.path.exists(OUTPUT_PATH):
    # Create the CSV file with headers if it doesn't exist
    pd.DataFrame(columns=['pod_name', 'namespace', 'predicted_failure_label', 'root_cause_analysis']).to_csv(OUTPUT_PATH, index=False)

# Analyze each failure
for index, row in failures.iterrows():
    # Skip API call if the predicted failure is 'normal'
    if row['predicted_failure_label'] == 'normal':
        logging.info(f"Skipping pod {row['pod_name']} (Predicted Failure: Normal)")
        continue  # Skip to the next iteration

    prompt = f"""
    The following Kubernetes metrics show a predicted failure:
    - Pod: {row['pod_name']}
    - Namespace: {row['namespace']}
    - CPU Allocation Efficiency: {row['cpu_allocation_efficiency']}
    - Memory Allocation Efficiency: {row['memory_allocation_efficiency']}
    - Disk I/O: {row['disk_io']}
    - Network Latency: {row['network_latency']}
    - Node Temperature: {row['node_temperature']}
    - Node CPU Usage: {row['node_cpu_usage']}
    - Node Memory Usage: {row['node_memory_usage']}
    - Event Message: {row['event_message']}
    - Scaling Event: {row['scaling_event']}
    - Pod Lifetime: {row['pod_lifetime_seconds']} seconds
    - Predicted Failure: {row['predicted_failure_label']}

    Analyze the root cause of the predicted failure and provide actionable recommendations.
    """

    try:
        # Use Gemini Flash to generate a response
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        response = model.generate_content(prompt)

        # Log the root cause analysis
        logging.info(f"Pod: {row['pod_name']}")
        logging.info("Root Cause Analysis:")
        logging.info(response.text)
        logging.info("-" * 50)

        # Append the result to the CSV file
        result = {
            'pod_name': row['pod_name'],
            'namespace': row['namespace'],
            'predicted_failure_label': row['predicted_failure_label'],
            'root_cause_analysis': response.text
        }
        pd.DataFrame([result]).to_csv(OUTPUT_PATH, mode='a', header=False, index=False)

    except Exception as e:
        logging.error(f"Error analyzing pod {row['pod_name']}: {e}")

logging.info(f"Root cause analysis saved to {OUTPUT_PATH}")