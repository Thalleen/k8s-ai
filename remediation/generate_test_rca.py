import pandas as pd

data = [{
    "pod_name": "demo-deploy",
    "namespace": "default",
    "predicted_failure_label": "cpu_exhaustion",
    "root_cause_analysis": "The predicted failure is `cpu_exhaustion`, driven by high CPU usage and low allocation efficiency."
}]

df = pd.DataFrame(data)
df.to_csv("data/test_root_cause_analysis.csv", index=False, header=False)
