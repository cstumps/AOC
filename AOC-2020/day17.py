# --- Day 17: Conway Cubes ---

# As your flight slowly drifts through the sky, the Elves at the Mythical
# Information Bureau at the North Pole contact you. They'd like some help
# debugging a malfunctioning experimental energy source aboard one of their
# super-secret imaging satellites.

# The experimental energy source is based on cutting-edge technology: a set of
# Conway Cubes contained in a pocket dimension! When you hear it's having
# problems, you can't help but agree to take a look.

# The pocket dimension contains an infinite 3-dimensional grid. At every integer
# 3-dimensional coordinate (x,y,z), there exists a single cube which is either
# active or inactive.

# In the initial state of the pocket dimension, almost all cubes start inactive.
# The only exception to this is a small flat region of cubes (your puzzle
# input); the cubes in this region start in the specified active (#) or inactive
# (.) state.

# The energy source then proceeds to boot up by executing six cycles.

# Each cube only ever considers its neighbors: any of the 26 other cubes where
# any of their coordinates differ by at most 1. For example, given the cube at
# x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at
# x=0,y=2,z=3, and so on.

# During a cycle, all cubes simultaneously change their state according to the
# following rules:

#     If a cube is active and exactly 2 or 3 of its neighbors are also active,
#     the cube remains active. Otherwise, the cube becomes inactive.

#     If a cube is inactive but exactly 3 of its neighbors are active, the cube
#     becomes active. Otherwise, the cube remains inactive.

# The engineers responsible for this experimental energy source would like you
# to simulate the pocket dimension and determine what the configuration of cubes
# should be at the end of the six-cycle boot process.

# For example, consider the following initial state:

# .#.
# ..#
# ###

# Even though the pocket dimension is 3-dimensional, this initial state
# represents a small 2-dimensional slice of it. (In particular, this initial
# state defines a 3x3x1 region of the 3-dimensional space.)

# Simulating a few cycles from this initial state produces the following
# configurations, where the result of each cycle is shown layer-by-layer at each
# given z coordinate (and the frame of view follows the active cells in each
# cycle):

# Before any cycles:

# z=0
# .#.
# ..#
# ###


# After 1 cycle:

# z=-1
# #..
# ..#
# .#.

# z=0
# #.#
# .##
# .#.

# z=1
# #..
# ..#
# .#.


# After 2 cycles:

# z=-2
# .....
# .....
# ..#..
# .....
# .....

# z=-1
# ..#..
# .#..#
# ....#
# .#...
# .....

# z=0
# ##...
# ##...
# #....
# ....#
# .###.

# z=1
# ..#..
# .#..#
# ....#
# .#...
# .....

# z=2
# .....
# .....
# ..#..
# .....
# .....


# After 3 cycles:

# z=-2
# .......
# .......
# ..##...
# ..###..
# .......
# .......
# .......

# z=-1
# ..#....
# ...#...
# #......
# .....##
# .#...#.
# ..#.#..
# ...#...

# z=0
# ...#...
# .......
# #......
# .......
# .....##
# .##.#..
# ...#...

# z=1
# ..#....
# ...#...
# #......
# .....##
# .#...#.
# ..#.#..
# ...#...

# z=2
# .......
# .......
# ..##...
# ..###..
# .......
# .......
# .......

# After the full six-cycle boot process completes, 112 cubes are left in the
# active state.

# Starting with your given initial configuration, simulate six cycles. How many
# cubes are left in the active state after the sixth cycle?

# --- Part Two ---

# For some reason, your simulated results don't match what the experimental
# energy source engineers expected. Apparently, the pocket dimension actually
# has four spatial dimensions, not three.

# The pocket dimension contains an infinite 4-dimensional grid. At every integer
# 4-dimensional coordinate (x,y,z,w), there exists a single cube (really, a
# hypercube) which is still either active or inactive.

