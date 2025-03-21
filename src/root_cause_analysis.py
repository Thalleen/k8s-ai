import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY is not set. Please check your .env file.")

# Configure Gemini AI
genai.configure(api_key=API_KEY)

# Use the correct model
model = genai.GenerativeModel('models/gemini-1.5-flash')  # Use 'models/gemini-1.5-pro' for higher accuracy

# Load dataset
data_path = "/Users/thalleencn/Desktop/k8s-ai/data/k8s_with_anamolies.csv"
try:
    data = pd.read_csv(data_path)
except FileNotFoundError:
    raise FileNotFoundError(f"Dataset not found at: {data_path}")

# Filter anomalies
anomalies = data[data['anomaly'] == -1]

# Process anomalies
for index, row in anomalies.iterrows():
    prompt = f"""
    The following Kubernetes metrics show an anomaly:
    - **Pod Name**: {row['pod_name']}
    - **Namespace**: {row['namespace']}
    - **CPU Allocation Efficiency**: {row['cpu_allocation_efficiency']}
    - **Memory Allocation Efficiency**: {row['memory_allocation_efficiency']}
    - **Disk I/O**: {row['disk_io']}
    - **Network Latency**: {row['network_latency']}
    - **Node Temperature**: {row['node_temperature']}
    - **Node CPU Usage**: {row['node_cpu_usage']}
    - **Node Memory Usage**: {row['node_memory_usage']}
    - **Event Type**: {row['event_type']}
    - **Event Message**: {row['event_message']}
    - **Scaling Event**: {row['scaling_event']}
    - **Pod Lifetime**: {row['pod_lifetime_seconds']} seconds

    Please analyze and suggest the root cause.
    """

    try:
        response = model.generate_content(prompt)
        print(f"\n🔍 **Anomaly Detected in Pod:** {row['pod_name']}")
        print("📌 **Root Cause Analysis:**")
        print(response.text)
        print("-" * 60)
    except Exception as e:
        print(f"❌ Error analyzing anomaly for pod {row['pod_name']}: {e}")
