#!/bin/sh
set -e
basepath="$(dirname $(readlink -f $0))"
outdir="$basepath/out"
cd ../../../AppAnalysis
./idroid -t "$basepath/kickmock_targets.txt" -o $outdir "$basepath/KickMock"
