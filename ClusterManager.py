from kubernetes import client
from ClusterManager.clusterManager import DeploymentManager
# Example usage
namespace = "default"
deployment_name = "service-a-deployment"




depManager = DeploymentManager(namespace,deployment_name)

depManager.updateReplicas(6)

cpu = "150m"
memory = "280Mi"
image = None
env = [
    {"name": "MY_VAR", "value": "new-value"},
    {"name": "ANOTHER_VAR", "value": "another-new-value"}
]
# volume = {
#     "volumes": [
#         client.V1Volume(
#             name="my-volume",
#             persistent_volume_claim=client.V1PersistentVolumeClaimVolumeSource(claim_name="my-pvc")
#         )
#     ],
#     "volumeMounts": [
#         client.V1VolumeMount(mount_path="/data", name="my-volume")
#     ]
# }

depManager.updateDeploymentConfig(cpu,memory,image,env)
