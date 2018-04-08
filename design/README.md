# ListenerTypesApp

Check out original branch

`./listenerTypes.sh original`

look at `out_original/appInfo.json`, check for IDs - only last one has it

Check out new branch

do a `./gradlew clean build`

`./listenerTypes.sh new`

look at `out_new/appInfo.json`, check for IDs: all three should have ID; the last one has wrong ID from Gator but correct ID from IntelliDroid constraints
