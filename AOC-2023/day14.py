# --- Day 14: Parabolic Reflector Dish ---

# You reach the place where all of the mirrors were pointing: a massive
# parabolic reflector dish attached to the side of another large mountain.

# The dish is made up of many small mirrors, but while the mirrors themselves
# are roughly in the shape of a parabolic reflector dish, each individual mirror
# seems to be pointing in slightly the wrong direction. If the dish is meant to
# focus light, all it's doing right now is sending it in a vague direction.

# This system must be what provides the energy for the lava! If you focus the
# reflector dish, maybe you can go where it's pointing and use the light to fix
# the lava production.

# Upon closer inspection, the individual mirrors each appear to be connected via
# an elaborate system of ropes and pulleys to a large metal platform below the
# dish. The platform is covered in large rocks of various shapes. Depending on
# their position, the weight of the rocks deforms the platform, and the shape of
# the platform controls which ropes move and ultimately the focus of the dish.

# In short: if you move the rocks, you can focus the dish. The platform even has
# a control panel on the side that lets you tilt it in one of four directions!
# The rounded rocks (O) will roll when the platform is tilted, while the
# cube-shaped rocks (#) will stay in place. You note the positions of all of the
# empty spaces (.) and rocks (your puzzle input). For example:

# O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....

# Start by tilting the lever so all of the rocks will slide north as far as they
# will go:

# OOOO.#.O..
# OO..#....#
# OO..O##..O
# O..#.OO...
# ........#.
# ..#....#.#
# ..O..#.O.O
# ..O.......
# #....###..
# #....#....

# You notice that the support beams along the north side of the platform are
# damaged; to ensure the platform doesn't collapse, you should calculate the
# total load on the north support beams.

# The amount of load caused by a single rounded rock (O) is equal to the number
# of rows from the rock to the south edge of the platform, including the row the
# rock is on. (Cube-shaped rocks (#) don't contribute to load.) So, the amount
# of load caused by each rock in each row is as follows:

# OOOO.#.O.. 10
# OO..#....#  9
# OO..O##..O  8
# O..#.OO...  7
# ........#.  6
# ..#....#.#  5
# ..O..#.O.O  4
# ..O.......  3
# #....###..  2
# #....#....  1

# The total load is the sum of the load caused by all of the rounded rocks. In
# this example, the total load is 136.

# Tilt the platform so that the rounded rocks all roll north. Afterward, what is
# the total load on the north support beams?

# --- Part Two ---

# The parabolic reflector dish deforms, but not in a way that focuses the beam.
# To do that, you'll need to move the rocks to the edges of the platform.
# Fortunately, a button on the side of the control panel labeled "spin cycle"
# attempts to do just that!

# Each cycle tilts the platform four times so that the rounded rocks roll north,
# then west, then south, then east. After each tilt, the rounded rocks roll as
# far as they can before the platform tilts in the next direction. After one
# cycle, the platform will have finished rolling the rounded rocks in those four
# directions in that order.

# Here's what happens in the example above after each of the first few cycles:

# After 1 cycle:
# .....#....
# ....#...O#
# ...OO##...
# .OO#......
# .....OOO#.
# .O#...O#.#
# ....O#....
# ......OOOO
# #...O###..
# #..OO#....

# After 2 cycles:
# .....#....
# ....#...O#
# .....##...
# ..O#......
# .....OOO#.
# .O#...O#.#
# ....O#...O
# .......OOO
# #..OO###..
# #.OOO#...O

# After 3 cycles:
# .....#....
# ....#...O#
# .....##...
# ..O#......
# .....OOO#.
# .O#...O#.#
# ....O#...O
# .......OOO
# #...O###.O
# #.OOO#...O

# This process should work if you leave it running long enough, but you're still
# worried about the north support beams. To make sure they'll survive for a
# while, you need to calculate the total load on the north support beams after
# 1000000000 cycles.

# In the above example, after 1000000000 cycles, the total load on the north
# support beams is 64.

# Run the spin cycle for 1000000000 cycles. Afterward, what is the total load on
# the north support beams?

import sys
import numpy as np

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day14-input.txt", "r" ) as f:
        data = [ line.rstrip( '\n' ) for line in f ]

    #data = [ 'O....#....',
    #         'O.OO#....#',
    #         '.....##...',
    #         'OO.#O....O',
    #         '.O.....O#.',
    #         'O.#..O.#.#',
    #         '..O..#O..O',
    #         '.......O..',
    #         '#....###..',
    #         '#OO..#....' ]

    grid = np.array( [ list( map( convertElement, line ) ) for line in data ] )

    ##
    # Part 1
    ##

    northGrid = np.flipud( np.vstack( [ tiltCol( c ) for c in np.flipud( grid ).T ] ).T )
    load = findLoad( northGrid )

    print( f"Part 1 answer: {load}" )

    ##
    # Part 2
    ##

    grid = np.flipud( grid ).T
    seenGrids = []

    initialCycle = 0
    cycleLength = 0

    stopIteration = False
    i = 1

    # Iterate until we've discovered the start of the first full cycle and the 
    # length of a full cycle
    while not stopIteration:
        grid = cycleGrid( grid )

        for g in seenGrids:
            if (grid == g[ 0 ]).all():
                if not initialCycle:
                    initialCycle = i
                    seenGrids.clear()
                elif not cycleLength:
                    cycleLength = i - initialCycle
                    stopIteration = True

                break

        # Save off grids we've seen as well as the load associated with it
        seenGrids.append( [ grid, findLoad( np.rot90( grid ) ) ] )
        i += 1

    # Using that info, compute the offset into the full cycle list (seenGrids) that
    # our answer is
    x = (1000000000 - initialCycle)
    offset = x % cycleLength

    print( f"Part 2 answer: {seenGrids[ offset ][ 1 ]}" )


def tiltCol( col ):
    return np.concatenate( [ np.sort( i ) for i in np.split( col, np.where( col == -1 )[ 0 ] ) ] )

def cycleGrid( grid ):
    grid = np.vstack( [ tiltCol( c ) for c in grid ] )
    grid = np.vstack( [ tiltCol( c ) for c in np.rot90( grid, k=-1 ) ] )
    grid = np.vstack( [ tiltCol( c ) for c in np.rot90( grid, k=-1 ) ] )
    grid = np.vstack( [ tiltCol( c ) for c in np.rot90( grid, k=-1 ) ] )
    grid = np.rot90( grid, k=-1 )

    return grid

def findLoad( grid ):
    locs = np.where( np.flipud( grid ) == 1 )
    loads = [ l + 1 for l in locs[ 0 ] ]

    return sum( loads )

def convertElement( e ):
    if e == '.':
        return 0
    elif e == '#':
        return -1
    elif e == 'O':
        return 1
    

if __name__ == "__main__":
    main( argv=sys.argv )