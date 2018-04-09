#!/bin/bash
set -e
rundir="$(readlink -f out)"
cd ../../../DynamicClient
for i in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14; do
NO_STARTACTIVITY=1 ./IntelliDroidDynamicClient.py "$rundir" << EOF
START
TRIGGER $i
CLOSE
EOF
sleep 0.2
done
