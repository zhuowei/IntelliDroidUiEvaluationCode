For reproducing PlayDrone results:

Reference:

1) checkout `feature/update-apktool` branch (3f6c9a83916dafc9ef48ebc00ca7867b37048cf4) from https://github.com/zhuowei/IntelliDroid

2) download these  apps from the PlayDrone Dataset (Package names and sha256 sums of the APKs are provided if you would like to grab them from Archive.org, or ask for the predownloaded .zip). (These are from the top 20 list in November 2014 that are small enough for IntelliDroid to analyze.)

com.android.chrome-2125114
com.google.android.apps.books-30149
com.google.android.gm-4900120
com.google.android.gms-6183036
com.google.android.street-18102
com.rovio.angrybirds-4210
com.sec.spp.push-102

3) extract them to this directory under the subdirectory `playdrone_20_ref_preproc`

4) `../../../AppAnalysis/preprocess/PreprocessDataset.sh playdrone_20_ref_preproc` to preproces them using original IntelliDroid

5) cd AppAnalysis; ./gradlew clean build

6) go to this directory, `./runstatic_ref.sh`
