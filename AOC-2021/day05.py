# --- Day 5: Hydrothermal Venture ---

# You come across a field of hydrothermal vents on the ocean floor! These vents
# constantly produce large, opaque clouds, so it would be best to avoid them if
# possible.

# They tend to form in lines; the submarine helpfully produces a list of nearby
# lines of vents (your puzzle input) for you to review. For example:

# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2

# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2
# where x1,y1 are the coordinates of one end the line segment and x2,y2 are the
# coordinates of the other end. These line segments include the points at both
# ends. In other words:

#     An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
#     An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

# For now, only consider horizontal and vertical lines: lines where either x1 =
# x2 or y1 = y2.

# So, the horizontal and vertical lines from the above list would produce the
# following diagram:

# .......1..
# ..1....1..
# ..1....1..
# .......1..
# .112111211
# ..........
# ..........
# ..........
# ..........
# 222111....

# In this diagram, the top left corner is 0,0 and the bottom right corner is
# 9,9. Each position is shown as the number of lines which cover that point or .
# if no line covers that point. The top-left pair of 1s, for example, comes from
# 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9
# and 0,9 -> 2,9.

# To avoid the most dangerous areas, you need to determine the number of points
# where at least two lines overlap. In the above example, this is anywhere in
# the diagram with a 2 or larger - a total of 5 points.

# Consider only horizontal and vertical lines. At how many points do at least
# two lines overlap?

# --- Part Two ---

# Unfortunately, considering only horizontal and vertical lines doesn't give you
# the full picture; you need to also consider diagonal lines.

# Because of the limits of the hydrothermal vent mapping system, the lines in
# your list will only ever be horizontal, vertical, or a diagonal line at
# exactly 45 degrees. In other words:

#     An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
#     An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

# Considering all lines from the above example would now produce the following
# diagram:

# 1.1....11.
# .111...2..
# ..2.1.111.
# ...1.2.2..
# .112313211
# ...1.2....
# ..1...1...
# .1.....1..
# 1.......1.
# 222111....

# You still need to determine the number of points where at least two lines
# overlap. In the above example, this is still anywhere in the diagram with a 2
# or larger - now a total of 12 points.

# Consider all of the lines. At how many points do at least two lines overlap?

import sys

def main( argv ):

    # Read in input file
    with open( "input/day05-input.txt", "r" ) as f:
        data = f.readlines()

    #data = [ '0,9 -> 5,9',
    #         '8,0 -> 0,8',
    #         '9,4 -> 3,4',
    #         '2,2 -> 2,1',
    #         '7,0 -> 7,4',
    #         '6,4 -> 2,0',
    #         '0,9 -> 2,9',
    #         '3,4 -> 1,4',
    #         '0,0 -> 8,8',
    #         '5,5 -> 8,2' ]

    # Generate line segments
    lineSegs = []

    for line in data:
        start = line.split()[ 0 ]
        end   = line.split()[ 2 ]

        lineSegs.append( LineSegment( int( start.split( ',' )[ 0 ] ), int( start.split( ',' )[ 1 ] ),
                                    int( end.split( ',' )[ 0 ] ), int( end.split( ',' )[ 1 ] ) ) )
    
    ##
    # Part 1
    ##

    board = [ [0]*999 for i in range( 999 ) ]

    for line in lineSegs:
        markLine( board, line )

    print( "Part 1 answer: %s" % checkBoard( board ) )

    ## 
    # Part 2
    ##

    board = [ [0]*999 for i in range( 999 ) ]

    for line in lineSegs:
        markLine( board, line, True )

    print( "Part 2 answer: %s" % checkBoard( board ) )

def markLine( board, line, diag=False ):
    if line.slope() == None: # Vertical line
        start = min( line.y1, line.y2 )
        end = max( line.y1, line.y2 )

        for i in range( start, end + 1 ):
            board[ i ][ line.x1 ] += 1

    elif line.slope() == 0.0: # Horizontal line
        start = min( line.x1, line.x2 )
        end = max( line.x1, line.x2 )

        for i in range( start, end + 1 ):
            board[ line.y1 ][ i ] += 1

    elif line.slope() in [ 1, -1 ] and diag: # Diagonal
        invertX = 1
        invertY = 1

        if line.x1 > line.x2:
            invertX = -1
        
        if line.y1 > line.y2:
            invertY = -1

        startX = line.x1
        startY = line.y1

        while startX != line.x2 + invertX:
            board[ startY ][ startX ] += 1

            startX += invertX
            startY += invertY

def checkBoard( board ):
    count = 0

    for row in board:
        for col in row:
            if col >= 2:
                count += 1

    return count

def printBoard( board ):
    print( '\n' + '\n'.join( [ ' '.join( [ str( r ) for r in row ] ) for row in board ] ) + '\n' )

class LineSegment( object ):
    def __init__( self, x1, y1, x2, y2 ):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__( self ):
        return "%s, %s -> %s, %s" % (self.x1, self.y1, self.x2, self.y2)

    def slope( self ):
        run = (self.x2 - self.x1)

        if run == 0.0:
            return None
        else:
            return (self.y2 - self.y1) / run

if __name__ == "__main__":
    main( argv=sys.argv )