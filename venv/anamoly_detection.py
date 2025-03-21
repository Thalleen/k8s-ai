import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Load cleaned dataset
data = pd.read_csv('/Users/thalleencn/Desktop/k8s-ai/venv/data/k8s_cleaned.csv')

# Select relevant features for anomaly detection
features = [
    'cpu_allocation_efficiency', 'memory_allocation_efficiency', 
    'disk_io', 'network_latency', 'node_temperature', 
    'node_cpu_usage', 'node_memory_usage'
]

# Train Isolation Forest model
model = IsolationForest(contamination=0.1)  # 10% anomalies
data['anomaly'] = model.fit_predict(data[features])

# Save the results
data.to_csv('/Users/thalleencn/Desktop/k8s-ai/venv/data/k8s_with_anamolies.csv', index=False)

# Visualize anomalies in CPU usage
plt.figure(figsize=(10, 6))
plt.plot(data['timestamp'], data['node_cpu_usage'], label='Node CPU Usage')
plt.scatter(data[data['anomaly'] == -1].timestamp, data[data['anomaly'] == -1].node_cpu_usage, color='red', label='Anomalies')
plt.legend()
plt.xlabel('Time')
plt.ylabel('CPU Usage')
plt.title('Node CPU Usage with Anomalies Detected')
plt.show()