#!/bin/bash
set -e
rm CalabashServer.apk ResignedApp.apk || true
../../../calabash/make_server.py ca.utoronto.intellidroid.guieval.manybuttonsapp CalabashServer.apk
../../../calabash/resign_apk.py ../../IntelliDroidGuiTestcases/prebuilt/ManyButtonsApp-release.apk ResignedApp.apk
adb uninstall ca.utoronto.intellidroid.guieval.manybuttonsapp || true
adb uninstall intellidroid.calabash.ca.utoronto.intellidroid.guieval.manybuttonsapp || true
adb install -r CalabashServer.apk
adb install -r ResignedApp.apk

