#!/bin/bash
set -e
rm CalabashServer.apk ResignedApp.apk || true
../../../calabash/make_server.py com.kickstarter.kickstarter.internal CalabashServer.apk
../../../calabash/resign_apk.py app-internal-pre21-release.apk ResignedApp.apk
adb uninstall com.kickstarter.kickstarter.internal || true
adb uninstall intellidroid.calabash.com.kickstarter.kickstarter.internal || true
adb install -r CalabashServer.apk
adb install -r ResignedApp.apk

