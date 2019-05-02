from py2neo import Graph, Node, Relationship, NodeMatcher
import time

uri = "http://40.121.20.57:7474/db/data" # note this database is no longer active in Azure, to save cost
graph = Graph(uri, password="Neo4jPassword")
print(len(graph.nodes))
graph.delete_all() # clear graph
matcher=NodeMatcher(graph)
tx=graph.begin()

# create genre nodes
print("inserting genres")
tx.create(Node("genre",type="unknown"))
tx.create(Node("genre",type="action"))
tx.create(Node("genre",type="unknown"))
tx.create(Node("genre",type="adventure"))
tx.create(Node("genre",type="animation"))
tx.create(Node("genre",type="childrens"))
tx.create(Node("genre",type="comedy"))
tx.create(Node("genre",type="crime"))
tx.create(Node("genre",type="documentary"))
tx.create(Node("genre",type="drama"))
tx.create(Node("genre",type="fantasy"))
tx.create(Node("genre",type="filmnoir"))
tx.create(Node("genre",type="horror"))
tx.create(Node("genre",type="musical"))
tx.create(Node("genre",type="mystery"))
tx.create(Node("genre",type="romance"))
tx.create(Node("genre",type="scifi"))
tx.create(Node("genre",type="thriller"))
tx.create(Node("genre",type="war"))
tx.create(Node("genre",type="western"))
tx.commit()
tx = graph.begin()

print("insert movies")
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

        newMovie=Node("movie",id=int(movieId),title=movieTitle,releaseDate=releaseDate,videoReleaseDate=videoReleaseDate,imdburl=imdbUrl)
        tx.create(newMovie)
        create relationships between new movie node and the genres nodes for the genres movie is in
        for genre in genres:
            existingGenreNode = matcher.match("genre",type=genre).first()
            rel=Relationship(newMovie,"ISOF",existingGenreNode)
            tx.create(rel)

print("done insert movies, time to insert in seconds was")
end=time.time()
print(end - start)
tx.commit()

print("start ratings")
counter=0 # counter used to see what line at in file, in case crash while inserting
start = time.time()
with open('./Dataset/dataset1/netIDs.data', 'r') as file:
    for row in file:
        counter=counter+1
        if (counter>59775): # only start inserting into database with new rows
            tx=graph.begin()
            # create node for each value, with appropriate relationships
            userId, itemId, rating, timestamp = row.split()
            newUser = Node("user", id=int(userId))
            newRating = Node("rating",value=int(rating), time=int(timestamp))
            tx.create(newUser)
            tx.create(newRating)
            tx.create(Relationship(newUser,"GAVE",newRating))
            tx.commit()
            tx=graph.begin()
            # create relationship between already made movie node and this user, and the rating and the movie
            existingMovie = matcher.match("movie",id=int(itemId)).first()
            rated=Relationship(newUser,"RATED",existingMovie)
            tx.create(rated)
            rates=Relationship(newRating,"RATES",existingMovie)
            tx.create(rates)
            tx.commit()
            print(counter) # visually see what line at, so if statement can be adjusted when crash

end = time.time()
print("done insert ratings, time to insert in seconds was")
print(end - start)
tx.commit()
print(len(graph.nodes))