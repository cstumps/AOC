# --- Day 24: Lobby Layout ---

# Your raft makes it to the tropical island; it turns out that the small crab was an 
# excellent navigator. You make your way to the resort.

# As you enter the lobby, you discover a small problem: the floor is being renovated. 
# You can't even reach the check-in desk until they've finished installing the new 
# tile floor.

# The tiles are all hexagonal; they need to be arranged in a hex grid with a very specific 
# color pattern. Not in the mood to wait, you offer to help figure out the pattern.

# The tiles are all white on one side and black on the other. They start with the white side 
# facing up. The lobby is large enough to fit whatever pattern might need to appear there.

# A member of the renovation crew gives you a list of the tiles that need to be flipped 
# over (your puzzle input). Each line in the list identifies a single tile that needs to
# be flipped by giving a series of steps starting from a reference tile in the very center 
# of the room. (Every line starts from the same reference tile.)

# Because the tiles are hexagonal, every tile has six neighbors: east, southeast, 
# southwest, west, northwest, and northeast. These directions are given in your list,
#  respectively, as e, se, sw, w, nw, and ne. A tile is identified by a series of these 
# directions with no delimiters; for example, esenee identifies the tile you land on if 
# you start at the reference tile and then move one tile east, one tile southeast, one 
# tile northeast, and one tile east.

# Each time a tile is identified, it flips from white to black or from black to white. 
# Tiles might be flipped more than once. For example, a line like esew flips a tile 
# immediately adjacent to the reference tile, and a line like nwwswee flips the reference 
# tile itself.

# Here is a larger example:

# sesenwnenenewseeswwswswwnenewsewsw
# neeenesenwnwwswnenewnwwsewnenwseswesw
# seswneswswsenwwnwse
# nwnwneseeswswnenewneswwnewseswneseene
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# wsweesenenewnwwnwsenewsenwwsesesenwne
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# eneswnwswnwsenenwnwnwwseeswneewsenese
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew

# In the above example, 10 tiles are flipped once (to black), and 5 more are flipped 
# twice (to black, then back to white). After all of these instructions have been followed, 
# a total of 10 tiles are black.

# Go through the renovation crew's list and determine which tiles they need to flip. 
# After all of the instructions have been followed, how many tiles are left with the 
# black side up?

# --- Part Two ---

# The tile floor in the lobby is meant to be a living art exhibit. Every day, the tiles 
# are all flipped according to the following rules:

#     Any black tile with zero or more than 2 black tiles immediately adjacent to it is 
#     flipped to white.

#     Any white tile with exactly 2 black tiles immediately adjacent to it is flipped 
#     to black.

# Here, tiles immediately adjacent means the six tiles directly touching the tile in question.

# The rules are applied simultaneously to every tile; put another way, it is first determined 
# which tiles need to be flipped, then they are all flipped at the same time.

# In the above example, the number of black tiles that are facing up after the given number 
# of days has passed is as follows:

# Day 1: 15
# Day 2: 12
# Day 3: 25
# Day 4: 14
# Day 5: 23
# Day 6: 28
# Day 7: 41
# Day 8: 37
# Day 9: 49
# Day 10: 37

# Day 20: 132
# Day 30: 259
# Day 40: 406
# Day 50: 566
# Day 60: 788
# Day 70: 1106
# Day 80: 1373
# Day 90: 1844
# Day 100: 2208

# After executing this process a total of 100 times, there would be 2208 black 
# tiles facing up.

# How many tiles will be black after 100 days?

import sys 
import numpy as np
from scipy.ndimage import convolve

COLOR_BLACK = 1
COLOR_WHITE = 0

DIR_E  = '0'
DIR_SE = '1'
DIR_SW = '2'
DIR_W  = '3'
DIR_NW = '4'
DIR_NE = '5'

