#!/bin/bash
set -e
basedir="$(dirname $(readlink -f $0))"
cd ../../../AppAnalysis
./idroid -t ../ui_evaluation/targetedMethods_startActivity.txt -o $basedir/kickstarterNew ../kickstarter

