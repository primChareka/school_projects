import os, traceback
def runBackEnd(osType,mtsf,csf):
    try:
        if osType == "macOS":
            os.system("java -classpath ../byteCode/ BackEnd.BackEndSystem " + mtsf + " " + csf)
        elif osType == "PC":
                os.system("java -classpath ..\\byteCode\\ BackEnd.BackEndSystem " + mtsf + " " + csf)
        else:
                raise Exception("Specified system must either be OS or PC. Attempted to use: "+ osType)
    except:
        traceback.print_exc()
        exit()
