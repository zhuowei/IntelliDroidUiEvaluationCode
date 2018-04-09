#!/bin/bash
set -e
scriptdir="$(dirname $0)"
for i in $1/*/appInfo.json
do
	echo $i
	$scriptdir/measureNumLinks.py $i
done
