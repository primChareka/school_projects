1) Install sandbox on azure 
	USE SSH and enable port 22
	https://hortonworks.com/tutorial/sandbox-deployment-and-install-guide/section/4/
2) set up ssh via port forwarding as indicated above
3) ssh azureSandbox 
	ssh into sandbox at port 22
4) ssh root@localhost -p 2222  
	shell web client I.e access web from shell 
	https://hortonworks.com/tutorial/manage-files-on-hdfs-via-cli-ambari-files-view/
5) wget https://github.com/primChareka/CMPE432Assignment2/blob/master/Dataset/netIDs.data
   wget https://raw.githubusercontent.com/primChareka/CMPE432Assignment2/master/SubmissionTemplate/testIDs.data
	download our netID's from github 
6) su hdfs
   cd
   hdfs dfs -chmod 777 /user
   exit
	give root access to read and write to the user directory
6) hdfs dfs -mkdir /user/primrose 
	make desired source directory
7) hdfs dfs -mkdir /user/primrose/netIDs 
	make desired source directory one level lower

8) hdfs dfs -put netIDs.data /user/primrose/netIDs 
	move file to right location from current to indicated path

9) hdfs dfs -get /user/primrose/netIDs netIDs.data
	get files from given location and store in current location as specified name

10) on web browser login to amber and navigate to file, click and download 
	https://hortonworks.com/tutorial/loading-and-querying-data-with-hadoop/

https://raw.githubusercontent.com/primChareka/CMPE432Assignment2/master/SubmissionTemplate/4/sparkRDD.py