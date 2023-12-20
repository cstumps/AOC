# --- Day 3: No Matter How You Slice It ---

# The Elves managed to locate the chimney-squeeze prototype fabric for Santa's
# suit (thanks to someone who helpfully wrote its box IDs on the wall of the
# warehouse in the middle of the night). Unfortunately, anomalies are still
# affecting them - nobody can even agree on how to cut the fabric.

# The whole piece of fabric they're working on is a very large square - at least
# 1000 inches on each side.

# Each Elf has made a claim about which area of fabric would be ideal for
# Santa's suit. All claims have an ID and consist of a single rectangle with
# edges parallel to the edges of the fabric. Each claim's rectangle is defined
# as follows:

#     The number of inches between the left edge of the fabric and the left edge
#     of the rectangle.

#     The number of inches between the top edge of the fabric and the top edge
#     of the rectangle.

#     The width of the rectangle in inches.

#     The height of the rectangle in inches.

# A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3
# inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4
# inches tall. Visually, it claims the square inches of fabric represented by #
# (and ignores the square inches of fabric represented by .) in the diagram
# below:

# ...........
# ...........
# ...#####...
# ...#####...
# ...#####...
# ...#####...
# ...........
# ...........
# ...........

# The problem is that many of the claims overlap, causing two or more claims to
# cover part of the same areas. For example, consider the following claims:

# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2

# Visually, these claim the following areas:

# ........
# ...2222.
# ...2222.
# .11XX22.
# .11XX22.
# .111133.
# .111133.
# ........

# The four square inches marked with X are claimed by both 1 and 2. (Claim 3,
# while adjacent to the others, does not overlap either of them.)

# If the Elves all proceed with their own plans, none of them will have enough
# fabric. How many square inches of fabric are within two or more claims?

# --- Part Two ---

# Amidst the chaos, you notice that exactly one claim doesn't overlap by even a
# single square inch of fabric with any other claim. If you can somehow draw
# attention to it, maybe the Elves will be able to make Santa's suit after all!

# For example, in the claims above, only claim 3 is intact after all claims are
# made.

# What is the ID of the only claim that doesn't overlap?

import sys
import numpy as np
from itertools import combinations

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day03-input.txt", "r" ) as f:
        data = [ line.rstrip( '\n' ) for line in f ]

    #data = [ '#1 @ 1,3: 4x4',
    #         '#2 @ 3,1: 4x4',
    #         '#3 @ 5,5: 2x2' ]

    rects = []

    for line in data:
        i, _, pos, size = line.split()
        rects.append( Rect( int( i[ 1: ] ), *map( int, pos[ :-1 ].split( ',' ) ), *map( int, size.split( 'x' ) ) ) )

    ##
    # Part 1
    ##

    fabric = np.zeros( (10000, 10000) )

    # Plot the rectangles
    for r in rects:
        for w in range( r.width ):
            for h in range( r.height ):
                fabric[ h + r.y1, w + r.x1 ] += 1

    count = 0

    for row in fabric:
        count += len( row[ row > 1 ] )
        
    print( f"Part 1 answer: {count}" )

    ##
    # Part 2
    ##

    overlaps = set()

    for r1, r2 in combinations( rects, 2 ):
        if r1.overlap( r2 ):
            overlaps.add( r1 )
            overlaps.add( r2 )

    print( f"Part 2 answer: {list(set( rects ) - overlaps)[ 0 ].id}" )

class Rect:
    def __init__( self, id, x, y, width, height ):
        self.id = id

        self.x1 = x
        self.y1 = y

        self.x2 = x + width
        self.y2 = y + height

        self.width = width
        self.height = height

    def __eq__( self, other ):
        return (self.x1 == other.x1) and (self.width == other.width) and (self.height == other.height)

    def __hash__( self ):
        return self.id

    def __str__( self ):
        return f"{self.x1},{self.y1} -> {self.width}x{self.height}"
    
    def overlap( self, other ):
        if (other.x1 >= self.x2) or (other.x2 <= self.x1):
            return False
        elif (other.y1 >= self.y2) or (other.y2 <= self.y1):
            return False
        
        return True

if __name__ == "__main__":
    main( argv=sys.argv )