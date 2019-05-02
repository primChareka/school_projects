1. Download python code from Github
	a) wget https://raw.githubusercontent.com/primChareka/CMPE432Assignment2/master/SubmissionTemplate/3/mapper.py
    b) wget https://raw.githubuser.content.com/primChareka/CMPE432Assignment2/master/SubmissionTemplate/3/reducer.py

2. Allow execution of those files
    a) chmod 777 mapper.py
    b) chmod 777 reducer.py

3. Run mapreduce
    a) /usr/bin/hadoop jar /usr/hdp/2.6.4.0-91/hadoop-mapreduce/hadoop-streaming.jar -file ./mapper.py -mapper ./mapper.py -file ./reducer.py -reducer ./reducer.py -input /user/maria_dev/inputData/netIDs.data -output /user/maria_dev/mapreduce_output

4. Move results story in temp folder in HDFS to sandbox filesystem
	hdfs dfs -get /user/maria_dev/mapreduce_output

5. Copy from sandbox down to vm
	scp ./mapreduce/* primchareka@168.61.147.132:./results

7. copy from azure vm down local
	scp -r primchareka@168.61.147.132:/home/primchareka/results ./