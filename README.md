# k8s-ai

# Kubernetes AI Phase 1: Failure Prediction and Root Cause Analysis

## Overview
This project predicts Kubernetes failures using machine learning and identifies root causes using Generative AI.
Most solutions focus on predicting failures, but very few provide insights into the underlying causes. By integrating Root Cause Analysis (RCA), this solution goes beyond mere prediction, offering actionable insights that help prevent failures and optimize system performance.

## Directory

```
k8s-AI/
├── data/                        # Raw and processed datasets
│   ├── kubernetes_performance_metrics_dataset.csv # Dataset for training model
|   ├── kubernetes_validation.csv                  # Dataset for validation in anomaly detection
|   ├── k8s_with_anomalies.csv                     # Result of anomaly detection
|   ├── root_cause_analysis.csv                    # Root cause analysis report
|
├── model/                       # Saved models and training artifacts
│   ├── RFC_prediction_model.pkl # Trained model for anomaly prediction
│
├── src/                         # Source code for AI and ML pipeline
│   ├── anomaly_detection.py     # Detect anomalies in Kubernetes metrics
│   ├── root_cause_analysis.py   # Explainable AI model for root cause detection
│   ├── train_model.py           # Model training script
│
├── venv/                        # Virtual environment (if using virtualenv)
│
├── .env                         # Environment variables (not committed)
├── .gitignore                   # Ignore files and directories (e.g., .env, venv, models)
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
```

### Demo Video
[Click Here!](https://drive.google.com/drive/folders/1Y7xSzqEnOOqjxzpnyzIdGuORKQVFXzHJ?usp=sharing)

### 📥 **Dataset**  
Download the dataset from [Kaggle](https://www.kaggle.com/datasets/nickkinyae/kubernetes-resource-and-performancemetricsallocation?select=kubernetes_performance_metrics_dataset.csv) and place it inside the `data/` directory.  

## Prerequisites
Before running the project, ensure you have the following installed:

Python 3.8 or higher
pip (Python package manager)

## How to Run

Clone the Repository: git clone https://github.com/your-username/k8s-ai.git

Create a .env File and add Generative AI api key: API_KEY=your_api_key_here

1. Install dependencies: `pip install -r requirements.txt`
2. Train the model: `python train_model.py`
3. Detect anomalies: `python anomaly_detection.py`
4. Analyze root causes: `python root_cause_analysis.py`

### Dependency Issues:

If you encounter dependency conflicts, create a virtual environment and install the dependencies:

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Root Cause Analysis (Generated by LLM)

<img width="1410" alt="Screenshot 2025-03-23 at 8 33 11 PM" src="https://github.com/user-attachments/assets/545981b6-4cc4-4cc1-9eef-94cc0d422360" />





