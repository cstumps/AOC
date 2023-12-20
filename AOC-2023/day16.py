# --- Day 16: The Floor Will Be Lava ---

# With the beam of light completely focused somewhere, the reindeer leads you
# deeper still into the Lava Production Facility. At some point, you realize
# that the steel facility walls have been replaced with cave, and the doorways
# are just cave, and the floor is cave, and you're pretty sure this is actually
# just a giant cave.

# Finally, as you approach what must be the heart of the mountain, you see a
# bright light in a cavern up ahead. There, you discover that the beam of light
# you so carefully focused is emerging from the cavern wall closest to the
# facility and pouring all of its energy into a contraption on the opposite
# side.

# Upon closer inspection, the contraption appears to be a flat, two-dimensional
# square grid containing empty space (.), mirrors (/ and \), and splitters (|
# and -).

# The contraption is aligned so that most of the beam bounces around the grid,
# but each tile on the grid converts some of the beam's light into heat to melt
# the rock in the cavern.

# You note the layout of the contraption (your puzzle input). For example:

# .|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\
# ..../.\\..
# .-.-/..|..
# .|....-|.\
# ..//.|....

# The beam enters in the top-left corner from the left and heading to the right.
# Then, its behavior depends on what it encounters as it moves:

#     If the beam encounters empty space (.), it continues in the same
#     direction.

#     If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees
#     depending on the angle of the mirror. For instance, a rightward-moving
#     beam that encounters a / mirror would continue upward in the mirror's
#     column, while a rightward-moving beam that encounters a \ mirror would
#     continue downward from the mirror's column.

#     If the beam encounters the pointy end of a splitter (| or -), the beam
#     passes through the splitter as if the splitter were empty space. For
#     instance, a rightward-moving beam that encounters a - splitter would
#     continue in the same direction.

#     If the beam encounters the flat side of a splitter (| or -), the beam is
#     split into two beams going in each of the two directions the splitter's
#     pointy ends are pointing. For instance, a rightward-moving beam that
#     encounters a | splitter would split into two beams: one that continues
#     upward from the splitter's column and one that continues downward from the
#     splitter's column.

# Beams do not interact with other beams; a tile can have many beams passing
# through it at the same time. A tile is energized if that tile has at least one
# beam pass through it, reflect in it, or split in it.

# In the above example, here is how the beam of light bounces around the
# contraption:

# >|<<<\....
# |v-.\^....
# .v...|->>>
# .v...v^.|.
# .v...v^...
# .v...v^..\
# .v../2\\..
# <->-/vv|..
# .|<<<2-|.\
# .v//.|.v..

# Beams are only shown on empty tiles; arrows indicate the direction of the
# beams. If a tile contains beams moving in multiple directions, the number of
# distinct directions is shown instead. Here is the same diagram but instead
# only showing whether a tile is energized (#) or not (.):

# ######....
# .#...#....
# .#...#####
# .#...##...
# .#...##...
# .#...##...
# .#..####..
# ########..
# .#######..
# .#...#.#..

# Ultimately, in this example, 46 tiles become energized.

# The light isn't energizing enough tiles to produce lava; to debug the
# contraption, you need to start by analyzing the current situation. With the
# beam starting in the top-left heading right, how many tiles end up being
# energized?

# --- Part Two ---

# As you try to work out what might be wrong, the reindeer tugs on your shirt
# and leads you to a nearby control panel. There, a collection of buttons lets
# you align the contraption so that the beam enters from any edge tile and
# heading away from that edge. (You can choose either of two directions for the
# beam if it starts on a corner; for instance, if the beam starts in the
# bottom-right corner, it can start heading either left or upward.)

# So, the beam could start on any tile in the top row (heading downward), any
# tile in the bottom row (heading upward), any tile in the leftmost column
# (heading right), or any tile in the rightmost column (heading left). To
# produce lava, you need to find the configuration that energizes as many tiles
# as possible.

# In the above example, this can be achieved by starting the beam in the fourth
# tile from the left in the top row:

# .|<2<\....
# |v-v\^....
# .v.v.|->>>
# .v.v.v^.|.
# .v.v.v^...
# .v.v.v^..\
# .v.v/2\\..
# <-2-/vv|..
# .|<<<2-|.\
# .v//.|.v..

# Using this configuration, 51 tiles are energized:

# .#####....
# .#.#.#....
# .#.#.#####
# .#.#.##...
# .#.#.##...
# .#.#.##...
# .#.#####..
# ########..
# .#######..
# .#...#.#..

# Find the initial beam configuration that energizes the largest number of
# tiles; how many tiles are energized in that configuration?