# Each cube only ever considers its neighbors: any of the 80 other cubes where
# any of their coordinates differ by at most 1. For example, given the cube at
# x=1,y=2,z=3,w=4, its neighbors include the cube at x=2,y=2,z=3,w=3, the cube
# at x=0,y=2,z=3,w=4, and so on.

# The initial state of the pocket dimension still consists of a small flat
# region of cubes. Furthermore, the same rules for cycle updating still apply:
# during each cycle, consider the number of active neighbors of each cube.

# For example, consider the same initial state as in the example above. Even
# though the pocket dimension is 4-dimensional, this initial state represents a
# small 2-dimensional slice of it. (In particular, this initial state defines a
# 3x3x1x1 region of the 4-dimensional space.)

# Simulating a few cycles from this initial state produces the following
# configurations, where the result of each cycle is shown layer-by-layer at each
# given z and w coordinate:

# Before any cycles:

# z=0, w=0
# .#.
# ..#
# ###


# After 1 cycle:

# z=-1, w=-1
# #..
# ..#
# .#.

# z=0, w=-1
# #..
# ..#
# .#.

# z=1, w=-1
# #..
# ..#
# .#.

# z=-1, w=0
# #..
# ..#
# .#.

# z=0, w=0
# #.#
# .##
# .#.

# z=1, w=0
# #..
# ..#
# .#.

# z=-1, w=1
# #..
# ..#
# .#.

# z=0, w=1
# #..
# ..#
# .#.

# z=1, w=1
# #..
# ..#
# .#.


# After 2 cycles:

# z=-2, w=-2
# .....
# .....
# ..#..
# .....
# .....

# z=-1, w=-2
# .....
# .....
# .....
# .....
# .....

# z=0, w=-2
# ###..
# ##.##
# #...#
# .#..#
# .###.

# z=1, w=-2
# .....
# .....
# .....
# .....
# .....

# z=2, w=-2
# .....
# .....
# ..#..
# .....
# .....

# z=-2, w=-1
# .....
# .....
# .....
# .....
# .....

# z=-1, w=-1
# .....
# .....
# .....
# .....
# .....

# z=0, w=-1
# .....
# .....
# .....
# .....
# .....

# z=1, w=-1
# .....
# .....
# .....
# .....
# .....

# z=2, w=-1
# .....
# .....
# .....
# .....
# .....

# z=-2, w=0
# ###..
# ##.##
# #...#
# .#..#
# .###.

# z=-1, w=0
# .....
# .....
# .....
# .....
# .....

# z=0, w=0
# .....
# .....
# .....
# .....
# .....

# z=1, w=0
# .....
# .....
# .....
# .....
# .....

# z=2, w=0
# ###..
# ##.##
# #...#
# .#..#
# .###.

# z=-2, w=1
# .....
# .....
# .....
# .....
# .....

# z=-1, w=1
# .....
# .....
# .....
# .....
# .....

# z=0, w=1
# .....
# .....
# .....
# .....
# .....

# z=1, w=1
# .....
# .....
# .....
# .....
# .....

# z=2, w=1
# .....
# .....
# .....
# .....
# .....

# z=-2, w=2
# .....
# .....
# ..#..
# .....
# .....

# z=-1, w=2
# .....
# .....
# .....
# .....
# .....

# z=0, w=2
# ###..
# ##.##
# #...#
# .#..#
# .###.

# z=1, w=2
# .....
# .....
# .....
# .....
# .....

# z=2, w=2
# .....
# .....
# ..#..
# .....
# .....

# After the full six-cycle boot process completes, 848 cubes are left in the
# active state.

# Starting with your given initial configuration, simulate six cycles in a
# 4-dimensional space. How many cubes are left in the active state after the
# sixth cycle?

import sys 
import numpy as np
from scipy.ndimage import convolve

