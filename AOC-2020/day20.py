# --- Day 20: Jurassic Jigsaw ---

# The high-speed train leaves the forest and quickly carries you south. You can
# even see a desert in the distance! Since you have some spare time, you might
# as well see if there was anything interesting in the image the Mythical
# Information Bureau satellite captured.

# After decoding the satellite messages, you discover that the data actually
# contains many small images created by the satellite's camera array. The camera
# array consists of many cameras; rather than produce a single square image,
# they produce many smaller square image tiles that need to be reassembled back
# into a single image.

# Each camera in the camera array returns a single monochrome image tile with a
# random unique ID number. The tiles (your puzzle input) arrived in a random
# order.

# Worse yet, the camera array appears to be malfunctioning: each image tile has
# been rotated and flipped to a random orientation. Your first task is to
# reassemble the original image by orienting the tiles so they fit together.

# To show how the tiles should be reassembled, each tile's image data includes a
# border that should line up exactly with its adjacent tiles. All tiles have
# this border, and the border lines up exactly when the tiles are both oriented
# correctly. Tiles at the edge of the image also have this border, but the
# outermost edges won't line up with any other tiles.

# For example, suppose you have the following nine tiles:

# Tile 2311:
# ..##.#..#.
# ##..#.....
# #...##..#.
# ####.#...#
# ##.##.###.
# ##...#.###
# .#.#.#..##
# ..#....#..
# ###...#.#.
# ..###..###

# Tile 1951:
# #.##...##.
# #.####...#
# .....#..##
# #...######
# .##.#....#
# .###.#####
# ###.##.##.
# .###....#.
# ..#.#..#.#
# #...##.#..

# Tile 1171:
# ####...##.
# #..##.#..#
# ##.#..#.#.
# .###.####.
# ..###.####
# .##....##.
# .#...####.
# #.##.####.
# ####..#...
# .....##...

# Tile 1427:
# ###.##.#..
# .#..#.##..
# .#.##.#..#
# #.#.#.##.#
# ....#...##
# ...##..##.
# ...#.#####
# .#.####.#.
# ..#..###.#
# ..##.#..#.

# Tile 1489:
# ##.#.#....
# ..##...#..
# .##..##...
# ..#...#...
# #####...#.
# #..#.#.#.#
# ...#.#.#..
# ##.#...##.
# ..##.##.##
# ###.##.#..

# Tile 2473:
# #....####.
# #..#.##...
# #.##..#...
# ######.#.#
# .#...#.#.#
# .#########
# .###.#..#.
# ########.#
# ##...##.#.
# ..###.#.#.

# Tile 2971:
# ..#.#....#
# #...###...
# #.#.###...
# ##.##..#..
# .#####..##
# .#..####.#
# #..#.#..#.
# ..####.###
# ..#.#.###.
# ...#.#.#.#

# Tile 2729:
# ...#.#.#.#
# ####.#....
# ..#.#.....
# ....#..#.#
# .##..##.#.
# .#.####...
# ####.#.#..
# ##.####...
# ##..#.##..
# #.##...##.

# Tile 3079:
# #.#.#####.
# .#..######
# ..#.......
# ######....
# ####.#..#.
# .#...#.##.
# #.#####.##
# ..#.###...
# ..#.......
# ..#.###...

# By rotating, flipping, and rearranging them, you can find a square arrangement
# that causes all adjacent borders to line up:

# #...##.#.. ..###..### #.#.#####.
# ..#.#..#.# ###...#.#. .#..######
# .###....#. ..#....#.. ..#.......
# ###.##.##. .#.#.#..## ######....
# .###.##### ##...#.### ####.#..#.
# .##.#....# ##.##.###. .#...#.##.
# #...###### ####.#...# #.#####.##
# .....#..## #...##..#. ..#.###...
# #.####...# ##..#..... ..#.......
# #.##...##. ..##.#..#. ..#.###...

# #.##...##. ..##.#..#. ..#.###...
# ##..#.##.. ..#..###.# ##.##....#
# ##.####... .#.####.#. ..#.###..#
# ####.#.#.. ...#.##### ###.#..###
# .#.####... ...##..##. .######.##
# .##..##.#. ....#...## #.#.#.#...
# ....#..#.# #.#.#.##.# #.###.###.
# ..#.#..... .#.##.#..# #.###.##..
# ####.#.... .#..#.##.. .######...
# ...#.#.#.# ###.##.#.. .##...####

