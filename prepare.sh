#!/bin/sh
# clone the testcase apps, install the idroid wrapper
set -e
git clone https://github.com/zhuowei/IntelliDroidGuiTestcases.git
cp common/idroid ../AppAnalysis/idroid
