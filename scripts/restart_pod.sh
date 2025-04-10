#!/bin/bash
POD_NAME=$1
echo "[SCALE] Scaling CPU-bound pod: $POD_NAME"
kubectl scale deployment $POD_NAME --replicas=3
