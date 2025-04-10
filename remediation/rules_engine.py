# rules_engine.py

def get_remediation_plan(issue_type, pod_name):
    if issue_type == "cpu_exhaustion":
        return f"bash scripts/scale_cpu.sh {pod_name}"
    elif issue_type == "memory_exhaustion":
        return f"bash scripts/restart_pod.sh {pod_name}"
    elif issue_type == "disk_io_bottleneck":
        return f"bash scripts/move_pod.sh {pod_name}"
    elif issue_type == "network_latency_issue":
        return f"bash scripts/check_network.sh {pod_name}"
    elif issue_type == "overheating":
        return f"bash scripts/evacuate_node.sh {pod_name}"
    elif issue_type == "pod_termination":
        return f"bash scripts/log_and_restart.sh {pod_name}"
    elif issue_type == "pod_failure":
        return f"bash scripts/optimize_resources.sh {pod_name}"
    else:
        return None