# ...#.#.#.# ###.##.#.. .##...####
# ..#.#.###. ..##.##.## #..#.##..#
# ..####.### ##.#...##. .#.#..#.##
# #..#.#..#. ...#.#.#.. .####.###.
# .#..####.# #..#.#.#.# ####.###..
# .#####..## #####...#. .##....##.
# ##.##..#.. ..#...#... .####...#.
# #.#.###... .##..##... .####.##.#
# #...###... ..##...#.. ...#..####
# ..#.#....# ##.#.#.... ...##.....

# For reference, the IDs of the above tiles are:

# 1951    2311    3079
# 2729    1427    2473
# 2971    1489    1171

# To check that you've assembled the image correctly, multiply the IDs of the
# four corner tiles together. If you do this with the assembled tiles from the
# example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.

# Assemble the tiles into an image. What do you get if you multiply together the
# IDs of the four corner tiles?

# --- Part Two ---

# Now, you're ready to check the image for sea monsters.

# The borders of each tile are not part of the actual image; start by removing
# them.

# In the example above, the tiles become:

# .#.#..#. ##...#.# #..#####
# ###....# .#....#. .#......
# ##.##.## #.#.#..# #####...
# ###.#### #...#.## ###.#..#
# ##.#.... #.##.### #...#.##
# ...##### ###.#... .#####.#
# ....#..# ...##..# .#.###..
# .####... #..#.... .#......

# #..#.##. .#..###. #.##....
# #.####.. #.####.# .#.###..
# ###.#.#. ..#.#### ##.#..##
# #.####.. ..##..## ######.#
# ##..##.# ...#...# .#.#.#..
# ...#..#. .#.#.##. .###.###
# .#.#.... #.##.#.. .###.##.
# ###.#... #..#.##. ######..

# .#.#.### .##.##.# ..#.##..
# .####.## #.#...## #.#..#.#
# ..#.#..# ..#.#.#. ####.###
# #..####. ..#.#.#. ###.###.
# #####..# ####...# ##....##
# #.##..#. .#...#.. ####...#
# .#.###.. ##..##.. ####.##.
# ...###.. .##...#. ..#..###

# Remove the gaps to form the actual image:

# .#.#..#.##...#.##..#####
# ###....#.#....#..#......
# ##.##.###.#.#..######...
# ###.#####...#.#####.#..#
# ##.#....#.##.####...#.##
# ...########.#....#####.#
# ....#..#...##..#.#.###..
# .####...#..#.....#......
# #..#.##..#..###.#.##....
# #.####..#.####.#.#.###..
# ###.#.#...#.######.#..##
# #.####....##..########.#
# ##..##.#...#...#.#.#.#..
# ...#..#..#.#.##..###.###
# .#.#....#.##.#...###.##.
# ###.#...#..#.##.######..
# .#.#.###.##.##.#..#.##..
# .####.###.#...###.#..#.#
# ..#.#..#..#.#.#.####.###
# #..####...#.#.#.###.###.
# #####..#####...###....##
# #.##..#..#...#..####...#
# .#.###..##..##..####.##.
# ...###...##...#...#..###

# Now, you're ready to search for sea monsters! Because your image is
# monochrome, a sea monster will look like this:

#                   # 
# #    ##    ##    ###
#  #  #  #  #  #  #   

# When looking for this pattern in the image, the spaces can be anything; only
# the # need to match. Also, you might need to rotate or flip your image before
# it's oriented correctly to find sea monsters. In the above image, after
# flipping and rotating it to the appropriate orientation, there are two sea
# monsters (marked with O):

# .####...#####..#...###..
# #####..#..#.#.####..#.#.
# .#.#...#.###...#.##.O#..
# #.O.##.OO#.#.OO.##.OOO##
# ..#O.#O#.O##O..O.#O##.##
# ...#.#..##.##...#..#..##
# #.##.#..#.#..#..##.#.#..
# .###.##.....#...###.#...
# #.####.#.#....##.#..#.#.
# ##...#..#....#..#...####
# ..#.##...###..#.#####..#
# ....#.##.#.#####....#...
# ..##.##.###.....#.##..#.
# #...#...###..####....##.
# .#.##...#.##.#.#.###...#
# #.###.#..####...##..#...
# #.###...#.##...#.##O###.
# .O##.#OO.###OO##..OOO##.
# ..O#.O..O..O.#O##O##.###
# #.#..##.########..#..##.
# #.#####..#.#...##..#....
# #....##..#.#########..##
# #...#.....#..##...###.##
# #..###....##.#...##.##.#

