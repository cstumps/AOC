# --- Day 16: Permutation Promenade ---

# You come upon a very unusual sight; a group of programs here appear to be
# dancing.

# There are sixteen programs in total, named a through p. They start by standing
# in a line: a stands in position 0, b stands in position 1, and so on until p,
# which stands in position 15.

# The programs' dance consists of a sequence of dance moves:

#     Spin, written sX, makes X programs move from the end to the front, but
#     maintain their order otherwise. (For example, s3 on abcde produces cdeab).

#     Exchange, written xA/B, makes the programs at positions A and B swap
#     places.

#     Partner, written pA/B, makes the programs named A and B swap places.

# For example, with only five programs standing in a line (abcde), they could do
# the following dance:

#     s1, a spin of size 1: eabcd.
#     x3/4, swapping the last two programs: eabdc.
#     pe/b, swapping programs e and b: baedc.

# After finishing their dance, the programs end up in order baedc.

# You watch the dance for a while and record their dance moves (your puzzle
# input). In what order are the programs standing after their dance?

# --- Part Two ---

# Now that you're starting to get a feel for the dance moves, you turn your
# attention to the dance as a whole.

# Keeping the positions they ended up in from their previous dance, the programs
# perform it again and again: including the first dance, a total of one billion
# (1000000000) times.

# In the example above, their second dance would begin with the order baedc, and
# use the same dance moves:

#     s1, a spin of size 1: cbaed.
#     x3/4, swapping the last two programs: cbade.
#     pe/b, swapping programs e and b: ceadb.

# In what order are the programs standing after their billion dances?

import sys
import string
from collections import deque

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day16-input.txt", "r" ) as f:
        data = f.readline().split( ',' )

    ##
    # Part 1
    ##

    line = deque( [ string.ascii_lowercase[ i ] for i in range( 16 ) ] )

    print( f"Part 1 answer: { ''.join( runDance( line, data ) ) }" )

    ##
    # Part 2
    ##

    # Figure out where it cycles, then we only have to run the remaining cycles
    numIterations = 1000000000 % findCycle( line, data )

    for _ in range( numIterations ):
        line = runDance( line, data )

    print( f"Part 2 answer: { ''.join( line ) }" )


def findCycle( line, moves ):
    found = []
    count = 0

    while True:
        line = runDance( line, moves )

        if ''.join( line ) in found:
            return count
        
        found.append( ''.join( line ) )
        count += 1

def runDance( line, moves ):
    line = line.copy()

    for move in moves:
        if move[ 0 ] == 's':   # Spin
            line.rotate( int( move[ 1: ] ) ) 
        elif move[ 0 ] == 'x': # Exchange
            move = move[ 1: ].split( '/' )
            l = int( move[ 0 ] )
            r = int( move[ 1 ] )

            line[ l ], line[ r ] = line[ r ], line[ l ]
        elif move[ 0 ] == 'p': # Partner
            move = move[ 1: ].split( '/' )
            l = line.index( move[ 0 ] )
            r = line.index( move[ 1 ] )

            line[ l ], line[ r ] = line[ r ], line[ l ]

    return line


if __name__ == "__main__":
    main( argv=sys.argv )