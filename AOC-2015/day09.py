# --- Day 9: All in a Single Night ---

# Every year, Santa manages to deliver all of his presents in a single night.

# This year, however, he has some new locations to visit; his elves have
# provided him the distances between every pair of locations. He can start and
# end at any two (different) locations he wants, but he must visit each location
# exactly once. What is the shortest distance he can travel to achieve this?

# For example, given the following distances:

# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141

# The possible routes are therefore:

# Dublin -> London -> Belfast = 982
# London -> Dublin -> Belfast = 605
# London -> Belfast -> Dublin = 659
# Dublin -> Belfast -> London = 659
# Belfast -> Dublin -> London = 605
# Belfast -> London -> Dublin = 982

# The shortest of these is London -> Dublin -> Belfast = 605, and so the answer
# is 605 in this example.

# What is the distance of the shortest route?

# --- Part Two ---

# The next year, just to show off, Santa decides to take the route with the
# longest distance instead.

# He can still start and end at any two (different) locations he wants, and he
# still must visit each location exactly once.

# For example, given the distances above, the longest route would be 982 via
# (for example) Dublin -> London -> Belfast.

# What is the distance of the longest route?

import sys
import numpy as np
import itertools as it

def main( argv ):

    data = []

    # Read in input file and add up the sums
    with open( "input/day09-input.txt", "r" ) as f:
        data = f.readlines()

    # Save off destinations
    destList = []

    for line in data:
        line = line.strip().split()

        if line[ 0 ] not in destList:
            destList.append( line[ 0 ] )
        
        if line[ 2 ] not in destList:
            destList.append( line[ 2 ] )

    # Create adjacency matrix
    adjMatrix = np.zeros( (len( destList ), len( destList )), dtype=int )

    for line in data:
        line = line.strip().split()

        src = destList.index( line[ 0 ] )
        dest = destList.index( line[ 2 ] )

        adjMatrix[ src, dest ] = int( line[ 4 ] )
        adjMatrix[ dest, src ] = int( line[ 4 ] )

    # Compute all path lengths
    pathLengths = []

    for path in it.permutations( range( len( destList ) ) ):
        pathLengths.append( [ path, computePath( path, adjMatrix ) ] )

    # Sort the list
    allPaths = sorted( pathLengths, key=lambda x:x[ 1 ] )

    ##
    # Part 1
    ##

    print( f"Part 1 answer: {allPaths[ 0 ][ 1 ]}" )

    ##
    # Part 2
    ##

    print( f"Part 2 answer: {allPaths[ -1 ][ 1 ]}" )


def computePath( path, adj ):
    dist = 0

    for i in range( 0, len( path ) - 1 ):  
        dist += adj[ path[ i ], path[ i + 1 ] ]

    return dist


if __name__ == "__main__":
    main( argv=sys.argv )
