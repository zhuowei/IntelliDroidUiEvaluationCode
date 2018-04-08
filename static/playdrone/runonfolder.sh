#!/bin/bash
set -e
srcfolder="$(readlink -f $1)"
dstfolder="$(readlink -f $2)"
targetfile="$(readlink -f ../../targetedMethods_startActivity.txt)"
cd ../../../AppAnalysis
mkdir $dstfolder || true
#idroid="./IntelliDroidAppAnalysis"
idroid="./idroid"
for i in $srcfolder/*
do
	date
	$idroid -t $targetfile -o $dstfolder/`basename $i` $i
done
date