def main( argv ):

    mapInt  = lambda x : 0 if x == '.' else 1

    # Read in input file
    with open( "input/day17-input.txt", "r" ) as f:
        data = [ line.rstrip() for line in f ]

    data = np.asarray( [ list( map( mapInt, line ) ) for line in data ] )

    #data = np.array( [ [ 0, 1, 0 ], [ 0, 0, 1 ], [ 1, 1, 1 ] ] )

    # Part 1

    # Convert the board from 2D into 3D and pad an additional 2 places for each
    # convolution iteration
    it = 6
    l  = len( data[ 0 ] )
    z1 = np.zeros( (l, l), dtype='int' )

    board = np.stack( (z1, data, z1) )
    board = np.pad( board, (it, it), "constant" )

    for i in range( it ):
        board = stepGame( board )

    print( "Part 1 answer: %s" % np.count_nonzero( board ) )

    # Part 2

    # So this part works to arrive at the correct solution.  I know the kernel in the function
    # is correct.  What I can't figure out is why when I stack the 3d arrays into a 4d array
    # I only have to stack 2 cubes... I would have thought that I'd have to stack the same
    # dimension as the cubes are.  I suspect there is a much simpler way to do that part but
    # given the time contraints and the my inexperience at visualizing 4d data this might be
    # the best we can do.

    # This guy did it far simpler though I can't figure out the syntax:
    # def answers(raw):
    #     init=np.array([list(r) for r in raw.split("\n")])=="#"
    #     N=6
    #     for D in (3,4):
    #         active=np.pad(init[(None,)*(D-init.ndim)],N)
    #         for _ in range(N):
    #             nbs=convolve(active,np.ones((3,)*D),int,mode="constant")
    #             active[:]=active&(nbs==4) | (nbs==3)
    #         yield np.sum(active)
    #
    # Here's a simpler one to understand:
    # def cycle(init, dim, gen=6):
    #     grid = init.reshape([1] * (dim - len(init.shape)) + list(init.shape))
    #     kernel = np.ones([3] * dim, dtype=np.uint8)
    #     for i in range(gen):
    #         nb = convolve(grid, kernel)
    #         grid = np.pad(grid, ((1, 1),), mode='constant')
    #         grid = ((nb == 3) | ((grid == 1) & (nb == 4))).astype(np.uint8)
    #     return np.sum(grid)

    # First convert our 2D array into a 3D stack
    z1 = np.zeros( (len( data[ 0 ] ), len( data[ 0 ] )), dtype='int' )
    board = np.stack( (z1, data, z1, z1, z1, z1, z1, z1) )

    # # Now stack that into a 4D array
    z1 = np.zeros( (len( board[ 0 ] ), len( board[ 0 ] ), len( board[ 0 ] )), dtype='int' )

    board = np.stack( (z1, board) )
    board = np.pad( board, (it, it), "constant" )

    for i in range( it ):
        board = stepGame2( board )

    print( "Part 2 answer: %s" % np.count_nonzero( board ) )

def stepGame2( board ):
    # Our convolution kernel
    kernel = np.ones( (3, 3, 3, 3), dtype='int' )
    kernel[ 1 ][ 1 ][ 1 ][ 1 ] = 0

    counts = convolve( board, kernel, mode='constant' )

    return (counts == 3) | ( (board & (counts == 2)) | (board & (counts == 3)) )

def stepGame( board ):
    # Our convolution kernel
    kernel = np.array( [ [[ 1, 1, 1 ], [ 1, 1, 1 ], [ 1, 1, 1 ]],
                         [[ 1, 1, 1 ], [ 1, 0, 1 ], [ 1, 1, 1 ]],
                         [[ 1, 1, 1 ], [ 1, 1, 1 ], [ 1, 1, 1 ]] ] )

    counts = convolve( board, kernel, mode='constant' )

    return (counts == 3) | ( (board & (counts == 2)) | (board & (counts == 3)) )


if __name__ == "__main__":
    main( argv=sys.argv )