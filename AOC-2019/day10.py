# --- Day 10:
# Monitoring Station ---
#
# You fly into the asteroid belt and reach the Ceres monitoring station. The
# Elves here have an emergency: they're having trouble tracking all of the
# asteroids and can't be sure they're safe.
#
# The Elves would like to build a new monitoring station in a nearby area of
# space; they hand you a map of all of the asteroids in that region (your puzzle
# input).
#
# The map indicates whether each position is empty (.) or contains an asteroid
# (#). The asteroids are much smaller than they appear on the map, and every
# asteroid is exactly in the center of its marked position. The asteroids can be
# described with X,Y coordinates where X is the distance from the left edge and
# Y is the distance from the top edge (so the top-left corner is 0,0 and the
# position immediately to its right is 1,0).
#
# Your job is to figure out which asteroid would be the best place to build a
# new monitoring station. A monitoring station can detect any asteroid to which
# it has direct line of sight - that is, there cannot be another asteroid
# exactly between them. This line of sight can be at any angle, not just lines
# aligned to the grid or diagonally. The best location is the asteroid that can
# detect the largest number of other asteroids.
#
# For example, consider the following map:
#
# .#..#
# .....
# #####
# ....#
# ...##
#
# The best location for a new monitoring station on this map is the highlighted
# asteroid at 3,4 because it can detect 8 asteroids, more than any other
# location. (The only asteroid it cannot detect is the one at 1,0; its view of
# this asteroid is blocked by the asteroid at 2,2.) All other asteroids are
# worse locations; they can detect 7 or fewer other asteroids. Here is the
# number of other asteroids a monitoring station on each asteroid could detect:
#
# .7..7
# .....
# 67775 ....7 ...87
#
# Here is an asteroid (#) and some examples of the ways its line of sight might
# be blocked. If there were another asteroid at the location of a capital
# letter, the locations marked with the corresponding lowercase letter would be
# blocked and could not be detected:
#
# #.........
# ...A...... ...B..a... .EDCG....a ..F.c.b... .....c.... ..efd.c.gb .......c..
# ....f...c. ...e..d..c
#
# Here are some larger examples:
#
#     Best is 5,8 with 33 other asteroids detected:
#
#     ......#.#.
#     #..#.#....
#     ..#######.
#     .#.#.###..
#     .#..#.....
#     ..#....#.#
#     #..#....#.
#     .##.#..###
#     ##...#..#.
#     .#....####
#
#     Best is 1,2 with 35 other asteroids detected:
#
#     #.#...#.#.
#     .###....#.
#     .#....#...
#     ##.#.#.#.#
#     ....#.#.#.
#     .##..###.#
#     ..#...##..
#     ..##....##
#     ......#...
#     .####.###.
#
#     Best is 6,3 with 41 other asteroids detected:
#
#     .#..#..###
#     ####.###.#
#     ....###.#.
#     ..###.##.#
#     ##.##.#.#.
#     ....###..#
#     ..#.#..#.#
#     #..#.#.###
#     .##...##.#
#     .....#.#..
#
#     Best is 11,13 with 210 other asteroids detected:
#
#     .#..##.###...#######
#     ##.############..##.
#     .#.######.########.#
#     .###.#######.####.#.
#     #####.##.#.##.###.##
#     ..#####..#.#########
#     ####################
#     #.####....###.#.#.##
#     ##.#################
#     #####.##.###..####..
#     ..######..##.#######
#     ####.##.####...##..#
#     .#####..#.######.###
#     ##...#.##########...
#     #.##########.#######
#     .####.#.###.###.#.##
#     ....##.##.###..#####
#     .#.#.###########.###
#     #.#.#.#####.####.###
#     ###.##.####.##.#..##
#
# Find the best location for a new monitoring station. How many other asteroids
# can be detected from that location?
#
# --- Part Two ---
#
# Once you give them the coordinates, the Elves quickly deploy an Instant
# Monitoring Station to the location and discover the worst: there are simply
# too many asteroids.
#
# The only solution is complete vaporization by giant laser.
#
# Fortunately, in addition to an asteroid scanner, the new monitoring station
# also comes equipped with a giant rotating laser perfect for vaporizing
# asteroids. The laser starts by pointing up and always rotates clockwise,
# vaporizing any asteroid it hits.
#
# If multiple asteroids are exactly in line with the station, the laser only has
# enough power to vaporize one of them before continuing its rotation. In other
# words, the same asteroids that can be detected can be vaporized, but if
# vaporizing one asteroid makes another one detectable, the newly-detected
# asteroid won't be vaporized until the laser has returned to the same position
# by rotating a full 360 degrees.
#
# For example, consider the following map, where the asteroid with the new
# monitoring station (and laser) is marked X:
#
# .#....#####...#..
# ##...##.#####..##
# ##...#...#.#####.
# ..#.....X...###..
# ..#.#.....#....##
#
# The first nine asteroids to get vaporized, in order, would be:
#
# .#....###24...#.. ##...##.13#67..9# ##...#...5.8####. ..#.....X...###..
# ..#.#.....#....##
#
# Note that some asteroids (the ones behind the asteroids marked 1, 5, and 7)
# won't have a chance to be vaporized until the next full rotation. The laser
# continues rotating; the next nine to be vaporized are:
#
# .#....###.....#..
# ##...##...#.....#
# ##...#......1234. ..#.....X...5##.. ..#.9.....8....76
#
# The next nine to be vaporized are then:
#
# .8....###.....#.. 56...9#...#.....# 34...7........... ..2.....X....##..
# ..1..............
#
# Finally, the laser completes its first full rotation (1 through 3), a second
# rotation (4 through 8), and vaporizes the last asteroid (9) partway through
# its third rotation:
#
# ......234.....6.. ......1...5.....7
# .................
# ........X....89..
# .................
#
# In the large example above (the one with the best monitoring station location
# at 11,13):
#
#     The 1st asteroid to be vaporized is at 11,12.
#     The 2nd asteroid to be vaporized is at 12,1.
#     The 3rd asteroid to be vaporized is at 12,2.
#     The 10th asteroid to be vaporized is at 12,8.
#     The 20th asteroid to be vaporized is at 16,0.
#     The 50th asteroid to be vaporized is at 16,9.
#     The 100th asteroid to be vaporized is at 10,16.
#     The 199th asteroid to be vaporized is at 9,6.
#     The 200th asteroid to be vaporized is at 8,2.
#     The 201st asteroid to be vaporized is at 10,9.
#     The 299th and final asteroid to be vaporized is at 11,1.
#
# The Elves are placing bets on which will be the 200th asteroid to be
# vaporized. Win the bet by determining which asteroid that will be; what do you
# get if you multiply its X coordinate by 100 and then add its Y coordinate?
# (For example, 8,2 becomes 802.)

