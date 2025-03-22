import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#path relative to the project root
SRC_DIR = Path(__file__).resolve().parent.parent

# Load dataset with anomalies
data = pd.read_csv(SRC_DIR/'data/k8s_with_anamolies.csv')

# Plot CPU usage with predicted failures
plt.figure(figsize=(10, 6))
plt.plot(data['timestamp'], data['node_cpu_usage'], label='Node CPU Usage')
plt.scatter(data[data['predicted_failure'].notnull()].timestamp, data[data['predicted_failure'].notnull()].node_cpu_usage, color='red', label='Predicted Failures')
plt.legend()
plt.xlabel('Time')
plt.ylabel('CPU Usage')
plt.title('Node CPU Usage with Predicted Failures')
plt.show()