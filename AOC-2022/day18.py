# --- Day 18: Boiling Boulders ---

# You and the elephants finally reach fresh air. You've emerged near the base of
# a large volcano that seems to be actively erupting! Fortunately, the lava
# seems to be flowing away from you and toward the ocean.

# Bits of lava are still being ejected toward you, so you're sheltering in the
# cavern exit a little longer. Outside the cave, you can see the lava landing in
# a pond and hear it loudly hissing as it solidifies.

# Depending on the specific compounds in the lava and speed at which it cools,
# it might be forming obsidian! The cooling rate should be based on the surface
# area of the lava droplets, so you take a quick scan of a droplet as it flies
# past you (your puzzle input).

# Because of how quickly the lava is moving, the scan isn't very good; its
# resolution is quite low and, as a result, it approximates the shape of the
# lava droplet with 1x1x1 cubes on a 3D grid, each given as its x,y,z position.

# To approximate the surface area, count the number of sides of each cube that
# are not immediately connected to another cube. So, if your scan were only two
# adjacent cubes like 1,1,1 and 2,1,1, each cube would have a single side
# covered and five sides exposed, a total surface area of 10 sides.

# Here's a larger example:

# 2,2,2
# 1,2,2
# 3,2,2
# 2,1,2
# 2,3,2
# 2,2,1
# 2,2,3
# 2,2,4
# 2,2,6
# 1,2,5
# 3,2,5
# 2,1,5
# 2,3,5

# In the above example, after counting up all the sides that aren't connected to
# another cube, the total surface area is 64.

# What is the surface area of your scanned lava droplet?

# --- Part Two ---

# Something seems off about your calculation. The cooling rate depends on
# exterior surface area, but your calculation also included the surface area of
# air pockets trapped in the lava droplet.

# Instead, consider only cube sides that could be reached by the water and steam
# as the lava droplet tumbles into the pond. The steam will expand to reach as
# much as possible, completely displacing any air on the outside of the lava
# droplet but never expanding diagonally.

# In the larger example above, exactly one cube of air is trapped within the
# lava droplet (at 2,2,5), so the exterior surface area of the lava droplet is
# 58.

# What is the exterior surface area of your scanned lava droplet?

import sys
import numpy as np
from scipy.signal import convolve
from scipy.ndimage import binary_fill_holes

def main( argv ):

    with open( "input/day18-input.txt" ) as f:
        data = f.readlines()

    #data = [ '2,2,2',
    #         '1,2,2',
    #         '3,2,2',
    #         '2,1,2',
    #         '2,3,2',
    #         '2,2,1',
    #         '2,2,3',
    #         '2,2,4',
    #         '2,2,6',
    #         '1,2,5',
    #         '3,2,5',
    #         '2,1,5',
    #         '2,3,5' ]

    width = 25
    height = 25
    depth = 25

    voxels = np.zeros( (depth, height, width) )

    for line in data:
        x, y, z = list( map( int, line.strip().split( ',' ) ) )
        voxels[ z ][ y ][ x ] = 1

    kernel = np.array( [ [[ 0, 0, 0 ], [ 0, 1, 0 ], [ 0, 0, 0 ]],
                         [[ 0, 1, 0 ], [ 1, 0, 1 ], [ 0, 1, 0 ]],
                         [[ 0, 0, 0 ], [ 0, 1, 0 ], [ 0, 0, 0 ]] ] )

    ##
    # Part 1
    ##

    # Counts is the number of neighbors that each cube has
    # 6 - counts is the number of faces without a neighbor for each cube (faces exposed)
    # We multiply by the original matrix to remove cubes with no neighbors (unconnected)

    counts = 6 - convolve( voxels, kernel, mode='same' )
    faceCount = (voxels * counts).sum()

    print( f"Part 1 answer: {faceCount}" )

    ## 
    # Part 2
    ##

    # So this does work however there two odd quirks.  
    #  1. scipy.ndimage.convolve gives a different and incorrect answer if used
    #  2. The answer to part 1 has a long decimal for some reason:
    #       4320.000000000002
    #     It's clear what the answer is, just not sure why we're getting that.

    # I did get the idea to use binary_fill_holes from the solutions megathread. 
    # Also got help for the selection of kernel there (I had started with a Laplacian)
    # and recogonizing that the output from convolve was the number of neighbors that each
    # cube had (therefore we have to subtrace 6 to see how many faces don't have neighbors).

    filledVoxels = binary_fill_holes( voxels )

    counts = 6 - convolve( filledVoxels, kernel, mode='same' )
    faceCount = (filledVoxels * counts).sum()

    print( f"Part 2 answer: {faceCount}" )


if __name__ == "__main__":
    main( argv=sys.argv )