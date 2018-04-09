#!/bin/bash
set -e
rundir="$(readlink -f out)"
cd ../../../DynamicClient
./IntelliDroidDynamicClient.py "$rundir" << EOF
START
TRIGGER 0
CLOSE
EOF
