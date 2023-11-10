# --- Day 3: Perfectly Spherical Houses in a Vacuum ---

# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location, and
# then an elf at the North Pole calls him via radio and tells him where to move
# next. Moves are always exactly one house to the north (^), south (v), east
# (>), or west (<). After each move, he delivers another present to the house at
# his new location.

# However, the elf back at the north pole has had a little too much eggnog, and
# so his directions are a little off, and Santa ends up visiting some houses
# more than once. How many houses receive at least one present?

# For example:

#     > delivers presents to 2 houses: one at the starting location, and one to
#     > the east.

#     ^>v< delivers presents to 4 houses in a square, including twice to the
#     house at his starting/ending location.

#     ^v^v^v^v^v delivers a bunch of presents to some very lucky children at
#     only 2 houses.

# --- Part Two ---

# The next year, to speed up the process, Santa creates a robot version of
# himself, Robo-Santa, to deliver presents with him.

# Santa and Robo-Santa start at the same location (delivering two presents to
# the same starting house), then take turns moving based on instructions from
# the elf, who is eggnoggedly reading from the same script as the previous year.

# This year, how many houses receive at least one present?

# For example:

#     ^v delivers presents to 3 houses, because Santa goes north, and then
#     Robo-Santa goes south.

#     ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up
#     back where they started.

#     ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one
#     direction and Robo-Santa going the other.

import sys

def main( argv ):

    data = []

    # Read in input file and add up the sums
    with open( "input/day03-input.txt", "r" ) as f:
        data = f.readlines()[ 0 ]

    ##
    # Part 1
    ##

    houses = followPath( data, { "0,0": 1 } )

    print( f"Part 1 answer: {len( houses.keys() )}" )

    ##
    # Part 2
    ##

    path1 = data[ 1::2 ]
    path2 = data[ ::2 ]

    houses = followPath( path1, { "0,0": 2 } )
    houses = followPath( path2, houses )

    print( f"Part 2 answer: {len( houses.keys() )}" )

def followPath( path, houses ):
    x = 0
    y = 0
    
    for dir in path:
        if dir == '<':
            x -= 1
        elif dir == '>':
            x += 1
        elif dir == '^':
            y += 1
        else:
            y -= 1

        loc = str( x ) + ',' + str( y )
        
        if loc in houses.keys():
            houses[ loc ] += 1
        else:
            houses[ loc ] = 1

    return houses


if __name__ == "__main__":
    main( argv=sys.argv )
