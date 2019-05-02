import os, traceback,sys
import datetime
date = datetime.datetime.today().strftime('%Y_%m_%d')
passMessage = " test case passed"
failMessage = " test case failed"
inputFiles = []
outputFiles =  []
validServiceFile = os.path.join("FrontEnd","validServices.txt")
TSF = os.path.join("FrontEnd", "TSF.txt")

########### FUNCTIONS ##########
def getTestFiles(testFilesPath):
    global inputFiles
    global outputFiles
    for file in sorted(os.listdir(testFilesPath)):
        if 'input.txt' in file:
            inputFiles.append(file)
        elif 'Expected.txt' in file:
            outputFiles.append(file)

def getResultsDirectory(testFilesPath,code):
    #Preparartion to write out summary of test into file
    #If the directory for the current test date does not exist initalize
    #it before making the summarry file. Summary files are named
    #consecuitively based on the number of files currently in the test
    #date folder
    resultFilesPath = os.path.join(testFilesPath,code)+'_ResultFiles'
    resultsDirectory = os.path.join(resultFilesPath,code)+'_'+date
    if not os.path.exists(resultsDirectory):
        os.makedirs(resultsDirectory)

    #Get the number off tests which have been run and turn it into a 3 digit number
    allFolders = os.listdir(resultsDirectory)
    num = sum("Test" in file for file in allFolders) + 1
    prefix = '%03d' % num

    #create new directory for current test
    resultsDirectory = os.path.join(resultsDirectory,"Test_") + str(prefix)
    if not os.path.exists(resultsDirectory):
        os.makedirs(resultsDirectory)
        
    return resultsDirectory;

    
def organizeOutputFiles(resultsDirectory,testName):
    os.system("mv " + TSF + " " + os.path.join(resultsDirectory,testName) + "tsf.txt")
    os.system("mv stdOutput.txt " + os.path.join(resultsDirectory,testName) + "stdOutput.txt")
    

def makeSummaryFile(resultsDirectory, code, testSummaryDict):   
    testNum = resultsDirectory[len(resultsDirectory)-3:]
    resultFile = open(os.path.join(resultsDirectory,testNum)+'_Summary'+'.txt', 'w') #i.e. LGI_2018_10_02/LGI__Summary001.txt

    resultFile.write("********************** "+date+" TEST CASES **********************\n\n")
    #Once file is made sort the the test results and write them into the summary file
    #passFailSummary is a dictionary of form {fail: testCaseNames[String], pass: testCaseNames[String],}
    passFailSummary = invert_dict(testSummaryDict)
    resultFile.write("============== FAILED TEST CASES ==============\n")
    if 'fail' in passFailSummary:
        #Get list of failed test cases and sort by test name then write to file
        failedTests = passFailSummary['fail'] 
        failedTests.sort()
        for result in failedTests:
            resultFile.write(result+'\n')
    else:
        resultFile.write('NO FAILED TESTS\n')

    resultFile.write("============== PASSED TEST CASES ==============\n")
    if 'pass' in passFailSummary:
        #Get list of successful test cases and sort by test name then write to file
        passedTests = passFailSummary['pass']
        passedTests.sort()
        for result in passedTests:
            resultFile.write(result+'\n')
    else:
        resultFile.write('ALL TESTS FAILED\n')

    resultFile.close()
    print("Testing done. Results stored in file: "+os.path.join(resultsDirectory,testNum))

def invert_dict(d):
    #Takes a dictionary d and inverts it into a a histogram
    #(i.e a dictionarycomprised of lists such that key's mapping
    #to the same value in the original dictionary d are placed
    #in the same list.
    #EXAMPLE {a:0,b:0,c:1,d:2,e:1} -> {0:[a,b],1:[c,e],2:[d]}
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