import sys

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day16-input.txt", "r" ) as f:
        data = [ line.rstrip( '\n' ) for line in f ]

    # Had to add extra slashes to sample data so characters are escaped properly
    #data = [ '.|...\....',
    #         '|.-.\.....',
    #         '.....|-...',
    #         '........|.',
    #         '..........',
    #         '.........\\',
    #         '..../.\\\\..',
    #         '.-.-/..|..',
    #         '.|....-|.\\',
    #         '..//.|....' ]

    # Not my best effort but it does work.  Could replace the if/else statments for rotation
    # with a look up table that multiplies by +/- j.  Note that the seenBeams variable being
    # a set is critical.  If it's a list part 2 takes upwards of 15 minutes to run.

    ##
    # Part 1
    ##

    b = Beam( 0, 0, Beam.DIR_RIGHT )
    grid = [ [0] * len( data[ 0 ] ) for i in range( len( data ) ) ]
    runBeam( b, data, grid, set() )

    count = sum( map( sum, grid ) )

    print( f"Part 1 answer: {count}" )

    ##
    # Part 2
    ##

    startBeams = []

    # Left & right side
    for i in range( len( data ) ):
        startBeams.append( Beam( 0, i, Beam.DIR_RIGHT ) )
        startBeams.append( Beam( len( data[ 0 ] ) - 1, i, Beam.DIR_LEFT ) )

    # Top & bottom
    for i in range( len( data[ 0 ] ) ):
        startBeams.append( Beam( i, 0, Beam.DIR_DOWN ) )
        startBeams.append( Beam( i, len( data ) - 1, Beam.DIR_UP ) )

    energy = 0

    for beam in startBeams:
        grid = [ [0] * len( data[ 0 ] ) for i in range( len( data ) ) ]
        runBeam( beam, data, grid, set() )

        energy = max( energy, sum( map( sum, grid ) ) )

    print( f"Part 2 answer: {energy}" )

def runBeam( beam, data, grid, seenBeams ):
    while (beam.pos.real >= 0 and beam.pos.real <= len( data[ 0 ] ) - 1) and (beam.pos.imag >= 0 and beam.pos.imag <= len( data ) - 1):
        grid[ int( beam.pos.imag ) ][ int( beam.pos.real ) ] = 1

        if (beam.pos, beam.dir) in seenBeams:
            break
        else:
            seenBeams.add( (beam.pos, beam.dir) )

        # Rotate
        if data[ int( beam.pos.imag ) ][ int( beam.pos.real ) ] == '\\':
            if beam.dir == Beam.DIR_UP:
                beam.dir = Beam.DIR_LEFT
            elif beam.dir == Beam.DIR_DOWN:
                beam.dir = Beam.DIR_RIGHT
            elif beam.dir == Beam.DIR_LEFT:
                beam.dir = Beam.DIR_UP
            else:
                beam.dir = Beam.DIR_DOWN

        elif data[ int( beam.pos.imag ) ][ int( beam.pos.real ) ] == '/':
            if beam.dir == Beam.DIR_UP:
                beam.dir = Beam.DIR_RIGHT
            elif beam.dir == Beam.DIR_DOWN:
                beam.dir = Beam.DIR_LEFT
            elif beam.dir == Beam.DIR_LEFT:
                beam.dir = Beam.DIR_DOWN
            else:
                beam.dir = Beam.DIR_UP

        # Split 
        elif (beam.dir == Beam.DIR_LEFT or beam.dir == Beam.DIR_RIGHT) and data[ int( beam.pos.imag ) ][ int( beam.pos.real ) ] == '|':
            beam.dir = Beam.DIR_UP
            runBeam( Beam( beam.pos.real, beam.pos.imag, Beam.DIR_DOWN ), data, grid, seenBeams )

        elif (beam.dir == Beam.DIR_UP or beam.dir == Beam.DIR_DOWN) and data[ int( beam.pos.imag ) ][ int( beam.pos.real ) ] == '-':
            beam.dir = Beam.DIR_LEFT
            runBeam( Beam( beam.pos.real, beam.pos.imag, Beam.DIR_RIGHT ), data, grid, seenBeams )

        beam.pos += Beam.moves[ beam.dir ]

class Beam:
    DIR_UP    = 0
    DIR_RIGHT = 1
    DIR_DOWN  = 2
    DIR_LEFT  = 3

    moves = [ complex( 0, -1 ), 
              complex( 1,  0 ), 
              complex( 0,  1 ), 
              complex( -1, 0 ) ]

    def __init__( self, x, y, dir ):
        self.pos = complex( x, y )
        self.dir = dir

    def __eq__( self, other ):
        return (self.pos == other.pos) and (self.dir == other.dir)


if __name__ == "__main__":
    main( argv=sys.argv )