# agent.py

import pandas as pd
import os
import json
from datetime import datetime
from rules_engine import get_remediation_plan

# Load RCA report 
df = pd.read_csv("data/test_root_cause_analysis.csv", header=None,
                 names=["pod_name", "namespace", "predicted_failure_label", "root_cause_analysis"])

# Initialize remediation log
remediation_log = []

for _, row in df.iterrows():
    issue = row["predicted_failure_label"]
    pod_name = row["pod_name"]
    namespace = row["namespace"]
    explanation = row["root_cause_analysis"]

    # Get remediation action
    
    get_remediation_plan(issue, pod_name)

    remediation_log.append(f"Pod name: {pod_name} in namespace: {namespace} faced issue {issue}. Remedied with remediation agent\n")
    
log_file = "remediation_logs.txt"
with open(log_file, "a") as f:
    for log in remediation_log:
        f.write(log)

print(f"\n✅ Remediation completed. Log saved to {log_file}")
