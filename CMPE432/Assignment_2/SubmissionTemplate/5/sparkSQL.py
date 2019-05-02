from datetime import datetime
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions

def readInputFile(line):
    data = line.split("\t")
        ## First field key
    return Row(movieId=int(data[1]),rating=int(data[2]))

if __name__ == "__main__":
    startTime = datetime.now()
    #Create SparkContext
    sc2 = SparkSession.builder.appName("Cisc432Spark_SQL").getOrCreate()

    # RDD fileLines: read data from HDFS returns list of filelines
    lines = sc2.sparkContext.textFile("hdfs:///user/maria_dev/netIDs.data")

    # RDD  movieRatings : Convert to (itemId) rows
    ratings = lines.map(readInputFile)

    # convert moveRatings RDD to a dataFrame
    moviesDataFrame = sc2.createDataFrame(ratings)

    counts = moviesDataFrame.groupBy("movieID").agg(functions.mean('rating').alias("avgRating"),functions.count('rating').alias("numRatings"))
    resultSchema = counts.orderBy("avgRating").take(20)
 
    file = open("outputData.txt","w")
    file.write("     MovieId\tAverage Rating\tNumber of Reviews\n")
    for row in resultSchema:
        file.write("-\t" + str(row.movieID)+"\t\t" + str(row.avgRating) + "\t\t" + str(row.numRatings)+"\n")

    file.write(str(datetime.now() - startTime))
    file.close()
