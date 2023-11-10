# --- Day 15: Beacon Exclusion Zone ---

# You feel the ground rumble again as the distress signal leads you to a large
# network of subterranean tunnels. You don't have time to search them all, but
# you don't need to: your pack contains a set of deployable sensors that you
# imagine were originally built to locate lost Elves.

# The sensors aren't very powerful, but that's okay; your handheld device
# indicates that you're close enough to the source of the distress signal to use
# them. You pull the emergency sensor system out of your pack, hit the big
# button on top, and the sensors zoom off down the tunnels.

# Once a sensor finds a spot it thinks will give it a good reading, it attaches
# itself to a hard surface and begins monitoring for the nearest signal source
# beacon. Sensors and beacons always exist at integer coordinates. Each sensor
# knows its own position and can determine the position of a beacon precisely;
# however, sensors can only lock on to the one beacon closest to the sensor as
# measured by the Manhattan distance. (There is never a tie where two beacons
# are the same distance to a sensor.)

# It doesn't take long for the sensors to report back their positions and
# closest beacons (your puzzle input). For example:

# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3

# So, consider the sensor at 2,18; the closest beacon to it is at -2,15. For the
# sensor at 9,16, the closest beacon to it is at 10,16.

# Drawing sensors as S and beacons as B, the above arrangement of sensors and
# beacons looks like this:

#                1    1    2    2
#      0    5    0    5    0    5
#  0 ....S.......................
#  1 ......................S.....
#  2 ...............S............
#  3 ................SB..........
#  4 ............................
#  5 ............................
#  6 ............................
#  7 ..........S.......S.........
#  8 ............................
#  9 ............................
# 10 ....B.......................
# 11 ..S.........................
# 12 ............................
# 13 ............................
# 14 ..............S.......S.....
# 15 B...........................
# 16 ...........SB...............
# 17 ................S..........B
# 18 ....S.......................
# 19 ............................
# 20 ............S......S........
# 21 ............................
# 22 .......................B....

# This isn't necessarily a comprehensive map of all beacons in the area, though.
# Because each sensor only identifies its closest beacon, if a sensor detects a
# beacon, you know there are no other beacons that close or closer to that
# sensor. There could still be beacons that just happen to not be the closest
# beacon to any sensor. Consider the sensor at 8,7:

#                1    1    2    2
#      0    5    0    5    0    5
# -2 ..........#.................
# -1 .........###................
#  0 ....S...#####...............
#  1 .......#######........S.....
#  2 ......#########S............
#  3 .....###########SB..........
#  4 ....#############...........
#  5 ...###############..........
#  6 ..#################.........
#  7 .#########S#######S#........
#  8 ..#################.........
#  9 ...###############..........
# 10 ....B############...........
# 11 ..S..###########............
# 12 ......#########.............
# 13 .......#######..............
# 14 ........#####.S.......S.....
# 15 B........###................
# 16 ..........#SB...............
# 17 ................S..........B
# 18 ....S.......................
# 19 ............................
# 20 ............S......S........
# 21 ............................
# 22 .......................B....

# This sensor's closest beacon is at 2,10, and so you know there are no beacons
# that close or closer (in any positions marked #).

# None of the detected beacons seem to be producing the distress signal, so
# you'll need to work out where the distress beacon is by working out where it
# isn't. For now, keep things simple by counting the positions where a beacon
# cannot possibly be along just a single row.

# So, suppose you have an arrangement of beacons and sensors like in the example
# above and, just in the row where y=10, you'd like to count the number of
# positions a beacon cannot possibly exist. The coverage from all sensors near
# that row looks like this:

#                  1    1    2    2
#        0    5    0    5    0    5
#  9 ...#########################...
# 10 ..####B######################..
# 11 .###S#############.###########.

# In this example, in the row where y=10, there are 26 positions where a beacon
# cannot be present.

# Consult the report from the sensors you just deployed. In the row where
# y=2000000, how many positions cannot contain a beacon?

# --- Part Two ---

# Your handheld device indicates that the distress signal is coming from a
# beacon nearby. The distress beacon is not detected by any sensor, but the
# distress beacon must have x and y coordinates each no lower than 0 and no
# larger than 4000000.

# To isolate the distress beacon's signal, you need to determine its tuning
# frequency, which can be found by multiplying its x coordinate by 4000000 and
# then adding its y coordinate.

# In the example above, the search space is smaller: instead, the x and y
# coordinates can each be at most 20. With this reduced search area, there is
# only a single position that could have a beacon: x=14, y=11. The tuning
# frequency for this distress beacon is 56000011.

# Find the only possible position for the distress beacon. What is its tuning
# frequency?

import sys
import re
import math
from scipy.spatial.distance import cityblock

