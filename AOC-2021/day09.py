# --- Day 9: Smoke Basin ---

# These caves seem to be lava tubes. Parts are even still volcanically active;
# small hydrothermal vents release smoke into the caves that slowly settles like
# rain.

# If you can model how the smoke flows through the caves, you might be able to
# avoid it and be that much safer. The submarine generates a heightmap of the
# floor of the nearby caves for you (your puzzle input).

# Smoke flows to the lowest point of the area it's in. For example, consider the
# following heightmap:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# Each number corresponds to the height of a particular location, where 9 is the
# highest and 0 is the lowest a location can be.

# Your first goal is to find the low points - the locations that are lower than
# any of its adjacent locations. Most locations have four adjacent locations
# (up, down, left, and right); locations on the edge or corner of the map have
# three or two adjacent locations, respectively. (Diagonal locations do not
# count as adjacent.)

# In the above example, there are four low points, all highlighted: two are in
# the first row (a 1 and a 0), one is in the third row (a 5), and one is in the
# bottom row (also a 5). All other locations on the heightmap have some lower
# adjacent location, and so are not low points.

# The risk level of a low point is 1 plus its height. In the above example, the
# risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels
# of all low points in the heightmap is therefore 15.

# Find all of the low points on your heightmap. What is the sum of the risk
# levels of all low points on your heightmap?

# --- Part Two ---

# Next, you need to find the largest basins so you know what areas are most
# important to avoid.

# A basin is all locations that eventually flow downward to a single low point.
# Therefore, every low point has a basin, although some basins are very small.
# Locations of height 9 do not count as being in any basin, and all other
# locations will always be part of exactly one basin.

# The size of a basin is the number of locations within the basin, including the
# low point. The example above has four basins.

# The top-left basin, size 3:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# The top-right basin, size 9:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# The middle basin, size 14:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# The bottom-right basin, size 9:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# Find the three largest basins and multiply their sizes together. In the above
# example, this is 9 * 14 * 9 = 1134.

# What do you get if you multiply together the sizes of the three largest
# basins?

import sys
import queue

mapInt  = lambda x : int( x )
mapChar = lambda x : '.' if x == -1 else 'X'

def main( argv ):

    # Read in input file
    with open( "input/day09-input.txt", "r" ) as f:
        data = f.readlines()

    #data = [ '2199943210','3987894921','9856789892','8767896789','9899965678' ]
    data = [ list( map( mapInt, line.strip() ) ) for line in data ]

    ##
    # Part 1
    ##

    score = 0

    for i in range( len( data ) ):
        for j in range( len( data[ i ] ) ):
            if not i:
                up = 99
            else:
                up = data[ i-1 ][ j ]
            
            if i == len( data ) - 1:
                down = 99
            else:
                down = data[ i+1 ][ j ]

            if not j:
                left = 99
            else:
                left = data[ i ][ j-1 ]

            if j == len( data[ i ] ) - 1:
                right = 99
            else:    
                right = data[ i ][ j+1 ]

            if ( data[ i ][ j ] < up and data[ i ][ j ] < down and
                 data[ i ][ j ] < left and data[ i ][ j ] < right ):
                 score += (data[ i ][ j ] + 1)

    print( "Part 1 answer: %s" % score )

    ##
    # Part 2
    ##

    sizes = []

    for i in range( len( data ) ):
        for j in range( len( data[ i ] ) ):
            # New region to fill
            if data[ i ][ j ] != 9 and data[ i ][ j ] >= 0:
                sizes.append( fillRegion( j, i, data ) )

    sizes = sorted( sizes, reverse=True )

    print( "Part 2 answer: %s" % (sizes[ 0 ] * sizes[ 1 ] * sizes[ 2 ]) )


def fillRegion( x, y, data ):
    q = queue.Queue()
    count = 0

    # Add the initial point to our queue
    q.put( (x, y) )

    while not q.empty():
        coord = q.get()

        y = coord[ 1 ]
        x = coord[ 0 ]

        # Border point or a point we've already filled
        if data[ y ][ x ] == 9 or data[ y ][ x ] == -1:
            continue

        # Otherwise, set the current loc and add other directions excluding up
        data[ y ][ x ] = -1
        count += 1
        
        # Down
        if y < len( data ) - 1:
            q.put( (x, y+1) )

        # Right
        if x < len( data[ y ] ) - 1:
            q.put( (x+1, y) )

        # Left
        if x > 0:
            q.put( (x-1, y) )

        if y > 0:
            q.put( (x, y-1) )

    return count

def printData( data ):
    for row in data:
        print( ''.join( map( mapChar, row ) ) )

    print( '\n' )

if __name__ == "__main__":
    main( argv=sys.argv )