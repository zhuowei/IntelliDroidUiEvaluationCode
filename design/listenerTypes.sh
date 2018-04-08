#!/bin/sh
set -e
rm -r out_$1 ListenerTypesApp_$1.apk || true
cp ../IntelliDroidGuiTestcases/prebuilt/ListenerTypesApp-release.apk ./ListenerTypesApp_$1.apk
basepath="$(dirname $(readlink -f $0))"
inputfile="$(readlink -f ./ListenerTypesApp_$1.apk)"
outdir="$basepath/out_$1"
cd ../../AppAnalysis
preprocess/PreprocessAPK.sh $inputfile
./idroid -t "$basepath/listenertypes_target.txt" -o $outdir "$basepath/ListenerTypesApp_$1"
