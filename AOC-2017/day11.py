# --- Day 11: Hex Ed ---

# Crossing the bridge, you've barely reached the other side of the stream when a
# program comes up to you, clearly in distress. "It's my child process," she
# says, "he's gotten lost in an infinite grid!"

# Fortunately for her, you have plenty of experience with infinite grids.

# Unfortunately for you, it's a hex grid.

# The hexagons ("hexes") in this grid are aligned such that adjacent hexes can
# be found to the north, northeast, southeast, south, southwest, and northwest:

#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \

# You have the path the child process took. Starting where he started, you need
# to determine the fewest number of steps required to reach him. (A "step" means
# to move from the hex you are in to any adjacent hex.)

# For example:

#     ne,ne,ne is 3 steps away.
#     ne,ne,sw,sw is 0 steps away (back where you started).
#     ne,ne,s,s is 2 steps away (se,se).
#     se,sw,se,sw,sw is 3 steps away (s,s,sw).

# --- Part Two ---

# How many steps away is the furthest he ever got from his starting position

import sys

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day11-input.txt", "r" ) as f:
        data = f.readline().strip().split( ',' )

    #data = [ 'ne', 'ne', 'ne' ]              # is 3 steps away.
    #data = [ 'ne', 'ne', 'sw', 'sw' ]        # is 0 steps away (back where you started).
    #data = [ 'ne', 'ne', 's', 's' ]          # is 2 steps away (se,se).
    #data = [ 'se', 'sw', 'se', 'sw', 'sw' ]  # is 3 steps away (s,s,sw).

    child = Hex( 0, 0, 0 )
    maxDist = 0

    for dir in data:
        child.go( dir )
        maxDist = max( maxDist, child.distance() )

    ##
    # Part 1
    ##

    print( f"Part 1 answer: { child.distance() }" )

    ##
    # Part 2
    ##

    print( f"Part 2 answer: { maxDist }" )

class Hex( object ):
    def __init__( self, q, r, s ):
        self.q = q
        self.r = r
        self.s = s

    def go( self, dir ):
        # An alternative way to do this is to have unit objects in a look up table and 
        # rely on the addition operator.
        if dir == 'se':
            self.s -= 1
            self.q += 1
        elif dir == 'sw':
            self.r += 1
            self.q -= 1
        elif dir == 'nw':
            self.s += 1
            self.q -= 1
        elif dir == 'ne':
            self.r -= 1
            self.q += 1
        elif dir == 'n':
            self.s += 1
            self.r -= 1
        elif dir == 's':
            self.s -= 1
            self.r += 1

    def distance( self ):
        return int( (abs( self.q ) + abs( self.r ) + abs( self.s )) / 2 )


if __name__ == "__main__":
    main( argv=sys.argv )