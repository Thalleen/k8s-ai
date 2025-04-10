import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from pathlib import Path

# Define dataset and model paths
BASE_DIR = Path(__file__).resolve().parent.parent  # Adjust if running from a different directory
DATA_PATH = BASE_DIR / "data" / "kubernetes_validation.csv"
TRAIN_DATA_PATH = BASE_DIR / "data" / "kubernetes_performance_metrics_dataset.csv"  # Training data to recreate LabelEncoder
MODEL_PATH = BASE_DIR / "model" / "RFC_prediction_model.pkl"
SAVE_DATA_PATH = BASE_DIR / "data" / "k8s_with_anomalies.csv"

# Load the training dataset to recreate LabelEncoder
train_data = pd.read_csv(TRAIN_DATA_PATH)

# Recreate the LabelEncoder
failure_label_encoder = LabelEncoder()
failure_label_encoder.fit(train_data["failure_type"])

# Load the validation dataset
data = pd.read_csv(DATA_PATH)
data = data.drop(columns=["failure_type", "timestamp", "event_type"])

# Encode categorical columns
categorical_columns = ["pod_name", "namespace", "event_message"]
label_encoders = {}

for col in categorical_columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le  # Store for inverse transformation if needed

# Load the trained model
model = joblib.load(MODEL_PATH)

# Predict failures
data['predicted_failure'] = model.predict(data)

# Convert predicted values back to original failure type labels
data['predicted_failure_label'] = failure_label_encoder.inverse_transform(data['predicted_failure'])

# Save the results
data.to_csv(SAVE_DATA_PATH, index=False)

print("Predictions saved with original failure labels!")

