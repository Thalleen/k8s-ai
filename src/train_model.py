import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import precision_score, recall_score, f1_score
from pathlib import Path

# Define dataset and model paths relative to the script's location
BASE_DIR = Path(__file__).resolve().parent.parent  # Adjust if running from a different directory
DATA_PATH = BASE_DIR / "data" / "kubernetes_performance_metrics_dataset.csv"
MODEL_PATH = BASE_DIR / "model" / "failure_prediction_model.pkl"

data = pd.read_csv(DATA_PATH)

# Drop unnecessary columns
X = data.drop(columns=["failure_type", "timestamp", "event_type"])
y = data["failure_type"]

# Encode categorical columns
categorical_columns = ["pod_name", "namespace", "event_message"]
label_encoders = {}

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le  # Store for inverse transformation if needed

# Encode the target column
y = LabelEncoder().fit_transform(y)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train Model
model = RandomForestClassifier(n_estimators=200, max_depth=20, min_samples_split=2, min_samples_leaf=1)
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))


# Compute global precision, recall, and f1-score
precision = precision_score(y_test, y_pred, average="weighted")
recall = recall_score(y_test, y_pred, average="weighted")
f1 = f1_score(y_test, y_pred, average="weighted")

print(f"Global Precision: {precision:.4f}")
print(f"Global Recall: {recall:.4f}")

# Save the trained model
joblib.dump(model, MODEL_PATH)
print(f"Trained model saved at: {MODEL_PATH}")
