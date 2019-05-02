1. SSH into shell web client which allows web access from the shell 
	ssh root@localhost -p 2222  

2.Download NetID's File from GitHub onto the local filesystem
	wget https://raw.githubusercontent.com/primChareka/CMPE432Assignment2/master/SubmissionTemplate/netIDs.data

3. Make a directory for the input data on the HDFS using the filesystem shell
	hdfs dfs -mkdir /user/maria_dev/inputData

4. Transfer files to the destination folder on the HDFS
	hdfs dfs -put netIDs.data /user/maria_dev/inputData
