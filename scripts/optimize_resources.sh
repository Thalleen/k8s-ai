#!/bin/bash
POD_NAME=$1
echo "[FAILURE] Restarting pod to optimize resource usage: $POD_NAME"
kubectl delete pod $POD_NAME
