The MongoDB code assumes you have the pymongo driver. It can be run with `python dataset1-mongodb-creation.py`. It connects to a local instance of MongoDB that needs to be started in advance with `mongod` run in another shell, meaning MongoDB needs to be installed.

The Cassandra code assumes you have Cassandra, the Cassandra-driver (which allows you to use python and can be installed using pip with the instructions found here https://github.com/datastax/python-driver) and python 3 installed on your computer. All programs are written in MacOS but should be compatible with windows (just make sure file paths are listed correctly!)

	Step 1: Launch Cassandra in your terminal (cassandra -f) *When you cassandra is running you will not be able to enter commands in this terminal

	Step 2: In a new terminal window not running cassandra, navigate to the the location of this file and then execute the python script (python setupCassandraDB.py

******************************* VIEWING DATA*******************************
To view the data that was loaded into the database:	

	Step 1: Log into the cassandra query language by typing in (cqlsh) in the terminal. If everything is working properly you should see something like:

		Connected to Test Cluster at 127.0.0.1.
		[cqlsh 5.0.1 | Cassandra 3.11.3 | CQL spec 3.4.4 | Native protocol v4]
		Use HELP for help.

	Step 2: Enter the following CQL commands hitting enter after each step
 		USE movRatings;
		SELECT uid, numItems(ratedMovies) from uidratedmovies;
		SELECT iid, avgRating(numRating, totRating)) from avgRating;

	
	


The Neo4j code assumes you have the py2neo 4.0.8 driver. It connects to an Azure Virtual Machine, that is no longer deployed, that had Neo4j installed. It can be run with `python dataset1-neo4j-creation.py`.