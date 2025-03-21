import pandas as pd
import matplotlib.pyplot as plt

# Load dataset with anomalies
data = pd.read_csv('/Users/thalleencn/Desktop/k8s-ai/venv/data/k8s_with_anamolies.csv')

# Plot CPU usage with anomalies
plt.figure(figsize=(10, 6))
plt.plot(data['timestamp'], data['node_cpu_usage'], label='Node CPU Usage')
plt.scatter(data[data['anomaly'] == -1].timestamp, data[data['anomaly'] == -1].node_cpu_usage, color='red', label='Anomalies')
plt.legend()
plt.xlabel('Time')
plt.ylabel('CPU Usage')
plt.title('Node CPU Usage with Anomalies and Root Cause Analysis')
plt.show()