# This is far and away a terrible solution.  At the very least part 1 should be done similar
# to part 2 where we use polar coords.  Additionally, the Point class functions should be
# cleaned up.

import sys
import math
import itertools as it

def main( argv ):

    data = []
    pList = []

    # Read in input file
    with open( "input/day10-input.txt", "r" ) as f:
        data = f.readlines()

    # data = [ '......#.#.',
    #          '#..#.#....',
    #          '..#######.',
    #          '.#.#.###..',
    #          '.#..#.....',
    #          '..#....#.#',
    #          '#..#....#.',
    #          '.##.#..###',
    #          '##...#..#.',
    #          '.#....####' ]

    # data = [ '.#..#',
    #          '.....',
    #          '#####',
    #          '....#',
    #          '...##' ]

    # data = [ 
    #          '.#..##.###...#######',
    #          '##.############..##.',
    #          '.#.######.########.#',
    #          '.###.#######.####.#.',
    #          '#####.##.#.##.###.##',
    #          '..#####..#.#########',
    #          '####################',
    #          '#.####....###.#.#.##',
    #          '##.#################',
    #          '#####.##.###..####..',
    #          '..######..##.#######',
    #          '####.##.####...##..#',
    #          '.#####..#.######.###',
    #          '##...#.##########...',
    #          '#.##########.#######',
    #          '.####.#.###.###.#.##',
    #          '....##.##.###..#####',
    #          '.#.#.###########.###',
    #          '#.#.#.#####.####.###',
    #          '###.##.####.##.#..##' ]

    for i, line in enumerate( data ):
        for j, point in enumerate( line ):
            if point == '#':
                pList.append( Point( j, i ) )

    losList = []

    # For each origin point
    for point in pList:
        los = 0

        # For each other point
        for p1 in pList:
           # Skip the current origin
            if p1 == point:
               continue

            # Check to see if another point lies on the line
            for p2 in pList:
                blocking = False

                # Skip the current origin and the current test point
                if p2 == point or p2 == p1:
                    continue

                # point = origin = point1
                # p1 = other point defining the line = point2
                # p2 = point to test if also on line = currpoint
                dxc = p2.x - point.x
                dyc = p2.y - point.y

                dxl = p1.x - point.x
                dyl = p1.y - point.y

                cross = dxc * dyl - dyc * dxl

                # If p2 is not on the line, test the next point
                if cross:
                    continue
            
                # p2 is on the line, now see if it's between p1 and the origin
                if abs( dxl ) >= abs( dyl ):
                    if dxl > 0:
                        blocking = (point.x <= p2.x) and (p2.x <= p1.x)
                    else:
                        blocking = (p1.x <= p2.x) and (p2.x <= point.x)

                else:
                    if dyl > 0:
                        blocking = (point.y <= p2.y) and (p2.y <= p1.y)
                    else:
                        blocking = (p1.y <= p2.y) and (p2.y <= point.y)

                # At this point, if blocking is True then we know that p2 lies between
                # p1 and point.  Therefore, p1 is not in line of sight of point.
                if blocking:
                    break
            else:
                # If we went thru the entire list without being blocked, this point
                # is in LOS.
                los += 1

        losList.append( [ point, los ] )

    # At the end.  Print out which point had the most number of other LOS points
    maxPoints = 0
    maxPoint  = None

    for p in losList:
        if p[ 1 ] > maxPoints:
            maxPoints = p[ 1 ]
            maxPoint  = p[ 0 ]

    print( "Part 1: Max LOS at point %s with %s other points" % (maxPoint, maxPoints) )

    # Part 2

    center = Point( maxPoint.x, maxPoint.y )

    for point in pList:
        # Re-orient the points around the center point.  This also updates
        # the polar version.
        point.translate( center )

    # First sort on magnitude
    pList.sort( key=lambda pt: pt.r )

    # Then sort on theta
    pList.sort( key=lambda pt: pt.theta )

    # Now iterate thru the list until we hit the 200th asteroid
    astCount = 0
    lastPoint = None
    delList = []

    while astCount != 200:
        for pt in pList:
            # If we've hit our 200th, we're done
            if astCount == 200:
                break

            # Only one angle entry on a pass through
            if (lastPoint != None) and (pt.theta == lastPoint.theta):
                continue

            lastPoint = pt
            astCount += 1

            delList.append( pt )

        # Sync the lists
        pList = set( pList ) - set( delList )
        delList = []

    answer = (lastPoint.origX * 100) + lastPoint.origY
    print( "Part 2: 200th asteroid at (%s,%s) = %s" % (lastPoint.origX, lastPoint.origY, answer))

    return 0

class Point( object ):
    def __init__( self, x, y ):
        self.x = float( x )
        self.y = float( y )

        # Cheap but store off original loc for answer
        self.origX = self.x
        self.origY = self.y

        self._convertPolar()

    def __str__( self ):
        return "(%s, %s)" % (self.x, self.y)

    def __eq__( self, other ):
        if isinstance( other, self.__class__ ):
            return (self.x == other.x) and (self.y == other.y)
        else:
            return False

    def __hash__( self ):
        return hash( (self.x, self.y) )

    # Move point and re-orient such that 0 is up
    def translate( self, p ):
        self.x = (p.x - self.x)
        self.y = (p.y - self.y)

        # CW rotation 90 degrees
        oldX = self.x
        self.x = self.y
        self.y = -oldX

        self._convertPolar()

    # Update the polar coords of this point
    def _convertPolar( self ):
        self.r = math.sqrt( (self.x ** 2) + (self.y ** 2) )
        self.theta = math.degrees( math.atan2( self.y, self.x ) ) % 360
        
if __name__ == "__main__":
    main( argv=sys.argv )