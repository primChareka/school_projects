1. SSH using port 22 into your MS virtual machine with is running HortonWorks Hadoop
	SSH azureSandbox

2. Access web client in a shell using SSH
	ssh root@localhost -p 2222 

3. Make sure you have write privileges for the /user folder
	su hdfs
	hdfs dfs -chmod 777 /user
   	exit
4. Download netIDs data from github
	wget https://raw.githubusercontent.com/primChareka/CMPE432Assignment2/master/SubmissionTemplate/netIDs.data

5. Put netIDs onto HDFS
	hdfs dfs -put netIDs.data /user/maria_dev 

4. Download python code from git hub
	# wget https://raw.githubusercontent.com/primChareka/CMPE432Assignment2/master/SubmissionTemplate/4/sparkRDD.py

5. Execute python script
	spark-submit ./sparkRDD.py 

6. Results will stored in a file called outputDataRDD in the same directory in which the script was executed. Optionally, the results can be stored in the /users/maria_dev/output directory on the HDFS as the unformatted RDD by uncommenting the following line in the code
	 #sortedResults.saveAsTextFile("hdfs:///user/maria_dev/output")