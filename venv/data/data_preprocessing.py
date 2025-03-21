import pandas as pd

# Load the dataset
try:
    data = pd.read_csv('/Users/thalleencn/Desktop/k8s-ai/venv/data/kubernetes_performance_metrics_dataset.csv')
    print("Dataset loaded successfully!")
    print(data.head())  # Display the first few rows
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# Fill missing values in numeric columns with the mean
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

# Convert 'timestamp' to DateTime
try:
    data['timestamp'] = pd.to_datetime(data['timestamp'])
except Exception as e:
    print(f"Error converting 'timestamp' column: {e}")
    exit()

# Save the cleaned dataset
try:
    data.to_csv('/Users/thalleencn/Desktop/k8s_cleaned.csv', index=False)
    print("Cleaned dataset saved successfully!")
except Exception as e:
    print(f"Error saving cleaned dataset: {e}")