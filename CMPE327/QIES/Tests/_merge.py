import os, sys, traceback
file = ''

# Checks if next TSF exists, and assigns it if it does
def getNextFile(basePath, day, fileNumber):
    global file
    
    #format day string to be two digits and file number string to be three digits
    dayString = '%02d' % day
    fileNumberString = '%03d' % fileNumber

    file = os.path.join(basePath,'outputFiles','TSF_' + dayString + 'day_' + fileNumberString + '.txt')
    exists = os.path.isfile(file)
    if exists:    
        return True
    else:
        return False

# "Main code" to merge TSFs to MTSF
def mergeTSF(basePath, day):
    fileNumber = 1
    ifExists = getNextFile(basePath, day, fileNumber)
    if ifExists:
        MTSF = os.path.join(basePath,'outputFiles','MTS_%02d'% day +'day.txt')
        mtsf = open(MTSF,'w')

        while ifExists:
            tsf = open(file,'r')
            line = tsf.readline()

            while line != 'EOS':
                mtsf.write(line)
                line = tsf.readline()
            tsf.close()
            fileNumber += 1
            ifExists = getNextFile(basePath,day, fileNumber)

        mtsf.write('EOS')
        mtsf.close()
    return MTSF


