#!/bin/bash
POD_NAME=$1
NODE=$(kubectl get pod $POD_NAME -o jsonpath='{.spec.nodeName}')
echo "[OVERHEATING] Evacuating node: $NODE"
kubectl drain $NODE --ignore-daemonsets --delete-local-data
kubectl cordon $NODE
