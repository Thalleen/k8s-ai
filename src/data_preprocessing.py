import pandas as pd
from pathlib import Path


#Define dataset and model paths relative to the script's location
BASE_DIR = Path(__file__).resolve().parent.parent  # Adjust if running from a different directory
DATA_PATH = BASE_DIR / "data" / "kubernetes_performance_metrics_dataset.csv"
SAVE_DATA_PATH = BASE_DIR / "data" / "k8s_cleaned_labeled.csv"

# Load the dataset
data = pd.read_csv(DATA_PATH)

# Fill missing values in numeric columns with the mean
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

# Convert 'timestamp' to DateTime
data['timestamp'] = pd.to_datetime(data['timestamp'], format='%d/%m/%Y %H:%M')

# Feature Engineering: Create rolling averages for CPU and memory usage
data['cpu_usage_avg'] = data['node_cpu_usage'].rolling(window=5).mean()
data['memory_usage_avg'] = data['node_memory_usage'].rolling(window=5).mean()

# Label the data for failure prediction
data['failure_type'] = None
data.loc[(data['cpu_allocation_efficiency'] < 0.1), 'failure_type'] = 'cpu_exhaustion'
data.loc[(data['memory_allocation_efficiency'] < 0.1), 'failure_type'] = 'memory_exhaustion'
data.loc[(data['disk_io'] > 1000), 'failure_type'] = 'disk_exhaustion'
data.loc[(data['network_latency'] > 50), 'failure_type'] = 'network_issue'
data.loc[(data['event_type'] == 'Error'), 'failure_type'] = 'pod_crash'

# Save the cleaned and labeled dataset
data.to_csv(SAVE_DATA_PATH, index=False)
print("Cleaned and labeled dataset saved as 'k8s_cleaned_labeled.csv'")