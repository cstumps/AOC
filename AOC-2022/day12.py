# --- Day 12: Hill Climbing Algorithm ---
 
# You try contacting the Elves using your handheld device, but the river you're
# following must be too low to get a decent signal.
 
# You ask the device for a heightmap of the surrounding area (your puzzle
# input). The heightmap shows the local area from above broken into a grid; the
# elevation of each square of the grid is given by a single lowercase letter,
# where a is the lowest elevation, b is the next-lowest, and so on up to the
# highest elevation, z.
 
# Also included on the heightmap are marks for your current position (S) and the
# location that should get the best signal (E). Your current position (S) has
# elevation a, and the location that should get the best signal (E) has
# elevation z.
 
# You'd like to reach E, but to save energy, you should do it in as few steps as
# possible. During each step, you can move exactly one square up, down, left, or
# right. To avoid needing to get out your climbing gear, the elevation of the
# destination square can be at most one higher than the elevation of your
# current square; that is, if your current elevation is m, you could step to
# elevation n, but not to elevation o. (This also means that the elevation of
# the destination square can be much lower than the elevation of your current
# square.)
 
# For example:
 
# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi
 
# Here, you start in the top-left corner; your goal is near the middle. You
# could start by moving down or right, but eventually you'll need to head toward
# the e at the bottom. From there, you can spiral around to the goal:
 
# v..v<<<<
# >v.vv<<^
# .>vv>E^^
# ..v>>>^^
# ..>>>>>^
 
# In the above diagram, the symbols indicate whether the path exits each square
# moving up (^), down (v), left (<), or right (>). The location that should get
# the best signal is still E, and . marks unvisited squares.
 
# This path reaches the goal in 31 steps, the fewest possible.
 
# What is the fewest steps required to move from your current position to the
# location that should get the best signal?

# --- Part Two ---

# As you walk up the hill, you suspect that the Elves will want to turn this
# into a hiking trail. The beginning isn't very scenic, though; perhaps you can
# find a better starting point.

# To maximize exercise while hiking, the trail should start as low as possible:
# elevation a. The goal is still the square marked E. However, the trail should
# still be direct, taking the fewest steps to reach its goal. So, you'll need to
# find the shortest path from any square at elevation a to the square marked E.

# Again consider the example from above:

# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi

# Now, there are six choices for starting position (five marked a, plus the
# square marked S that counts as being at elevation a). If you start at the
# bottom-left square, you can reach the goal most quickly:

# ...v<<<<
# ...vv<<^
# ...v>E^^
# .>v>>>^^
# >^>>>>>^

# This path reaches the goal in only 29 steps, the fewest possible.

# What is the fewest steps required to move starting from any square with
# elevation a to the location that should get the best signal?

# My implementation of Dijkstra's algorithm here kind of sucks.  I suspect there is a much
# cleaner way to do this, however mine does actually work (though it chugs).  It returns
# None when it cannot find a route to the goal with the given rules (no step up greater than
# 1).

import sys
from string import ascii_lowercase
from queue import PriorityQueue
 
def main( argv ):
 
    # Read in input file
    with open( "input/day12-input.txt", "r" ) as f:
        data = list( f.readlines() )
   
    #data = [ 'Sabqponm',
    #         'abcryxxl',
    #         'accszExk',
    #         'acctuvwj',
    #         'abdefghi' ]
 
    data = [ list( line.strip() ) for line in data ]
 
    for j in range( len( data ) ):
        for i in range( len( data[ 0 ] ) ):
            if data[ j ][ i ] == 'S':
                start = [ i, j ]
                data[ j ][ i ] = 0
 
            elif data[ j ][ i ] == 'E':
                end = [ i, j ]
                data[ j ][ i ] = 25
 
            else:
                data[ j ][ i ] = ascii_lowercase.index( data[ j ][ i ] )   
 
    ##
    # Part 1
    ##
 
    d = dijkstra( data, start, end )
 
    print( f"Part 1 answer: {d}" )
 
    ##
    # Part 2
    ##

    startCoords = [ [x, y] for y in range( len( data ) ) for x in range( len( data[ 0 ] ) ) if data[ y ][ x ] == 0 ]
    dist = []

    for start in startCoords:
        d = dijkstra( data, start, end )

        if d != None: # Found a path to end
            dist.append( d )

    dist.sort()

    print( f"Part 2 answer: {dist[ 0 ]}" )
 
def dijkstra( data, start, end ):
    mx = len( data[ 0 ] )
    my = len( data )

    visited =  [ [0 for i in range( mx )] for j in range( my ) ]
    q = PriorityQueue()

    q.put( (0, start) ) # Add starting node

    while not q.empty():
        p, coord = q.get()
        x, y = coord

        if visited[ y ][ x ]:
            continue

        visited[ y ][ x ] = 1

        if coord == end:
            return p

        for (dx, dy) in [ (-1, 0), (1, 0), (0, -1), (0, 1) ]:
            if ( (x + dx < 0) or (x + dx >= mx) or                  # X bounds
                 (y + dy < 0) or (y + dy >= my) or                  # Y bounds
                 (data[ y + dy ][ x + dx ] - data[ y ][ x ] > 1) ): # Max step up of 1
                continue

            q.put( (p+1, [x + dx, y + dy]) )

    return None # No route to goal


if __name__ == "__main__":
    main( argv=sys.argv )