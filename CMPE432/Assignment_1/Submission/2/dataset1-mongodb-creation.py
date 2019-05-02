from pymongo import MongoClient
import time
# from collections import OrderedDict
# import sys

# connect to azure mongodb instance
client = MongoClient("localhost",27017)  # supply connection args as appropriate

# create/retrieve database
db = client.dataset1

# clear old collections
db.ratings.drop()
db.movies.drop()

# create collections
ratingsCollection = db.ratings
moviesCollection = db.movies

ratings = []
print("start ratings")
start = time.time()
with open('./Dataset/dataset1/netIDs.data', 'r') as file:
    for row in file:
        # create one document for mongodb with one row's values
        userId, itemId, rating, timestamp = row.split()
        oneRating = {"userId": int(userId), "itemId": int(itemId), "rating": int(rating), "timestamp": int(timestamp)}
        ratings.append(oneRating)
print("insert ratings")
# bulk insert all values at once - faster than inserting individually
ratingsCollection.insert(ratings)
end = time.time()
print("done insert ratings, time to insert in seconds was")
print(end - start)

movies = []
start = time.time()
with open('./Dataset/dataset1/movies.dat', 'r') as file:
    for row in file:
        # retrieve row values, based of '|' delimiter
        movieId, movieTitle, releaseDate, videoReleaseDate, imdbUrl, unknown, action, adventure, animation, childrens, \
        comedy, crime, documentary, drama, fantasy, filmnoir, horror, musical, mystery, romance, scifi, thriller, war, \
        western = row.split("|")

        # create array of genre names, not 1/0 value
        genres = []
        if int(unknown) == 1: genres.append("unknown")
        if int(action) == 1: genres.append("action")
        if int(adventure) == 1: genres.append("adventure")
        if int(animation) == 1: genres.append("animation")
        if int(childrens) == 1: genres.append("childrens")
        if int(comedy) == 1: genres.append("comedy")
        if int(crime) == 1: genres.append("crime")
        if int(documentary) == 1: genres.append("documentary")
        if int(drama) == 1: genres.append("drama")
        if int(fantasy) == 1: genres.append("fantasy")
        if int(filmnoir) == 1: genres.append("filmnoir")
        if int(horror) == 1: genres.append("horror")
        if int(musical) == 1: genres.append("musical")
        if int(mystery) == 1: genres.append("mystery")
        if int(romance) == 1: genres.append("romance")
        if int(scifi) == 1: genres.append("scifi")
        if int(thriller) == 1: genres.append("thriller")
        if int(war) == 1: genres.append("war")
        if int(western) == 1: genres.append("western")

        oneMovie = {"movieId": int(movieId), "movieTitle": movieTitle, "releaseDate": releaseDate,
                    "videoReleaseDate": videoReleaseDate, "IMDbURL": imdbUrl, "genres": genres}
        movies.append(oneMovie)

print("insert movies")
# bulk insert movie documents
moviesCollection.insert(movies)
end = time.time()
print("done insert movies, time to insert in seconds was")
print(end - start)
client.close()