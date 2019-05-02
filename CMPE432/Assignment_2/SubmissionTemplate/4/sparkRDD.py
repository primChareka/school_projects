from pyspark import SparkConf, SparkContext
from datetime import datetime
# This  spark map-reduce script  counts the number of reviews per each movie
def readInputFile(line):
    #line = [userID, itemID,movieRating,timestamp]
    data = line.split("\t")

    #Return key value pair with item ID as key and value as a list
    return (int(data[1]),[int(data[2]),1.0])

def avg(x):
    #return average and number of reviews in a list
    return [round((x[0]/x[1]),1),x[1]]

if __name__ == "__main__":
    startTime = datetime.now()
    #Create SparkContext
    conf = SparkConf().setAppName("CMPE432Spark")
    sc = SparkContext(conf = conf)

    # RDD fileLines: read data from HDFS returns list of filelines
    fileLines = sc.textFile("hdfs:///user/maria_dev/netIDs.data")
    movieRatings = fileLines.map(readInputFile)

    #Returns [key-itemID, vlaue-[sumOfReviews, numberOfReviews]    
    sumRatings = movieRatings.reduceByKey(lambda movie1, movie2: [movie1[0] + movie2[0],movie1[1]+movie2[1]])

    #Returns [key-itemID, vlaue-[avgOfReviews, numberOfReviews]  
    avgRatings = sumRatings.mapValues(avg)

    #Returns output sorted in Ascending Order
    sortedResults = avgRatings.sortBy(lambda avgReview: avgReview[1][0])
    
    #OPTIONAL, Uncomment this line to store the finalRDD on Hadoop File System
    #sortedResults.saveAsTextFile("hdfs:///user/maria_dev/output")

    #Store Results in a text file on the local machine
    records = sortedResults.take(20)
    file = open("outputData.txt","w")
    file.write("     MovieId\tAverage Rating\tNumber of Reviews\n")
    for line in records:
        file.write("-\t"+str(line[0])+"\t\t"+str(line[1][0])+"\t\t"+str(line[1][1])+"\n")

    file.write(str(datetime.now() - startTime))
    file.close()

