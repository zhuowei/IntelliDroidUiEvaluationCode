#!/bin/bash
set -e
rm -r KickMock.apk KickMock KickOut || true
cp app-internal-pre21-release.apk KickMock.apk
SKIP_GATOR=1 ../../../AppAnalysis/preprocess/PreprocessAPK.sh KickMock.apk
# it's Kickstarter: remove Gator (won't help), add ButterKnife
. jdk8_on
../../../AppAnalysis/preprocess/gui-annotation-extract/guiAnnotationExtract.sh KickMock/KickMock.apk KickMock/guiAnnotations.json
