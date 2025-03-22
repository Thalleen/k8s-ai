import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY is not set. Please check your .env file.")

# Configure Gemini AI
genai.configure(api_key=API_KEY)

# Define dataset and model paths relative to the script's location
BASE_DIR = Path(__file__).resolve().parent.parent  # Adjust if running from a different directory
DATA_PATH = BASE_DIR / "data" / "k8s_with_anamolies.csv"

# Load the dataset with predicted failures
data = pd.read_csv(DATA_PATH)

# Filter rows with predicted failures
failures = data[data['predicted_failure'].notnull()]

# Analyze each failure
for index, row in failures.iterrows():
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
    - Event Type: {row['event_type']}
    - Event Message: {row['event_message']}
    - Scaling Event: {row['scaling_event']}
    - Pod Lifetime: {row['pod_lifetime_seconds']} seconds
    - Predicted Failure: {row['predicted_failure']}
    Please analyze and suggest the root cause.
    """

    # Use Gemini Flash to generate a response
    model = genai.GenerativeModel('models/gemini-1.5-flash') 
    response = model.generate_content(prompt)

    # Print the root cause analysis
    print(f"Pod: {row['pod_name']}")
    print("Root Cause Analysis:")
    print(response.text)
    print("-" * 50)