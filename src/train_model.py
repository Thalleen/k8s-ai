import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
from collections import Counter
from pathlib import Path


# Define dataset and model paths relative to the script's location
BASE_DIR = Path(__file__).resolve().parent.parent  # Adjust if running from a different directory
DATA_PATH = BASE_DIR / "data" / "k8s_cleaned_labeled.csv"
MODEL_PATH = BASE_DIR / "model" / "failure_prediction_model.pkl"


data = pd.read_csv(DATA_PATH)

# Fix FutureWarning (Pandas 3.0 issue)
data = data.assign(**{col: data[col].fillna(data[col].mean()) for col in ['cpu_usage_avg', 'memory_usage_avg', 'node_cpu_usage', 'node_memory_usage']})

# Drop rows where failure_type is NaN
data.dropna(subset=['failure_type'], inplace=True)

# Feature Engineering
data['cpu_memory_ratio'] = np.where(data['node_memory_usage'] == 0, 0, data['node_cpu_usage'] / data['node_memory_usage'])
data['disk_network_ratio'] = np.where(data['network_latency'] == 0, 0, data['disk_io'] / data['network_latency'])

# Rolling Averages
window_size = 5
data['cpu_usage_rolling_avg'] = np.convolve(data['node_cpu_usage'], np.ones(window_size)/window_size, mode='same')
data['memory_usage_rolling_avg'] = np.convolve(data['node_memory_usage'], np.ones(window_size)/window_size, mode='same')

# Features & Target
features = [
    'cpu_allocation_efficiency', 'memory_allocation_efficiency',
    'disk_io', 'network_latency', 'node_cpu_usage',
    'node_memory_usage', 'cpu_usage_avg', 'memory_usage_avg',
    'cpu_memory_ratio', 'disk_network_ratio',
    'cpu_usage_rolling_avg', 'memory_usage_rolling_avg'
]
X = data[features]
y = data['failure_type']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Print class distribution before SMOTE
print("Before SMOTE:", Counter(y_train))

# Apply SMOTE for multi-class classification
smote = SMOTE(sampling_strategy='auto', random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# Print class distribution after SMOTE
print("After SMOTE:", Counter(y_train_res))

# Train Model
model = RandomForestClassifier(n_estimators=200, max_depth=20, min_samples_split=2, min_samples_leaf=1, random_state=42)
model.fit(X_train_res, y_train_res)

# Evaluate Model
y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(model, MODEL_PATH)
print(f"Trained model saved at: {MODEL_PATH}")
