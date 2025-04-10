#!/bin/bash
POD_NAME=$1
NODE=$(kubectl get pod $POD_NAME -o jsonpath='{.spec.nodeName}')
echo "[MOVE] Draining node: $NODE and rescheduling pod: $POD_NAME"
kubectl drain $NODE --ignore-daemonsets --delete-local-data
kubectl delete pod $POD_NAME
