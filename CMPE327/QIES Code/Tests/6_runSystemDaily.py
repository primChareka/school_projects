import os, traceback,sys
import _merge
import _runBackEnd
import _dailyScript

########### MAIN CODE ##########
if hasattr(__builtins__, 'raw_input'):
    input = raw_input
testDirectories = []
osType = input("What is your OS? Press (1) for macOS or (2) PC\n")
while osType!= "1" and osType != "2":
    print("Invalid entry. You entered: " + osType+" \n")
    osType = input("Please try again with one fo the following options\n1 for macOS or 2 for PC\n")
if osType == "1":
    osType = "macOS"
elif osType == "2":
    osType = "PC"

basePath = os.path.join('..','Tests','FullSystem')
day = 1
    
_dailyScript.runTerminals(osType, basePath, day)
mtsf = _merge.mergeTSF(basePath,day)
csf = 'CSF_' + '%03d' % day+ ".txt"
csf = os.path.join(basePath,'dailyInputs', csf)

_runBackEnd.runBackEnd(osType,mtsf, csf)