def runTransactionTest(code,osType):
    global inputFiles
    global outputFiles
    global validServiceFile
    global TSF
    
    #Get a list of the input file names and the expected output file names
    testFilesPath = os.path.join('FrontEnd',code)
    getTestFiles(testFilesPath)

    #Get name of directory to store results
    resultsDirectory = getResultsDirectory(testFilesPath,code)
    
    testSummaryDict = dict() #Used to record passed tests and failed tests
    for inputFileName, expectedTSFFileName in zip(inputFiles,outputFiles):  #inputFiles and outputFiles are global variables populated in the function call getTestFiles() above
        key = inputFileName
        try:
            if(inputFileName[4:7]!=expectedTSFFileName[4:7]):
                raise Exception("ERROR: Input file name:\n\t\t" +inputFileName+"\ndoes not match output file name:\n\t\t" +expectedTSFFileName)
        except:
            traceback.print_exc()
            exit()
        #run Java file with test case input file and store results in temp file
        inputFilePath = os.path.join(testFilesPath,inputFileName)
        try:
            if osType == "macOS":
                #os.system("java -classpath ../byteCode/ FrontEnd.FrontEndSystem " + validServiceFile + " " + TSF)

                os.system("java -classpath ../byteCode/ FrontEnd.FrontEndSystem " + validServiceFile + " " + TSF + " < " + inputFilePath + " > stdOutput.txt")
            elif osType == "PC":
                os.system("java -classpath ..\\byteCode\\ FrontEnd.FrontEndSystem " + validServiceFile + " " + TSF + " < " + inputFilePath + " > stdOutput.txt")
            else:
                raise Exception("Specified system must either be OS or PC. Attempted to use: "+ osType)
        except:
            traceback.print_exc()
            exit()
        #open the test case's expected TSF file and compare to results in actusal TSF
        expectedTSF = open(os.path.join(testFilesPath,expectedTSFFileName))
        actualTSF = open(TSF) #generated by the java code

        expectedTSFContents = expectedTSF.read()
        expectedTSFContents = expectedTSFContents.strip() #does not get rid of \n in middle of files, only ends
    
        actualTSFContents = actualTSF.read()
        actualTSFContents = actualTSFContents.strip()
        
        #If the file contents above are the same, the test passed else it failed. Store result with pass/fail message
        testName = inputFileName[:len(inputFileName)-9] #i.e. LGI_001
        if expectedTSFContents == actualTSFContents:
            testSummaryDict[testName+passMessage] = "pass"
        else:
            message = testName+failMessage + "\n   Expected out was\n\t" + expectedTSFContents + "\n   Test Output was\n\t" + actualTSFContents 
            testSummaryDict[message] = "fail"

        expectedTSF.close()
        actualTSF.close()

        organizeOutputFiles(resultsDirectory,testName)
        
        
    makeSummaryFile(resultsDirectory, code, testSummaryDict)
   
    inputFiles = []
    outputFiles = []
    


########### MAIN CODE ##########
if hasattr(__builtins__, 'raw_input'):
    input = raw_input
testDirectories = []
osType = input("What is your OS? Press (1) for macOS or (2) PC\n")
while osType!= "1" and osType != "2":
    osType = input("Invalid entry. You entered: " + osType+" \nPlease try again with one fo the following options\nmacOS or PC\n")
if osType == "1":
    osType = "macOS"
elif osType == "2":
    osType = "PC"

for code in os.listdir('FrontEnd'):
    if os.path.isdir(os.path.join('FrontEnd',code)):
        testDirectories.append(code);
decision = input("Would you like to test one or all transactions?\nPress (1) for one transaction (2) for all transactions or (q) to quit\n")
while decision != str(1) and decision != str(2) and decision != "q":
    print("You entered \n" + decision)
    print("Invalid entry, please try again using one of the following options")
    decision = input("Would you like to test one or all transactions?\nPress (1) for one transaction (2) for all transactions or (q) to quit\n")

if decision == "q":
    exit()
elif decision == str(2):
    #User opted to test all transactions. Systematically iterating through all folders
    for code in testDirectories:
        runTransactionTest(code, osType)
elif decision == str(1):
    #This means the user opted to only test one transaction. Need user to specifiy which one 
    print("Which transaction do you want to test? \nEnter one of the transaction codes or press (q) to quit:")
    i=0;
    for code in testDirectories:
        sys.stdout.write(code + "\t")
        i=i+1
        if i%3 == 0:
            print("")
    code = input("\n")
    while code not in testDirectories and code != "q":
        print("You entered \n" + code)
        print("Invalid entry, please try again using one of the following options or press (q) to quit")
        i=0
        for code in testDirectories:
            sys.stdout.write(code + "\t")
            i=i+1
            if i%3 == 0:
                print("")
        code = input("\n")
    if code == "q":
        exit()
    else:
        runTransactionTest(code, osType)
     
