# k8s-ai

# Kubernetes AI Phase 1: Failure Prediction and Root Cause Analysis

## Overview
This project predicts Kubernetes failures using machine learning and identifies root causes using Generative AI.

## Directory

Download the dataset from this link and add it under the data/: [Click Here](https://www.kaggle.com/datasets/nickkinyae/kubernetes-resource-and-performancemetricsallocation?select=kubernetes_performance_metrics_dataset.csv)


8S-AI/
├── data/                        # Raw and processed datasets
│   ├── kubernetes_performance.csv
|
├── model/                       # Saved models and training artifacts
│   ├── failure_prediction_model.pkl
│
├── src/                         # Source code for AI and ML pipeline
│   ├── anomaly_detection.py     # Detect anomalies in Kubernetes metrics
│   ├── data_preprocessing.py    # Data cleaning and feature engineering
│   ├── root_cause_analysis.py   # Explainable AI model for root cause detection
│   ├── train_model.py           # Model training and evaluation script
│   ├── visualize_results.py     # Script for plotting results and insights
│
├── venv/                        # Virtual environment (if using virtualenv)
│
├── .env                         # Environment variables (not committed)
├── .gitignore                   # Ignore files and directories (e.g., .env, venv, models)
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation 

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Preprocess the data: `python data_preprocessing.py`
3. Train the model: `python train_model.py`
4. Detect anomalies: `python anomaly_detection.py`
5. Analyze root causes: `python root_cause_analysis.py`
6. Visualize results: `python visualize_results.py`
