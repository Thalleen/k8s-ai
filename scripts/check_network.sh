#!/bin/bash
POD_NAME=$1
echo "[NETWORK] Running traceroute from pod: $POD_NAME"
kubectl exec -it $POD_NAME -- traceroute 8.8.8.8
