import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from pathlib import Path

# Define dataset and model paths relative to the script's location
BASE_DIR = Path(__file__).resolve().parent.parent  # Adjust if running from a different directory
DATA_PATH = BASE_DIR / "data" / "k8s_cleaned_labeled.csv"
MODEL_PATH = BASE_DIR / "model" / "failure_prediction_model.pkl"
SAVE_DATA_PATH = BASE_DIR / "data" / "k8s_with_anamolies.csv"

# Feature Engineering (same as during training)
def preprocess_data(data):
    # Compute derived features
    data['cpu_memory_ratio'] = np.where(data['node_memory_usage'] == 0, 0, data['node_cpu_usage'] / data['node_memory_usage'])
    data['disk_network_ratio'] = np.where(data['network_latency'] == 0, 0, data['disk_io'] / data['network_latency'])

    # Rolling Averages
    window_size = 5
    data['cpu_usage_rolling_avg'] = np.convolve(data['node_cpu_usage'], np.ones(window_size)/window_size, mode='same')
    data['memory_usage_rolling_avg'] = np.convolve(data['node_memory_usage'], np.ones(window_size)/window_size, mode='same')

    return data

# Select relevant features for anomaly detection (same as during training)
features = [
    'cpu_allocation_efficiency', 'memory_allocation_efficiency', 
    'disk_io', 'network_latency', 'node_cpu_usage', 
    'node_memory_usage', 'cpu_usage_avg', 'memory_usage_avg',
    'cpu_memory_ratio', 'disk_network_ratio', 
    'cpu_usage_rolling_avg', 'memory_usage_rolling_avg'
]

# Load the cleaned and labeled dataset
data = pd.read_csv(DATA_PATH)

# Preprocess the data (compute derived features)
data = preprocess_data(data)

# Load the trained failure prediction model
model = joblib.load(MODEL_PATH)

# Predict failures
data['predicted_failure'] = model.predict(data[features])

# Save the results
data.to_csv(SAVE_DATA_PATH, index=False)

# Visualize anomalies in CPU usage
plt.figure(figsize=(10, 6))
plt.plot(data['timestamp'], data['node_cpu_usage'], label='Node CPU Usage')
plt.scatter(data[data['predicted_failure'] == -1].timestamp, data[data['predicted_failure'] == -1].node_cpu_usage, color='red', label='Anomalies')
plt.legend()
plt.xlabel('Time')
plt.ylabel('CPU Usage')
plt.title('Node CPU Usage with Anomalies Detected')
plt.show()