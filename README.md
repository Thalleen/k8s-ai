# 🚀 k8s-ai

## 🔍 Kubernetes AI Phase 1: Failure Prediction and Root Cause Analysis

### Overview
This project leverages Machine Learning and Generative AI to **predict Kubernetes failures** and provide **Root Cause Analysis (RCA)**.

While most solutions stop at anomaly detection, this project goes further by offering **explainable, actionable insights** to help prevent failures and optimize cluster performance.

---

## 📁 Project Structure



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


---

## 🎥 Demo

📽️ **Watch it in action**:  
[👉 Click Here!](https://drive.google.com/drive/folders/1Y7xSzqEnOOqjxzpnyzIdGuORKQVFXzHJ?usp=sharing)

---

## 📥 Dataset

Get the dataset from Kaggle and place it in the `data/` folder:  
🔗 [Kubernetes Resource & Performance Metrics Dataset](https://www.kaggle.com/datasets/nickkinyae/kubernetes-resource-and-performancemetricsallocation?select=kubernetes_performance_metrics_dataset.csv)

---

## ⚙️ Prerequisites

Make sure you have:

- Python **3.8+**
- `pip` installed

---

## 🛠️ Setup & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/Thalleen/k8s-ai.git
cd k8s-ai
```


## How to Run

### 2. Configure Environment Variables
Create a .env file in the root directory and add your Generative AI API key:

```bash
API_KEY=your_api_key_here
```

#### 1. Install dependencies: 
```bash
pip install -r requirements.txt
```
#### 2. Train the model: 
```bash
python train_model.py
```

#### 3. Detect anomalies: 
```bash
python anomaly_detection.py
```
4. Analyze root causes: `python root_cause_analysis.py`

### Dependency Issues

If you encounter dependency conflicts, it's recommended to create and activate a virtual environment before installing the requirements:

```bash
python -m venv venv
source venv/bin/activate   # On Linux/macOS
# On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

# 🚀 k8s-ai - Phase 2

## 🧠 Enhanced Kubernetes Insights with LLM-Powered Diagnostics

### Overview
Building upon the foundation of failure prediction and anomaly detection in Phase 1, Phase 2 of **k8s-ai** introduces a powerful capability: **intelligent diagnosis of Kubernetes errors and automated Root Cause Analysis (RCA)** using Large Language Models (LLMs).

Instead of just identifying anomalies, this phase focuses on providing **human-readable, context-aware explanations** for errors by feeding specific Kubernetes attributes and metrics to an LLM. This enables faster troubleshooting, deeper understanding of complex issues, and ultimately, more resilient and stable Kubernetes clusters.

---

## 💡 Key Features

* **LLM-Powered Error Diagnosis:** Pass specific Kubernetes attributes and metrics to a configured LLM to get detailed diagnostic insights.
* **Contextual Root Cause Analysis:** The LLM analyzes the provided context (metrics, logs, configurations) to infer potential root causes.
* **Explainable Insights:** Receive natural language explanations and potential reasons behind the observed errors.
* **Actionable Recommendations:** The LLM can suggest potential steps to mitigate the diagnosed issues.
* **Integration with Existing Monitoring:** Designed to work with data collected from your existing Kubernetes monitoring tools.
* **Extensible Framework:** Easily adapt and configure the prompts and context provided to the LLM.

---

<img width="1410" alt="Screenshot 2025-03-23 at 8 33 11 PM" src="https://github.com/user-attachments/assets/545981b6-4cc4-4cc1-9eef-94cc0d422360" />


### <ul> Utilize LLM-Based Error Diagnosis
The core logic for interacting with the LLM is in the **src/root_cause_analysis.py** script. You will need to integrate this into your workflow to feed relevant Kubernetes attributes and metrics.

##### 📄note 
*The effectiveness of the LLM-based diagnosis heavily relies on the quality of the prompts. You can modify the prompts in src/root_cause_analysis.py to tailor the LLM's behavior and the level of detail in the diagnosis and RCA.*
