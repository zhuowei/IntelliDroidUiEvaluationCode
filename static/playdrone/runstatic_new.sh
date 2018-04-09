#!/bin/bash
set -e
if [[ ! -e playdrone_20_new_preproc ]]; then
	mkdir playdrone_20_new_preproc
	cp playdrone_set/*.apk playdrone_20_new_preproc/
	../../../AppAnalysis/preprocess/PreprocessDataset.sh playdrone_20_new_preproc
fi
./runonfolder.sh playdrone_20_new_preproc playdrone_20_new_static 2>&1 | tee -a static_log.txt