# Determine how rough the waters are in the sea monsters' habitat by counting
# the number of # that are not part of a sea monster. In the above example, the
# habitat's water roughness is 273.

# How many # are not part of a sea monster?

# This was brutal.  Got it working but probably not the most efficient way and
# a lot of code could be refactored to take better advantage of code reuse.

import sys 
import math
from itertools import combinations 
from scipy.signal import convolve2d
import numpy as np

def main( argv ):

    # Read in input file
    with open( "input/day20-input.txt", "r" ) as f:
        data = [ line.rstrip() for line in f ]

    # Create the tiles
    tiles = []

    for line in data:
        if 'Tile' in line:
            tile = Tile( int( line.split()[ 1 ][ :-1 ] ) )
            tiles.append( tile )

        elif line != '':
            tile.addData( line )

    # Work out for each tile which adjacent tiles it matches with
    for c in combinations( tiles, 2 ):
        c[ 0 ].checkTile( c[ 1 ] )

    # Now the ugly part...

    # Allocate a puzzle board
    dim = int( math.sqrt( len( tiles ) ) )
    puzzle = [ [ None for j in range( dim ) ] for i in range( dim ) ]

    # Find a tile that will fit in the top right.  As we use a tile we'll remove it
    # from the tile list and add it to the puzzle board.
    for t in tiles:
        if t.countConnections() == 2 and t.hasAdjacent():
            # Rotate to correct orentation (tile to east and south)
            if t.north and t.east:
                t.rotate()

            elif t.west and t.south:
                t.flipX()

            elif t.west and t.north:
                t.flipX()
                t.rotate()

            puzzle[ 0 ][ 0 ] = t

            break

    # Now, for each placed tile fill in the tiles it connects to
    for i in range( dim ):
        for j in range( dim ):
            curTile = puzzle[ i ][ j ]

            # Always assume curTile is correct.  We only need to check east and south directions.
            if curTile.east:
                # Rotate/flip the west tile until it lines up
                if curTile.east.west != curTile:
                    curTile.east.rotate()
                
                    if curTile.east.west != curTile:
                        curTile.east.flipX()

                        if curTile.east.west != curTile:
                            curTile.east.rotate()

                            if curTile.east.west != curTile:
                                print( "This should never happen!" )
                                return 1
                
                # Flip if necessary
                if (curTile.east.south == None) and (i != (dim - 1)):
                    curTile.east.flipY()

                puzzle[ i ][ j+1 ] = curTile.east

            if curTile.south:
                # Rotate/flip the south tile until it lines up
                if curTile.south.north != curTile:
                    curTile.south.rotate()

                    if curTile.south.north != curTile:
                        curTile.south.flipY()

                        if curTile.south.north != curTile:
                            curTile.south.rotate()

                            if curTile.south.north != curTile:
                                print( "This should never happen!" )
                                return 1

                # Flip if necessary
                if (curTile.south.east == None) and (j != (dim - 1)):
                    curTile.south.flipX()

                puzzle[ i+1 ][ j ] = curTile.south

    # In theory we should have a completed puzzle now.  
    
    ans = (puzzle[ 0 ][ 0 ].id *
          puzzle[ dim - 1 ][ 0 ].id *
          puzzle[ 0 ][ dim - 1 ].id *
          puzzle[ dim - 1 ][ dim - 1 ].id)

    print( "Part 1 answer: %s" % ans )

    # Init our output array (uncomment to re-add border and dividing lines)
    ##puzDisp = [ [] for i in range( dim * 13 ) ] 
    puzDisp = [ [] for i in range( dim * 8 ) ] 

    #Append each piece 
    for y in range( dim ):
        for x in range( dim ):
            t = puzzle[ y ][ x ] # tile
        
            ##for pLine, tLine in zip( puzDisp[ y*11:(y*11)+11 ], t.data ):
            for pLine, tLine, in zip( puzDisp[ (y*8):(y*8)+8 ], t.data[ 1:-1 ] ):
                pLine += tLine[ 1:-1 ]
                ##pLine += tLine
                ##pLine += ['|']

            ##puzDisp[ (y*11)+10 ] += [ '-' for z in range( 11 ) ]

    # Attempt to print
    #print( '\n'.join( ''.join( i ) for i in puzDisp ) )

    # Time to search for sea monsters.
    found = findMonsters( puzDisp )

    # Now total up the number of '#' tiles minus (found * 15)
    ans = sum( x.count( '#' ) for x in puzDisp ) - (found * 15)
    
    print( "Part 2 answer: %s" % ans )