def main( argv ):

    # Read in input file
    #with open( "input/day24-input.txt", "r" ) as f:
    #    data = [ line.rstrip() for line in f ]

    data = [ 'sesenwnenenewseeswwswswwnenewsewsw',
             'neeenesenwnwwswnenewnwwsewnenwseswesw',
             'seswneswswsenwwnwse',
             'nwnwneseeswswnenewneswwnewseswneseene',
             'swweswneswnenwsewnwneneseenw',
             'eesenwseswswnenwswnwnwsewwnwsene',
             'sewnenenenesenwsewnenwwwse',
             'wenwwweseeeweswwwnwwe',
             'wsweesenenewnwwnwsenewsenwwsesesenwne',
             'neeswseenwwswnwswswnw',
             'nenwswwsewswnenenewsenwsenwnesesenew',
             'enewnwewneswsewnwswenweswnenwsenwsw',
             'sweneswneswneneenwnewenewwneswswnese',
             'swwesenesewenwneswnwwneseswwne',
             'enesenwswwswneneswsenwnewswseenwsese',
             'wnwnesenesenenwwnenwsewesewsesesew',
             'nenewswnwewswnenesenwnesewesw',
             'eneswnwswnwsenenwnwnwwseeswneewsenese',
             'neswnwewnwnwseenwseesewsenwsweewe',
             'wseweeenwnesenwwwswnew', ]

    ##
    # Part 1 - Uses cube coordinates
    ##

    tiles = []

    for line in data:
        line = line.replace( 'se', DIR_SE )
        line = line.replace( 'sw', DIR_SW )
        line = line.replace( 'nw', DIR_NW )
        line = line.replace( 'ne', DIR_NE )
        line = line.replace( 'e', DIR_E )
        line = line.replace( 'w', DIR_W )

        h = Hex( 0, 0, 0 )

        for val in line:
            h.go( val )

        if h in tiles:
            tiles[ tiles.index( h ) ].flip()
        else:
            h.flip()
            tiles.append( h )

    # Count up black tiles
    count = 0

    for t in tiles:
        if t.color == COLOR_BLACK:
            count += 1

    print( "Part 1 answer: %s" % count )

    ##
    # Part 2
    ##

    # Start with the list from part 1 and determine how big a cube we need
    maxQ = 0
    minQ = 0
    maxR = 0
    minR = 0
    maxS = 0
    minS = 0

    for h in tiles:
        if h.q > maxQ:
            maxQ = h.q
        elif h.q < minQ:
            minQ = h.q

        if h.r > maxR:
            maxR = h.r
        elif h.r < minR:
            minR = h.r

        if h.s > maxS:
            maxS = h.s
        elif h.s < minS:
            minS = h.s

    maxQ = (maxQ - minQ) * 2
    maxR = (maxR - minR) * 2
    maxS = (maxS - minS) * 2

    # Define the playing field and set the initial state
    field = np.zeros( (maxQ, maxR, maxS), dtype='int' )

    for h in tiles:
        if h.color == COLOR_BLACK:
            # Translate the tile into screen coords
            x = h.q + int( maxQ / 2 )
            y = int( maxS / 2 ) - h.s
            z = int( maxR / 2 ) - h.r

            print( "x = %s, y = %s, z = %s" % (x, y, z) )

            field[ z ][ y ][ x ] = 1
            #field[ h.q ][ h.r ][ h.s ] = 1
            # z = r
            # x = q
            # y = s


    field = runDay( field )

    print( np.count_nonzero( field ) )

    # for q in enumerate( maxQ ):
    #     for r in enumerate( maxR ):
    #         for s in enumerate( maxS ):
    #             if flips[ q ][ r ][ s ]:
    #                 field[ q ][ r ][ s ] = 

    # (0, 0, 0) isn't in the center of hte grid :( this is the issue. rebase?
    # Draw out an example in 2D space. should be able to remap all initial values using bound of
    # array and current x,y(,z)

# Great info on hex grids and coordinate systems:  
#   https://www.redblobgames.com/grids/hexagons/
    
def runDay( field ):
    # Define a convolution kernel - not sure this is right.  negative indexes might be wrong... it is wrong
    kernel = np.zeros( (3, 3, 3), dtype='int' )
    kernel[  0 ][ -1 ][  1 ] = 1
    kernel[  1 ][ -1 ][  0 ] = 1
    kernel[  1 ][  0 ][ -1 ] = 1
    kernel[  0 ][  1 ][ -1 ] = 1
    kernel[ -1 ][  1 ][  0 ] = 1
    kernel[ -1 ][  0 ][  1 ] = 1

    # Run the days
    counts = convolve( field, kernel, mode='constant' )

    return (field & (counts == 1)) | (counts == 2) #(field & (counts == 2)) | (np.invert( field ) & (counts == 2))

class Hex( object ):
    def __init__( self, q, r, s, color=COLOR_WHITE ):
        self.q = q
        self.r = r
        self.s = s
        self.color = color

    def __str__( self ):
        return "q = %s, r = %s, s = %s -> %s" % (self.q, self.r, self.s, self.color)

    def __eq__( self, other ):
        return (self.q == other.q) and (self.r == other.r) and (self.s == other.s)

    def go( self, dir ):
        # An alternative way to do this is to have unit objects in a look up table and 
        # rely on the addition operator.
        if dir == DIR_SE:
            self.s -= 1
            self.r += 1
        elif dir == DIR_SW:
            self.q -= 1
            self.r += 1
        elif dir == DIR_NW:
            self.s += 1
            self.r -= 1
        elif dir == DIR_NE:
            self.q += 1
            self.r -= 1
        elif dir == DIR_E:
            self.q += 1
            self.s -= 1
        elif dir == DIR_W:
            self.q -= 1
            self.s += 1

    def flip( self ):
        self.color ^= 1




if __name__ == "__main__":
    main( argv=sys.argv )