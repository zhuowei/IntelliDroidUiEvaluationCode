#!/bin/bash
set -e
for i in $1/*/appInfo.json
do
	echo $i
	./measureNumLinks.py $i
done
