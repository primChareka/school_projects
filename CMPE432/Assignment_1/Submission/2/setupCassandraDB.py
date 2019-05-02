#this script has all of the necessary statments to set up the test database
import os
from cassandra.cluster import Cluster

#Connect to cassandra cluster
cluster = Cluster()
session = cluster.connect()
session.execute("CREATE KEYSPACE movRatings WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '3'}")
session.execute("use movRatings")
session.execute("CREATE FUNCTION avgRating ( num_rating counter, tot_rating counter ) RETURNS NULL ON NULL INPUT RETURNS float LANGUAGE java AS $$ return (float)tot_rating/(float)num_rating; $$;")
session.execute("CREATE FUNCTION numItems(my_list List<int>) RETURNS NULL ON NULL INPUT RETURNS int LANGUAGE java AS $$ return my_list.size(); $$;")
session.execute("CREATE TABLE ratings(uid int ,iid int,rating int,tstamp int, primary key(uid,iid)) WITH CLUSTERING ORDER BY(iid ASC)")
session.execute("CREATE TABLE uidratedMovies(uid int Primary Key, ratedMovies List<int>)")
session.execute("CREATE TABLE avgRatings(iid int Primary Key,numRatings counter, totRating counter)")

#for each line in the data file, split it into its components and then insert it into the master rating entry table
with open("random_data/netIDs.data", "r") as source:
    for line in source:
        #process entry line from file
        entry = line.strip()
        entry = entry.split('\t')

        #get variable values each line is of the form {userId|itemId|ratingValue|timestamp}
        uidCur = entry[0]
        iidCur = entry[1]
        ratingCur = entry[2]
        tstampCur = entry[3]

        session.execute("INSERT INTO ratings (uid,iid,rating,tstamp) VALUES (%s,%s,%s,%s)", [int(uidCur), int(iidCur), int(ratingCur), int(tstampCur)])
        session.execute("UPDATE uidRatedMovies SET ratedMovies = ratedMovies + %s where uid =%s", [[int(iidCur)],int(uidCur)])
        session.execute("UPDATE avgRatings SET numRatings = numRatings +1, totRating = totRating +%s where iid =%s ",[int(ratingCur),int(iidCur)])

