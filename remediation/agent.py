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

    

    # if remediation_cmd:
    #     print(f"[ACTION] Issue: {issue} on Pod: {pod_name} in Namespace: {namespace} → Running: {remediation_cmd}")
        
    #     # Optional: run in the correct namespace if needed
    #     # You can inject namespace logic in your scripts if required
    #     os.system(remediation_cmd)

    #     remediation_log.append({
    #         "timestamp": datetime.utcnow().isoformat(),
    #         "issue": issue,
    #         "pod": pod_name,
    #         "namespace": namespace,
    #         "remediation": remediation_cmd,
    #         "explanation": explanation[:300] + "..."  # Truncate explanation for readability
    #     })
    # else:
    #     print(f"[SKIP] No remediation rule for issue: {issue}")

# Save remediation actions log
log_file = "remediation_logs.json"
with open(log_file, "w") as f:
    json.dump(remediation_log, f, indent=2)

print(f"\n✅ Remediation completed. Log saved to {log_file}")
