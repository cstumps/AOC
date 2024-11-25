# --- Day 14: Disk Defragmentation ---

# Suddenly, a scheduled job activates the system's disk defragmenter. Were the
# situation different, you might sit and watch it for a while, but today, you
# just don't have that kind of time. It's soaking up valuable system resources
# that are needed elsewhere, and so the only option is to help it finish its
# task as soon as possible.

# The disk in question consists of a 128x128 grid; each square of the grid is
# either free or used. On this disk, the state of the grid is tracked by the
# bits in a sequence of knot hashes.

# A total of 128 knot hashes are calculated, each corresponding to a single row
# in the grid; each hash contains 128 bits which correspond to individual grid
# squares. Each bit of a hash indicates whether that square is free (0) or used
# (1).

# The hash inputs are a key string (your puzzle input), a dash, and a number
# from 0 to 127 corresponding to the row. For example, if your key string were
# flqrgnkx, then the first row would be given by the bits of the knot hash of
# flqrgnkx-0, the second row from the bits of the knot hash of flqrgnkx-1, and
# so on until the last row, flqrgnkx-127.

# The output of a knot hash is traditionally represented by 32 hexadecimal
# digits; each of these digits correspond to 4 bits, for a total of 4 * 32 = 128
# bits. To convert to bits, turn each hexadecimal digit to its equivalent binary
# value, high-bit first: 0 becomes 0000, 1 becomes 0001, e becomes 1110, f
# becomes 1111, and so on; a hash that begins with a0c2017... in hexadecimal
# would begin with 10100000110000100000000101110000... in binary.

# Continuing this process, the first 8 rows and columns for key flqrgnkx appear
# as follows, using # to denote used squares, and . to denote free ones:

# ##.#.#..-->
# .#.#.#.#   
# ....#.#.   
# #.#.##.#   
# .##.#...   
# ##..#..#   
# .#...#..   
# ##.#.##.-->
# |      |   
# V      V   

# In this example, 8108 squares are used across the entire 128x128 grid.

# Given your actual key string, how many squares are used?

# Your puzzle input is hfdlxzhv.

# --- Part Two ---

# Now, all the defragmenter needs to know is the number of regions. A region is
# a group of used squares that are all adjacent, not including diagonals. Every
# used square is in exactly one region: lone used squares form their own
# isolated regions, while several adjacent squares all count as a single region.

# In the example above, the following nine regions are visible, each marked with
# a distinct digit:

# 11.2.3..-->
# .1.2.3.4   
# ....5.6.   
# 7.8.55.9   
# .88.5...   
# 88..5..8   
# .8...8..   
# 88.8.88.-->
# |      |   
# V      V   

# Of particular interest is the region marked 8; while it does not appear
# contiguous in this small view, all of the squares marked 8 are connected when
# considering the whole 128x128 grid. In total, in this example, 1242 regions
# are present.

# How many regions are present given your key string?

import sys
import numpy as np
from day10 import getHashWithString

def main( argv ):

    data = 'hfdlxzhv'
    #data = 'flqrgnkx'

    lut = { "0": np.array( [ 0, 0, 0, 0 ] ),
            "1": np.array( [ 0, 0, 0, 1 ] ), 
            "2": np.array( [ 0, 0, 1, 0 ] ),
            "3": np.array( [ 0, 0, 1, 1 ] ),
            "4": np.array( [ 0, 1, 0, 0 ] ), 
            "5": np.array( [ 0, 1, 0, 1 ] ),
            "6": np.array( [ 0, 1, 1, 0 ] ), 
            "7": np.array( [ 0, 1, 1, 1 ] ), 
            "8": np.array( [ 1, 0, 0, 0 ] ), 
            "9": np.array( [ 1, 0, 0, 1 ] ), 
            "a": np.array( [ 1, 0, 1, 0 ] ), 
            "b": np.array( [ 1, 0, 1, 1 ] ), 
            "c": np.array( [ 1, 1, 0, 0 ] ), 
            "d": np.array( [ 1, 1, 0, 1 ] ), 
            "e": np.array( [ 1, 1, 1, 0 ] ), 
            "f": np.array( [ 1, 1, 1, 1 ] ) }

    # This creates the initial 128x128 grid
    grid = []

    for i in range( 128 ):
        h = getHashWithString( data + '-' + str( i ) )
        b = np.hstack( [ lut[ c ] for c in h ] )
        
        grid.append( b )

    grid = np.vstack( grid )

    ##
    # Part 1
    ##

    print( f"Part 1 answer: { np.count_nonzero( grid == 1 ) }" )

    ##
    # Part 2
    ##

    # Now that we've got the grid, we'll loop through it.  For any elements that are 1, that means we
    # haven't visited that group yet so we'll recurse thru it and mark it.

    groupNumber = 2

    for y, x in np.ndindex( grid.shape ):
        if grid[ y, x ] == 1:
            markGroup( y, x, grid, groupNumber )
            groupNumber += 1

    # We subtract 1 because 'group' 0 just indicates unused cells
    print( f"Part 2 answer: { len( np.unique( grid ) ) - 1 }" )

# Basically flood fill...
def markGroup( y, x, grid, gn ):
    grid[ y, x ] = gn

    if y > 0 and grid[ y-1, x ] == 1:
        markGroup( y-1, x, grid, gn )

    if y < grid.shape[ 0 ] - 1 and grid[ y+1, x ] == 1:
        markGroup( y+1, x, grid, gn )

    if x > 0 and grid[ y, x-1 ] == 1:
        markGroup( y, x-1, grid, gn )
        
    if x < grid.shape[ 1 ] - 1 and grid[ y, x+1 ] == 1:
        markGroup( y, x+1, grid, gn )


if __name__ == "__main__":
    main( argv=sys.argv )