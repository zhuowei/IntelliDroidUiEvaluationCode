My attempt to setup IntelliDroid with Gator on a new computer running Ubuntu 16.04.

- download Gator, extract into AppAnalysis/preprocess
- follow https://askubuntu.com/questions/454253/how-to-run-32-bit-app-in-ubuntu-64-bit
- also need zlib1g:i386
- sudo apt install ant
- make sure ANDROID_HOME set
- install Android 23 sdk in Android Studio
- install an Java 7 - OpenJDK works, but 16.04 doesn't package it anymore, can't find a JDK7 from Oracle either - Java 8 hates WALA

Conclusion: stay on the Ubuntu 14.04 machine which does work
