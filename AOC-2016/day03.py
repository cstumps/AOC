# --- Day 3: Squares With Three Sides ---

# Now that you can think clearly, you move deeper into the labyrinth of hallways
# and office furniture that makes up this part of Easter Bunny HQ. This must be
# a graphic design department; the walls are covered in specifications for
# triangles.

# Or are they?

# The design document gives the side lengths of each triangle it describes,
# but... 5 10 25? Some of these aren't triangles. You can't help but mark the
# impossible ones.

# In a valid triangle, the sum of any two sides must be larger than the
# remaining side. For example, the "triangle" given above is impossible, because
# 5 + 10 is not larger than 25.

# In your puzzle input, how many of the listed triangles are possible?

# --- Part Two ---

# Now that you've helpfully marked up their design documents, it occurs to you
# that triangles are specified in groups of three vertically. Each set of three
# numbers in a column specifies a triangle. Rows are unrelated.

# For example, given the following specification, numbers with the same hundreds
# digit would be part of the same triangle:

# 101 301 501
# 102 302 502
# 103 303 503
# 201 401 601
# 202 402 602
# 203 403 603

# In your puzzle input, and instead reading by columns, how many of the listed
# triangles are possible?

import sys

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day03-input.txt", "r" ) as f:
        data = [ list( map( int, l.split() ) ) for l in f.readlines() ]

    ##
    # Part 1
    ##

    valid = [ t for t in data if sorted(t)[ 0 ] + sorted(t)[ 1 ] > sorted(t)[ 2 ] ]

    print( f"Part 1 answer: {len( valid )}" )

    ##
    # Part 2
    ##

    valid = 0

    for row in range( 0, len( data ), 3 ):
        for col in range( len( data[ row ] ) ):
            t = sorted( [ data[ row ][ col ], data[ row + 1 ][ col ], data[ row + 2 ][ col ] ] )

            if t[ 0 ] + t[ 1 ] > t[ 2 ]:
                valid += 1

    print( f"Part 2 answer: {valid}" )


if __name__ == "__main__":
    main( argv=sys.argv )
