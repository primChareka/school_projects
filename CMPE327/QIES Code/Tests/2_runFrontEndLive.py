import os
if hasattr(__builtins__, 'raw_input'):
    input = raw_input
validServiceFile = os.path.join("FrontEnd","validServices.txt")
TSF = os.path.join("FrontEnd", "TSF.txt")

osType = input("What is your OS? Press (1) for macOS or (2) PC\n")
while osType!= "1" and osType != "2":
    osType = input("Invalid entry. You entered: " + osType+" \nPlease try again with one fo the following options\n1 for macOS or 2 for PC\n")
if osType == "1":
    os.system("java -classpath ../byteCode/ FrontEnd.FrontEndSystem " + validServiceFile + " " + TSF)
elif osType == "2":
     os.system("java -classpath ..\\byteCode\\ FrontEnd.FrontEndSystem " + validServiceFile + " " + TSF)


