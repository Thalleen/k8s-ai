import pandas as pd
import numpy as np
from pathlib import Path

# Define paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "kubernetes_performance_metrics_dataset.csv"
SAVE_DATA_PATH = BASE_DIR / "data" / "k8s_cleaned_labeled.csv"

# Load data with error handling
if not DATA_PATH.exists():
    raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")
data = pd.read_csv(DATA_PATH)

# Handle missing values (forward-fill for time-series)
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_cols] = data[numeric_cols].fillna(method='ffill')

# Parse timestamps
data['timestamp'] = pd.to_datetime(data['timestamp'], infer_datetime_format=True)

# Feature engineering (avoid leakage)
data['cpu_usage_avg'] = data['node_cpu_usage'].rolling(window=5, min_periods=1).mean().shift(1)
data['memory_usage_avg'] = data['node_memory_usage'].rolling(window=5, min_periods=1).mean().shift(1)

# Label failures with prioritized conditions
conditions = [
    data['event_type'] == 'Error',
    data['cpu_allocation_efficiency'] < 0.1,
    data['memory_allocation_efficiency'] < 0.1,
    data['network_latency'] > 50,
    data['disk_io'] > 1000
]
choices = ['pod_crash', 'cpu_exhaustion', 'memory_exhaustion', 'network_issue', 'disk_exhaustion']
data['failure_type'] = np.select(conditions, choices, default='normal')

# Save cleaned data
data.to_csv(SAVE_DATA_PATH, index=False)
print("Cleaned and labeled dataset saved successfully!")