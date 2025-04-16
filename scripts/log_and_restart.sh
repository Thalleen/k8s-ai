#!/bin/bash
POD_NAME=$1
mkdir -p logs
echo "[TERMINATION] Logging and restarting: $POD_NAME"
kubectl describe pod $POD_NAME > logs/$POD_NAME.log
kubectl delete pod $POD_NAME
