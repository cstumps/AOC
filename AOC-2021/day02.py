# --- Day 2: Dive! ---

# Now, you need to figure out how to pilot this thing.

# It seems like the submarine can take a series of commands like forward 1, down
# 2, or up 3:

#     forward X increases the horizontal position by X units.
#     down X increases the depth by X units.
#     up X decreases the depth by X units.

# Note that since you're on a submarine, down and up affect your depth, and so
# they have the opposite result of what you might expect.

# The submarine seems to already have a planned course (your puzzle input). You
# should probably figure out where it's going. For example:

# forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2

# Your horizontal position and depth both start at 0. The steps above would then
# modify them as follows:

#     forward 5 adds 5 to your horizontal position, a total of 5.
#     down 5 adds 5 to your depth, resulting in a value of 5.
#     forward 8 adds 8 to your horizontal position, a total of 13.
#     up 3 decreases your depth by 3, resulting in a value of 2.
#     down 8 adds 8 to your depth, resulting in a value of 10.
#     forward 2 adds 2 to your horizontal position, a total of 15.

# After following these instructions, you would have a horizontal position of 15
# and a depth of 10. (Multiplying these together produces 150.)

# Calculate the horizontal position and depth you would have after following the
# planned course. What do you get if you multiply your final horizontal position
# by your final depth?

import sys

def main( argv ):
    # Read in input file
    with open( "input/day02-input.txt", "r" ) as f:
        data = [ [ l.split()[0], int( l.split()[1] ) ] for l in f ]

    ##
    # Part 1
    ##

    s = Submarine()

    for dir in data:
        s.move( dir[ 0 ], dir[ 1 ] )

    print( "Part 1 answer: %s" % (s.h * s.d) )

    ##
    # Part 2
    ##

    s = Submarine()

    for dir in data:
        s.move2( dir[ 0 ], dir[ 1 ] )

    print( "Part 2 answer: %s" % (s.h * s.d) )


class MyError( Exception ):
    def __init__( self, value ):
        self.value = value

    def __str__( self ):
        return repr( self.value )

class Submarine( object ):
    def __init__( self ):
        self.h = 0
        self.d = 0
        self.aim = 0

    # Part 1 move
    def move( self, dir, dist ):
        if dir == 'forward':
            self.h += dist
        elif dir == 'up':
            self.d -= dist
        elif dir == 'down':
            self.d += dist
        else:
            raise( "Invalid direction requested: %s" % dir )

    # Part 2 move
    def move2( self, dir, dist ):
        if dir == 'forward':
            self.h += dist
            self.d += (self.aim * dist)
        elif dir == 'up':
            self.aim -= dist
        elif dir == 'down':
            self.aim += dist
        else:
            raise( "Invalid direction requested: %s" % dir )            


if __name__ == "__main__":
    main( argv=sys.argv )