def main( argv ):

    with open( "input/day15-input.txt" ) as f:
        data = f.readlines()

    #data = [ 'Sensor at x=2, y=18: closest beacon is at x=-2, y=15',
    #         'Sensor at x=9, y=16: closest beacon is at x=10, y=16',
    #         'Sensor at x=13, y=2: closest beacon is at x=15, y=3',
    #         'Sensor at x=12, y=14: closest beacon is at x=10, y=16',
    #         'Sensor at x=10, y=20: closest beacon is at x=10, y=16',
    #         'Sensor at x=14, y=17: closest beacon is at x=10, y=16',
    #         'Sensor at x=8, y=7: closest beacon is at x=2, y=10',
    #         'Sensor at x=2, y=0: closest beacon is at x=2, y=10',
    #         'Sensor at x=0, y=11: closest beacon is at x=2, y=10',
    #         'Sensor at x=20, y=14: closest beacon is at x=25, y=17',
    #         'Sensor at x=17, y=20: closest beacon is at x=21, y=22',
    #         'Sensor at x=16, y=7: closest beacon is at x=15, y=3',
    #         'Sensor at x=14, y=3: closest beacon is at x=15, y=3',
    #         'Sensor at x=20, y=1: closest beacon is at x=15, y=3' ]

    # For each sensor/beacon pair compute the manhattan distance
    dist = []

    for line in data:
        line = re.split( ' |, |: ', line )
        xy1 = [ int( line[ 2 ].split( '=' )[ 1 ] ), int( line[ 3 ].split( '=' )[ 1 ] ) ]
        xy2 = [ int( line[ 8 ].split( '=' )[ 1 ] ), int( line[ 9 ].split( '=' )[ 1 ] ) ]

        dist.append( [ xy1, cityblock( xy1, xy2 ) ] ) 

    ##
    # Part 1
    ##

    #tgtRow = 10
    tgtRow = 2000000
 
    segments = getSegments( dist, tgtRow )

    # We make an important assumption here:  There are no gaps between line segments.
    # For part 1 this is okay, for part 2 we are specifically looking for a gap.
    minX = 0
    maxX = 0

    for seg in segments:
        if seg[ 0 ] < minX:
            minX = seg[ 0 ]
        if seg[ 1 ] > maxX:
            maxX = seg[ 1 ]

    print( f"Part 1 answer: {maxX - minX}" )


    ## 
    # Part 2
    #

    # So the below works but there are a few comments:
    # I adapetd the segment merging code from something someone posted on the internet.  
    # it could use some retooling to better fit my application.  Also, mRanges doesn't seems to be 
    # hitting each y coord twice?  I thnk I'm not bailing out of the nested loops right.
    # rangeOverlap does not take into account segments perfectly butted together, i handleded this
    # via a special case when iterating thru mRanges...not great.

    #maxCoord = 20
    maxCoord = 4000000
    bx = -1
    by = -1

    for y in range( maxCoord ):
        segments = getSegments( dist, y )
        ranges = [ range( start.astype(int), stop.astype(int) ) for start, stop in segments ]

        rCopy = sorted( ranges.copy(), key=lambda x: x.stop )
        rCopy = sorted( rCopy, key=lambda x: x.start )
        mRanges = []

        while rCopy:
            r1 = rCopy.copy()[ 0 ]
            del rCopy[ 0 ]

            merges = []

            for i, r2 in enumerate( rCopy ):
                if rangeOverlap( r1, r2 ):
                    r1 = range( min( [r1.start, r2.start] ), max( [r1.stop, r2.stop] ) )
                    merges.append( i )

            mRanges.append( r1 )

            for i in reversed( merges ):
                del rCopy[ i ]

        # Fix stuff here:
        for r in mRanges:
            if len( mRanges ) > 1 and mRanges[ 1 ].start - mRanges[ 0 ].stop > 1:
                bx = mRanges[ 0 ].stop + 1
                by = y
                break

    print( f"Part 2 answer: {(bx * 4000000) + by}" )

def rangeOverlap( r1, r2 ):
    if r1.start <= r2.stop and r2.start <= r1.stop:
        return True

    return False

def getSegments( dist, tgt ):
    segments = [] # Horizontal segments on target row

    for xy1, d in dist:
        if xy1[ 1 ] > tgt and xy1[ 1 ] - d <= tgt: # Sensor below target row
            width = (2*d - 2*(xy1[ 1 ] - tgt)) / 2
            segments.append( [ xy1[ 0 ] - width, xy1[ 0 ] + width ] )

        elif xy1[ 1 ] < tgt and xy1[ 1 ] + d >= tgt : # Sesor below target row
            width = (2*d - 2*(tgt - xy1[ 1 ])) / 2
            segments.append( [ xy1[ 0 ] - width, xy1[ 0 ] + width ] )

        elif xy1[ 1 ] == tgt: # Sensor on target row
            segments.append( [ xy1[ 0 ] - d, xy1[ 0 ] + d ] ) # 2x distance

    return segments

if __name__ == "__main__":
    main( argv=sys.argv )