def findMonsters( puzzle ):
    # Our convolution kernel.  If counts == 15 then we have a hit
    kernel = np.array( [ [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0 ],
                         [ 1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,0 ],
                         [ 0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0 ] ] )

    # Replace characters with numbers in our puzzle
    puzTemp = np.array( puzzle )
    puzTemp[ puzTemp == '.' ] = 0
    puzTemp[ puzTemp == '#' ] = 1
    puzTemp = puzTemp.astype( np.int )

    # Try all the orientations
    for i in range( 4 ):
        counts = convolve2d( puzTemp, kernel, mode='same' )
        found = np.count_nonzero( counts == 15 )

        if found:
            break
        else:
            puzTemp = np.rot90( puzTemp )

    if not found:
        puzTemp = np.flip( puzTemp, axis=0 )

        for i in range( 4 ):
            counts = convolve2d( puzTemp, kernel, mode='same' )
            found = np.count_nonzero( counts == 15 )

            if found:
                break      

    return found

class Tile( object ):
    def __init__( self, id ):
        self.id = id
        self.data = []
        
        self.north = None
        self.east = None
        self.south = None
        self.west = None

    def __str__( self ):
        return 'ID: %s\n' % self.id + '\n'.join( ''.join( i ) for i in self.data )

    # Check all rotateions of this tile aginst all rotations of a differnet tile
    # and record any matches.
    def checkTile( self, other ):

        #if self.id == 1489 or other.id == 1489:
        #    a = 0

        # East
        if self._checkOtherTile( other ):
            self.east = other
            return # Not best practice but simplifies the flow

        self.rotate()

        # North
        if self._checkOtherTile( other ):
            self.east = other
            return

        self.flipX()

        # South
        if self._checkOtherTile( other ):
            self.east = other
            return

        self.rotate()

        # West
        if self._checkOtherTile( other ):
            self.east = other        

    # Compares the east edge of our tile against the west edge of another in
    # all possible configs for other.
    def _checkOtherTile( self, otherTile ):
        # West
        if self._compareEdge( self.data, otherTile.data ):
            otherTile.west = self
            return True

        otherTile.flipY()

        if self._compareEdge( self.data, otherTile.data ):
            otherTile.west = self
            return True

        otherTile.rotate()

        # South
        if self._compareEdge( self.data, otherTile.data ):
            otherTile.west = self
            return True

        otherTile.flipY()

        if self._compareEdge( self.data, otherTile.data ):
            otherTile.west = self
            return True

        otherTile.flipX()

        # North
        if self._compareEdge( self.data, otherTile.data ):
            otherTile.west = self
            return True

        otherTile.flipY()

        if self._compareEdge( self.data, otherTile.data ):
            otherTile.west = self
            return True

        otherTile.rotate()

        # East
        if self._compareEdge( self.data, otherTile.data ):
            otherTile.west = self
            return True

        otherTile.flipY()

        if self._compareEdge( self.data, otherTile.data ):
            otherTile.west = self
            return True

        return False

    # Compares the east edge of two tiles
    def _compareEdge( self, thisData, otherData ):
        for i, j in zip( thisData, otherData ):
            if i[ -1 ] != j[ 0 ]:
                return False
        else:
            return True

    # Rotate CW
    def rotate( self ):
        self.data = list( zip( *self.data[ ::-1 ] ) )

        # Update links
        oldN = self.north
        oldE = self.east
        oldS = self.south
        oldW = self.west

        self.east = oldN
        self.south = oldE
        self.west = oldS
        self.north = oldW

        return self.data

    def flipX( self ):
        self.data = [ x[ ::-1 ] for x in self.data ]

        # Update links
        oldE = self.east
        oldW = self.west

        self.east = oldW
        self.west = oldE

        return self.data

    def flipY( self ):
        self.data = self.data[ ::-1 ]

        # Update links
        oldN = self.north
        oldS = self.south

        self.north = oldS
        self.south = oldN

        return self.data

    # There is certainly a better way to do this, lambda function or some such.
    def countConnections( self ):
        count = 0

        if self.north:
            count += 1
        if self.east:
            count += 1
        if self.south:
            count += 1
        if self.west:
            count += 1

        return count

    def hasAdjacent( self ):
        if self.north and self.east:
            return True
        elif self.east and self.south:
            return True
        elif self.south and self.west:
            return True
        elif self.west and self.north:
            return True

        return False

    def addData( self, data ):
        self.data.append( list( data ) )

if __name__ == "__main__":
    main( argv=sys.argv )