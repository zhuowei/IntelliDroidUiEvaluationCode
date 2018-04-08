#!/bin/sh
set -e
rm -r out ManyButtons.apk ManyButtons || true
cp ../../IntelliDroidGuiTestcases/prebuilt/ManyButtonsApp-release.apk ./ManyButtons.apk
basepath="$(dirname $(readlink -f $0))"
inputfile="$(readlink -f ./ManyButtons.apk)"
outdir="$basepath/out"
cd ../../../AppAnalysis
preprocess/PreprocessAPK.sh $inputfile
./idroid -t "$basepath/manybuttons_targets.txt" -o $outdir "$basepath/ManyButtons"
