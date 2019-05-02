import os, traceback,sys
########### FUNCTIONS ##########
def getTestFiles(testFilesPath):
    inputFiles = []
    for file in os.listdir(testFilesPath):
        if 'input.txt' in file:
            inputFiles.append(file)
    return inputFiles

def runTerminals(osType, basePath, day):
    #Set the VSF file path and name
    vsf = 'VSF_' + '%03d' % day+ ".txt"
    vsf = os.path.join(basePath,'dailyInputs',vsf)

    #Get a list of the input file names and the expected output file names
    testFilesPath = os.path.join(basePath, 'dailyInputs')
    inputFiles = getTestFiles(testFilesPath)  
    for inputFileName in inputFiles:
        #For each input file, generate the correct path corresponding tsf output file path
        inputFilePath = os.path.join(testFilesPath,inputFileName)     
        tsf = 'TSF_' + '%02d' % day + 'day_' + inputFileName[6:9] + '.txt'
        tsf = os.path.join(basePath,'outputFiles',tsf)
      
        #run Java file with input file listed above      
        try:
            if osType == "macOS":
                command = "java -classpath ../byteCode/ FrontEnd.FrontEndSystem "
                command += vsf + " " + tsf + " < " + inputFilePath
                command += " > FullSystem/outputFiles/Extra/stdout"+inputFileName
            elif osType == "PC":
                command = "java -classpath ..\\byteCode\\ FrontEnd.FrontEndSystem "
                command += vsf + " " + tsf + " < " + inputFilePath
                command += " > FullSystem\\outputFiles\\Extra\\stdout"+inputFileName
            else:
                raise Exception("Specified system must either be OS or PC. Attempted to use: "+ osType)
        except:
            traceback.print_exc()
            exit()

        os.system(command)
