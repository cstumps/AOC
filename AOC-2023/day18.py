# --- Day 18: Lavaduct Lagoon ---

# Thanks to your efforts, the machine parts factory is one of the first
# factories up and running since the lavafall came back. However, to catch up
# with the large backlog of parts requests, the factory will also need a large
# supply of lava for a while; the Elves have already started creating a large
# lagoon nearby for this purpose.

# However, they aren't sure the lagoon will be big enough; they've asked you to
# take a look at the dig plan (your puzzle input). For example:

# R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)

# The digger starts in a 1 meter cube hole in the ground. They then dig the
# specified number of meters up (U), down (D), left (L), or right (R), clearing
# full 1 meter cubes as they go. The directions are given as seen from above, so
# if "up" were north, then "right" would be east, and so on. Each trench is also
# listed with the color that the edge of the trench should be painted as an RGB
# hexadecimal color code.

# When viewed from above, the above example dig plan would result in the
# following loop of trench (#) having been dug out from otherwise ground-level
# terrain (.):

# #######
# #.....#
# ###...#
# ..#...#
# ..#...#
# ###.###
# #...#..
# ##..###
# .#....#
# .######

# At this point, the trench could contain 38 cubic meters of lava. However, this
# is just the edge of the lagoon; the next step is to dig out the interior so
# that it is one meter deep as well:

# #######
# #######
# #######
# ..#####
# ..#####
# #######
# #####..
# #######
# .######
# .######

# Now, the lagoon can contain a much more respectable 62 cubic meters of lava.
# While the interior is dug out, the edges are also painted according to the
# color codes in the dig plan.

# The Elves are concerned the lagoon won't be large enough; if they follow their
# dig plan, how many cubic meters of lava could it hold?

# --- Part Two ---

# The Elves were right to be concerned; the planned lagoon would be much too
# small.

# After a few minutes, someone realizes what happened; someone swapped the color
# and instruction parameters when producing the dig plan. They don't have time
# to fix the bug; one of them asks if you can extract the correct instructions
# from the hexadecimal codes.

# Each hexadecimal code is six hexadecimal digits long. The first five
# hexadecimal digits encode the distance in meters as a five-digit hexadecimal
# number. The last hexadecimal digit encodes the direction to dig: 0 means R, 1
# means D, 2 means L, and 3 means U.

# So, in the above example, the hexadecimal codes can be converted into the true
# instructions:

#     #70c710 = R 461937
#     #0dc571 = D 56407
#     #5713f0 = R 356671
#     #d2c081 = D 863240
#     #59c680 = R 367720
#     #411b91 = D 266681
#     #8ceee2 = L 577262
#     #caa173 = U 829975
#     #1b58a2 = L 112010
#     #caa171 = D 829975
#     #7807d2 = L 491645
#     #a77fa3 = U 686074
#     #015232 = L 5411
#     #7a21e3 = U 500254

# Digging out this loop and its interior produces a lagoon that can hold an
# impressive 952408144115 cubic meters of lava.

# Convert the hexadecimal color codes into the correct instructions; if the
# Elves follow this new dig plan, how many cubic meters of lava could the lagoon
# hold?

import sys
import math

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day18-input.txt", "r" ) as f:
        data = [ line.rstrip( '\n' ) for line in f ]

    #data = [ 'R 6 (#70c710)',
    #         'D 5 (#0dc571)',
    #         'L 2 (#5713f0)',
    #         'D 2 (#d2c081)',
    #         'R 2 (#59c680)',
    #         'D 2 (#411b91)',
    #         'L 5 (#8ceee2)',
    #         'U 2 (#caa173)',
    #         'L 1 (#1b58a2)',
    #         'U 2 (#caa171)',
    #         'R 2 (#7807d2)',
    #         'U 3 (#a77fa3)',
    #         'L 2 (#015232)',
    #         'U 2 (#7a21e3)' ]

    ##
    # Part 1
    ##

    # Shoelace theorem find the interior lattice points which can then be used with 
    # Pick's theorem to find the area since we also know the perimeter.  I was on the
    # right track with the Shoelace theorem myself but needed a nudge to work it in 
    # with Pick's.  Might have arrived at it on my own if I wasn't already behind on 
    # the puzzles.

    moves = [ (l.split()[ 0 ], int( l.split()[ 1 ] ) ) for l in data ]
    coords, perimeter = generateCoords( moves ) 

    area = math.floor( shoeLace( coords ) + (perimeter / 2) + 1 )

    print( f"Part 1 answer: {area}" )
    
    ##
    # Part 2
    ##

    lut = { '0': 'R', '1': 'D', '2': 'L', '3': 'U' }

    decodedMoves = []

    for line in data:
        val = line.split()[ 2 ][ 2:-1 ]

        dir = lut[ val[ -1 ] ]
        dist = int( val[ :-1 ], 16 )

        decodedMoves.append( (dir, dist) )

    coords, perimeter = generateCoords( decodedMoves )

    area = math.floor( shoeLace( coords ) + (perimeter / 2) + 1 )

    print( f"Part 2 answer: {area}" )

# This finds the number of interior lattice points
def shoeLace( corners ):
    n = len( corners )
    area = 0.0

    for i in range( n ):
        j = (i + 1) % n

        area += corners[ i ][ 0 ] * corners[ j ][ 1 ]
        area -= corners[ j ][ 0 ] * corners[ i ][ 1 ]
        
    area = abs( area ) / 2.0

    return area

# Generates a list of coordinates from directions and returns 
# them along with the perimeter
def generateCoords( data ):
    coords = []
    counter = 0

    x = 0
    y = 0

    for d in data:
        dir, step = d

        if dir == 'R':
            x += step
        elif dir == 'L':
            x -= step
        elif dir == 'U':
            y -= step
        else:
            y += step

        counter += step

        coords.append( (x, y) )

    return coords, counter


if __name__ == "__main__":
    main( argv=sys.argv )