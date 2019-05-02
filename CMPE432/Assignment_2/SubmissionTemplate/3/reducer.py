#!/usr/bin/env python
import sys, json

movieDataList=[]
currentId = None
currentRatingCount = 0
currentRatingSum = 0

# input comes from STDIN
for line in sys.stdin:
    # parse the input we got from mapper.py
    movieId, rating, count = line.split()
    movieId = int(movieId)
    rating = float(rating)
    count = int(count)
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if currentId == movieId:
        currentRatingCount += count
        currentRatingSum += rating
    else:
        if currentId:
            # add to sorted list of average 
            movieDataList.append({"id": currentId, "average_rating": currentRatingSum/currentRatingCount, "numReviews": currentRatingCount})
        currentRatingCount = count
        currentRatingSum = rating
        currentId = movieId
if currentId:
            # add to sorted list of average 
            movieDataList.append({"id": currentId, "average_rating": currentRatingSum/currentRatingCount, "numReviews": currentRatingCount})
# sort and output to STDOUT
movieDataList.sort(key=lambda x: (x["average_rating"], x["id"]))
for data in movieDataList[:20]: # loops through first 20 movies (highest 20 average ratings)
    print(data["id"],data["average_rating"],data["numReviews"])