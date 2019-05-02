PREREQUISITES:
The tests scripts are compatible with MacOS and Windows PC. They can be run using python 2 or python 3. The program utilizes a JDK (tested with 8u191) and a JRE (tested with 1.8.0_191) to compile and run Java code. Note that the scripts are case sensitive when responding to the prompts 

COMPILING THE CODE
It is recommend to recompile the source code after first downloading the project. This can be done by completing the following steps:
	1. In a terminal window, Navigate to the directory "Tests"
	2. Run the script 1_compileFrontEnd.py
	3. Once the script is running, follow the prompts provided by the program.
	4. Run the script 4_compileBackEnd.py
	5. Once the script is running, follow the prompts provided by the program.

INTERACTIVELY RUNNING THE FRONT END PROGRAM
The QIES program can be run live allowing you to interact with the program as a live agent or planner.
This can be done by completing the following steps:
	1. In a terminal window, navigate to the directory "Tests"
	2. Run the script 2_runFrontEndLive.py
	3. Once the script is running, follow the prompts provided by the program.
The service file used to run the front end must be stored in /FrontEnd and must be named validServices.txt for this script to work. The file name and location can be changed if the corresponding code (Line 4) in script 2_runFrontEndLive.py is also changed 

RUNNING THE FRONT END TEST SCRIPTS
The automated front-end testing script allows you to test one or all of transactions at once. It stores the resulting files in each transactions respective results folder (further details on this provided in the next section). 
	1. In a terminal window, Navigate to the directory "Tests"
	2. Run the script 3_runFrontEndTests.py
	3. Once the script is running, follow the prompts provided by the program. 
For this script to work, the service file and TSF used to run the front end must be stored in /FrontEnd and must be named validServices.txt and TSF.txt respectively. The file name and location can be changed if the corresponding code (Line 8 and 9 respectively) in script 3_runFrontEndTests.py is also changed 

CHECKING FRONT END TESETING OUTPUTS
	1. Navigate to Tests/FrontEnd
	2. Select the folder of the transaction tested above which you wish to inspect.
	3. Select the XXX_ResultFiles folder (where XXX is the transaction code).
	4. Select the folder labeled with the date on which the script was run on  
	5. Select the folder of the test run (e.g Test_001, Test_002) you wish to view. The highest numbered folder is the most recent test
		5.a) The DDD_Summary (where DDD is the test run number) file holds the overall review of the automated tests. It contains the tests that failed and passed for a rapid overview to validate Front End functionality
		5.b) The stdOutput files contain the console output of the Front End during the test case
		5.c) The tsf files contain the TSF output for the test case

RUNNING THE BACK END PROGRAM
The QIES back-end program can be run by completing the following steps:
	1. In a terminal window, navigate to the directory "Tests"
	2. Run the script 5_runBackEnd.py
	3. Once the script is running, follow the prompts provided by the program.
The CSF file used to run the back-end must be named CSF_DDD.txt where DDD is a 3 digit number (i.e. CSF_000.txt) and stored in /BackEnd for the source code and subsequently this script to work. The source code uses a substring method that assumes the CSF file is 7 characters long and follows the format above to extract the file number (see ../sourceCode/BackEnd, CSF.java - line 31). It also uses a substring method that assumes the file path is longer than 7 characters and contains the file directory to output the new VSF (see ../sourceCode/BackEnd, CSF.java - line 197). THIS FILE SHOULD NOT BE MOVED NOR RENAMED. The MTSF file name and location can be changed if the corresponding code (Line 5) in script 5_runBackEnd.py is also changed 


RUNNING THE DAILY SCRIPTS
The automated testing script allows you to test one day's worth of inputs from 4 sessions. The inputs are located in the folder dailyInputs which is itself located in the folder FullSystem. It stores the resulting output files (the TSF for of the each sessions and the MTSF) in the folder 'outputFiles', while the intermediary VSF and CSF are kept in the 'dailyInputs' folder. The standard output contents produced by each input file while being run on the front end is stored in the folder "Extra" which is located in the 'outputFiles' folder. To run the daily script
	1. In a terminal window, Navigate to the directory "Tests"
	2. Run the script 2_runSystemDaily.py
	3. Once the script is running, follow the prompts provided by the program.
For the script to work, the filenames should not be changed and the directories dailyInputs, outputFiles, and outputFiles/Extra MUST exist. 

RUNNING THE WEEKLY SCRIPTS
The automated testing script allows you to test one weeks worth of inputs(5 days). The inputs are located in the folder weeklyInputs which is itself located in the folder FullSystem. It stores the resulting output files (the TSF for of the each sessions and the MTSF) in the folder 'outputFiles', while the intermediary VSF and CSF are kept in the 'weeklyInputs' folder. The standard output contents produced by each input file while being run on the front end is stored in the folder "Extra" which is located in the 'outputFiles' folder. To run the weekly script
	1. In a terminal window, Navigate to the directory "Tests"
	2. Run the script 3_runSystemWeekly.py
	3. Once the script is running, follow the prompts provided by the program. 
For the script to work, the filenames should not be changed and the directories weeklyInputs, outputFiles, and outputFiles/Extra MUST exist. 
