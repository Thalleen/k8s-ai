# rules_engine.py
import sys
import os






def get_remediation_plan(issue_type, pod_name):
    myDir = os.getcwd()
    sys.path.append(myDir)

    from pathlib import Path
    path = Path(myDir)
    a=str(path.parent.absolute())

    sys.path.append(a)
    from ClusterManager.clusterManager import DeploymentManager
    deployment_manager =DeploymentManager("default","service-a-deployment")
    deployment = deployment_manager.getDeploymentConfig()
    resources = deployment.spec.template.spec.containers[0].resources


    SCALE_FACTOR = 1.5
    cpu = float((resources.limits.get("cpu")[:-1]))*SCALE_FACTOR
    cpu_unit = resources.limits.get("cpu")[-1]
    memory = float((resources.limits.get("memory")[:-2]))*SCALE_FACTOR
    memory_unit = resources.limits.get("memory")[-2:]

    updated_cpu = (str(cpu)+cpu_unit)
    updated_memory = (str(memory)+memory_unit)
    if issue_type == "cpu_exhaustion":
        print("here")
        deployment_manager.updateDeploymentConfig(cpu=updated_cpu)
    elif issue_type == "memory_exhaustion":
        print("here2")
        deployment_manager.updateDeploymentConfig(memory=updated_memory)
    # elif issue_type == "disk_io_bottleneck":
    #     return f"bash scripts/move_pod.sh {pod_name}"
    # elif issue_type == "network_latency_issue":
    #     return f"bash scripts/check_network.sh {pod_name}"
    # elif issue_type == "overheating":
    #     return f"bash scripts/evacuate_node.sh {pod_name}"
    # elif issue_type == "pod_termination":
    #     return f"bash scripts/log_and_restart.sh {pod_name}"
    # elif issue_type == "pod_failure":
    #     return f"bash scripts/optimize_resources.sh {pod_name}"
    # else:
    #     return None
