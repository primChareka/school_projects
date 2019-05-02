#!/usr/bin/env python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
        userId, itemId, rating, timestamp = line.split() #pull out relevant information from each row
        # write the results to STDOUT (standard output), which is the input for the reducer
        # write the movie ID, the rating for that movie and the trivial count of 1
        # hadoop will sort the output by movie ID
        print '%s\t%s\t1' % (itemId, rating) # format for reducer
