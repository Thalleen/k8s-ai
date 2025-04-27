from kubernetes import client, config
from kubernetes.client.rest import ApiException
import time

class DeploymentManager:
    def __init__(self,namespace,deploymentName):
        self.namespace = namespace
        self.deploymentName = deploymentName
        # Load Kubernetes configuration from default location (~/.kube/config)
        config.load_kube_config()
        # Create API clients
        self.apps_v1 = client.AppsV1Api()
        self.core_v1 = client.CoreV1Api()

    def updateReplicas(self,number):
        """
    Change the number of replicas in a deployment.
    """
        try:
            # Get the deployment
            deployment = self.apps_v1.read_namespaced_deployment(self.deploymentName, self.namespace)
            
            # Update replicas
            deployment.spec.replicas = number
            
            # Patch the deployment
            self.apps_v1.patch_namespaced_deployment(self.deploymentName, self.namespace, deployment)
            
            return self.deploymentName,number

        except client.ApiException as e:
            print(f"Failed to update deployment: {e}")
    
    def getDeploymentConfig(self):
        """
        Get the current configuration of a deployment.
        """
        deployment = self.apps_v1.read_namespaced_deployment(self.deploymentName, self.namespace)
        return deployment

    def updateDeploymentConfig(self, cpu=None, memory=None, image=None, env=None, volume=None):
        """
        Update various configurations of pods in a deployment."""
        try:
            while True:  # Retry mechanism for handling conflicts
                try:
                    # Get the latest version of the deployment
                    deployment = self.apps_v1.read_namespaced_deployment(self.deploymentName, self.namespace)
                    
                    print("I am here")
                
                    # Update container resources
                    resourceDict = {}
                    if cpu is not None:
                        resourceDict["cpu"] = cpu
                    if memory is not None:
                        resourceDict["memory"] = memory

                    if resourceDict:
                        deployment.spec.template.spec.containers[0].resources = client.V1ResourceRequirements(
                            requests=resourceDict,
                            limits=resourceDict
                        )

                    # Update container image
                    if image is not None:
                        deployment.spec.template.spec.containers[0].image = image

                    # Update environment variables
                    if env is not None:
                        existing_env = deployment.spec.template.spec.containers[0].env if deployment.spec.template.spec.containers[0].env else []
                        new_env = []
                        for var in env:
                            existing_var = next((e for e in existing_env if e.name == var["name"]), None)
                            if existing_var:
                                existing_var.value = var["value"]
                            else:
                                new_env.append(client.V1EnvVar(name=var["name"], value=var["value"]))
                        deployment.spec.template.spec.containers[0].env = existing_env + new_env

                    # Update volume mounts
                    if volume is not None:
                        deployment.spec.template.spec.volumes = volume["volumes"]
                        deployment.spec.template.spec.containers[0].volumeMounts = volume["volumeMounts"]

                    # Patch the deployment
                    self.apps_v1.patch_namespaced_deployment(self.deploymentName, self.namespace, deployment)

                    return self.deploymentName, cpu, memory

                except ApiException as e:
                    if e.status == 409:  # Handle conflict error
                        print("Conflict detected. Retrying with updated resource...")
                        time.sleep(1)  # Brief delay before retrying
                        continue  # Retry operation
                    else:
                        raise e  # Raise other exceptions

        except ApiException as e:
            raise e
