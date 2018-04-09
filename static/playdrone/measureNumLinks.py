#!/usr/bin/env python3
import sys
import json
with open(sys.argv[1], "r") as infile:
	indata = infile.read()
	appInfo = json.loads(indata)
count=0
for pathId in appInfo["callPaths"]:
	path = appInfo["callPaths"][pathId]
	for chainElem in path["eventChain"]:
		if chainElem["type"] != "ui":
			continue
		if "inDialog" in chainElem:
			break
		if len(chainElem["activities"]) == 0 or chainElem["activities"][0] == "":
			break
		if "viewId" in chainElem:
			count+=1
			break
		if "variables" in chainElem and "\u003cChainedInput1\u003e.getId()" in chainElem["variables"]:
			count+=1
			break
		break
print(count)
