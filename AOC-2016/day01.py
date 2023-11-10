# --- Day 1: No Time for a Taxicab ---

# Santa's sleigh uses a very high-precision clock to guide its movements, and
# the clock's oscillator is regulated by stars. Unfortunately, the stars have
# been stolen... by the Easter Bunny. To save Christmas, Santa needs you to
# retrieve all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each
# day in the Advent calendar; the second puzzle is unlocked when you complete
# the first. Each puzzle grants one star. Good luck!

# You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near",
# unfortunately, is as close as you can get - the instructions on the Easter
# Bunny Recruiting Document the Elves intercepted start here, and nobody had
# time to work them out further.

# The Document indicates that you should start at the given coordinates (where
# you just landed) and face North. Then, follow the provided sequence: either
# turn left (L) or right (R) 90 degrees, then walk forward the given number of
# blocks, ending at a new intersection.

# There's no time to follow such ridiculous instructions on foot, though, so you
# take a moment and work out the destination. Given that you can only walk on
# the street grid of the city, how far is the shortest path to the destination?

# For example:

#     Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
#     R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
#     R5, L5, R5, R3 leaves you 12 blocks away.

# How many blocks away is Easter Bunny HQ?

# --- Part Two ---

# Then, you notice the instructions continue on the back of the Recruiting
# Document. Easter Bunny HQ is actually at the first location you visit twice.

# For example, if your instructions are R8, R4, R4, R8, the first location you
# visit twice is 4 blocks away, due East.

# How many blocks away is the first location you visit twice?

import sys

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day01-input.txt", "r" ) as f:
        data = [ x.strip() for x in f.readline().split( ',' ) ]

    ##
    # Part 1
    ##

    # Perform the moves (turtle graphics!), find the manhattan distance.

    turtle = Turtle()

    for move in data:
        turtle.turn( move[ 0 ] )
        turtle.move( int( move[ 1: ] ) )
    
    print( f"Part 1 answer: {abs( turtle.x + turtle.y )}" )

    ##
    # Part 2
    ##

    turtle.reset()

    for move in data:
        turtle.turn( move[ 0 ] )
        if turtle.move( int( move[ 1: ] ), True ):
            break

    print( f"Part 2 answer: {abs( turtle.x + turtle.y )}" )


class Turtle:
    def __init__( self ):
        self.reset()

    def reset( self ):
        self.x = 0
        self.y = 0
        self.dir = 0
        self.visited = []

    def turn( self, dir ):
        if dir == 'L':
            self.dir = (self.dir - 1) % 4
        else:
            self.dir = (self.dir + 1) % 4

    def move( self, dist, track=False ):
        if self.dir == 0:
            op = 'self.y += 1'
        elif self.dir == 2:
            op = 'self.y -= 1'
        elif self.dir == 1:
            op = 'self.x -= 1'
        else:
            op = 'self.x += 1'

        for _ in range( dist ):
            exec( op )

            if track:
                if [ self.x, self.y ] not in self.visited:
                    self.visited.append( [ self.x, self.y ] )
                else:
                    break
        else:
            return False # Did not visit a known spot
        
        return True # We broke out because we visited a place twice


if __name__ == "__main__":
    main( argv=sys.argv )
