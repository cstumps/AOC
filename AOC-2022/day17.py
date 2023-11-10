# --- Day 17: Pyroclastic Flow ---

# Your handheld device has located an alternative exit from the cave for you and
# the elephants. The ground is rumbling almost continuously now, but the strange
# valves bought you some time. It's definitely getting warmer in here, though.

# The tunnels eventually open into a very tall, narrow chamber. Large,
# oddly-shaped rocks are falling into the chamber from above, presumably due to
# all the rumbling. If you can't work out where the rocks will fall next, you
# might be crushed!

# The five types of rocks have the following peculiar shapes, where # is rock
# and . is empty space:

# ####

# .#.
# ###
# .#.

# ..#
# ..#
# ###

# #
# #
# #
# #

# ##
# ##

# The rocks fall in the order shown above: first the - shape, then the + shape,
# and so on. Once the end of the list is reached, the same order repeats: the -
# shape falls first, sixth, 11th, 16th, etc.

# The rocks don't spin, but they do get pushed around by jets of hot gas coming
# out of the walls themselves. A quick scan reveals the effect the jets of hot
# gas will have on the rocks as they fall (your puzzle input).

# For example, suppose this was the jet pattern in your cave:

# >>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>

# In jet patterns, < means a push to the left, while > means a push to the
# right. The pattern above means that the jets will push a falling rock right,
# then right, then right, then left, then left, then right, and so on. If the
# end of the list is reached, it repeats.

# The tall, vertical chamber is exactly seven units wide. Each rock appears so
# that its left edge is two units away from the left wall and its bottom edge is
# three units above the highest rock in the room (or the floor, if there isn't
# one).

# After a rock appears, it alternates between being pushed by a jet of hot gas
# one unit (in the direction indicated by the next symbol in the jet pattern)
# and then falling one unit down. If any movement would cause any part of the
# rock to move into the walls, floor, or a stopped rock, the movement instead
# does not occur. If a downward movement would have caused a falling rock to
# move into the floor or an already-fallen rock, the falling rock stops where it
# is (having landed on something) and a new rock immediately begins falling.

# Drawing falling rocks with @ and stopped rocks with #, the jet pattern in the
# example above manifests as follows:

# The first rock begins falling:
# |..@@@@.|
# |.......|
# |.......|
# |.......|
# +-------+

# Jet of gas pushes rock right:
# |...@@@@|
# |.......|
# |.......|
# |.......|
# +-------+

# Rock falls 1 unit:
# |...@@@@|
# |.......|
# |.......|
# +-------+

# Jet of gas pushes rock right, but nothing happens:
# |...@@@@|
# |.......|
# |.......|
# +-------+

# Rock falls 1 unit:
# |...@@@@|
# |.......|
# +-------+

# Jet of gas pushes rock right, but nothing happens:
# |...@@@@|
# |.......|
# +-------+

# Rock falls 1 unit:
# |...@@@@|
# +-------+

# Jet of gas pushes rock left:
# |..@@@@.|
# +-------+

# Rock falls 1 unit, causing it to come to rest:
# |..####.|
# +-------+

# A new rock begins falling:
# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |.......|
# |.......|
# |..####.|
# +-------+

# Jet of gas pushes rock left:
# |..@....|
# |.@@@...|
# |..@....|
# |.......|
# |.......|
# |.......|
# |..####.|
# +-------+

# Rock falls 1 unit:
# |..@....|
# |.@@@...|
# |..@....|
# |.......|
# |.......|
# |..####.|
# +-------+

# Jet of gas pushes rock right:
# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |.......|
# |..####.|
# +-------+

# Rock falls 1 unit:
# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |..####.|
# +-------+

# Jet of gas pushes rock left:
# |..@....|
# |.@@@...|
# |..@....|
# |.......|
# |..####.|
# +-------+

# Rock falls 1 unit:
# |..@....|
# |.@@@...|
# |..@....|
# |..####.|
# +-------+

# Jet of gas pushes rock right:
# |...@...|
# |..@@@..|
# |...@...|
# |..####.|
# +-------+

# Rock falls 1 unit, causing it to come to rest:
# |...#...|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# A new rock begins falling:
# |....@..|
# |....@..|
# |..@@@..|
# |.......|
# |.......|
# |.......|
# |...#...|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# The moment each of the next few rocks begins falling, you would see this:

# |..@....|
# |..@....|
# |..@....|
# |..@....|
# |.......|
# |.......|
# |.......|
# |..#....|
# |..#....|
# |####...|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@@...|
# |..@@...|
# |.......|
# |.......|
# |.......|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@@@@.|
# |.......|
# |.......|
# |.......|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |.......|
# |.......|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |....@..|
# |....@..|
# |..@@@..|
# |.......|
# |.......|
# |.......|
# |..#....|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@....|
# |..@....|
# |..@....|
# |..@....|
# |.......|
# |.......|
# |.......|
# |.....#.|
# |.....#.|
# |..####.|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@@...|
# |..@@...|
# |.......|
# |.......|
# |.......|
# |....#..|
# |....#..|
# |....##.|
# |....##.|
# |..####.|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@@@@.|
# |.......|
# |.......|
# |.......|
# |....#..|
# |....#..|
# |....##.|
# |##..##.|
# |######.|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# To prove to the elephants your simulation is accurate, they want to know how
# tall the tower will get after 2022 rocks have stopped (but before the 2023rd
# rock begins falling). In this example, the tower of rocks will be 3068 units
# tall.

# How many units tall will the tower of rocks be after 2022 rocks have stopped
# falling?

# --- Part Two ---

# The elephants are not impressed by your simulation. They demand to know how
# tall the tower will be after 1000000000000 rocks have stopped! Only then will
# they feel confident enough to proceed through the cave.

# In the example above, the tower would be 1514285714288 units tall!

# How tall will the tower be after 1000000000000 rocks have stopped?

import sys
import math

def main( argv ):

    with open( "input/day17-input.txt" ) as f:
        data = f.readline().strip()

    data = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

    ##
    # Part 1
    ##

    val, _ = runGame( data, 2022 )
    print( f"Part 1 answer: {val}" )

    ## 
    # Part 2
    ##

    # Get enough of a sample that we think we might have a cycle present
    print()
    print( "Beginning part 2.  Running 10000 blocks." )

    val, actions = runGame( data, 10000 )

    print( "Complete, looking for cycle..." )

    # Now take the list of actions and see if we can find a cycle
    cycleSize, cycleStart = findCycles( actions )

    print( f"Found cycle of length {cycleSize} starting at {cycleStart}" )
    
    # Figure out how much height each complete cycle creates by computing everything before the first
    # cycle and subtracting that from the start + the first cycle
    startHeight, _ = runGame( data, cycleStart )
    startPlusCycle, _ = runGame( data, cycleStart + cycleSize )

    cycleHeight = startPlusCycle - startHeight

    # Compute how many full cycles we have and how many blocks are in the final partial cycle
    wholeCycles = math.floor( (1000000000000 - cycleStart) / cycleSize )
    partialSize = (1000000000000 - cycleStart) % cycleSize

    # Run the start + the first cycle + the last cycle because the last cycle will not be starting
    # on a flat floor like the first rock to fall will.
    truncatedRun, _ = runGame( data, cycleStart + cycleSize + partialSize )

    # The total height will be the truncated run + the remaining cycles/heights
    totalHeight = truncatedRun + ((wholeCycles - 1) * cycleHeight)

    print( f"Part 2 answer: {totalHeight}" )


def findCycles( actions ):
    for i, a in enumerate( actions ):
        try:
            ind = actions.index( a, i+1 )
        except ValueError:
            continue

        c = countCycle( actions[ i:ind ], actions[ ind: ] )

        if c > 10:
            return c, i
            

def countCycle( l1, l2 ):
    count = 0

    for e1, e2 in zip( l1, l2 ):
        if e1 == e2:
            count += 1
        else:
            break

    return count

def runGame( data, count ):
    width = 7
    height = 7
    move = 0

    actions = []

    game = Tetris( height, width )
    game.nextBlock()

    for i in range( count ):
        moves = ''                # The string of moves associated with this block
        act = [ game.block.type ] # The block associated with this string of moves

        while game.block != None:
            if data[ move ] == '>':
                game.moveSide( 1 )
            else:
                game.moveSide( -1 )

            moves += data[ move ]

            game.moveDown()
            move = (move + 1) % len( data )

        act.append( moves )
        actions.append( act )

        game.nextBlock()

    return game.height - height, actions

# Going to be perfectly honest and say that this code was adapted from some other
# tetris implementation due to time contraints.

class Block:

    #  0  1  2  3
    #  4  5  6  7
    #  8  9 10 11
    # 12 13 14 15

    shapes = [ [ 12, 13, 14, 15 ],
               [ 5, 8, 9, 10, 13 ],
               [ 6, 10, 14, 13, 12 ],
               [ 0, 4, 8, 12 ],
               [ 8, 9, 12, 13 ] ]

    def __init__( self, x, y, n ):
        self.x = x
        self.y = y
        self.type = n
    
    def getShape( self ):
        return Block.shapes[ self.type ]

class Tetris:
    def __init__( self, height, width ):
        self.height = height
        self.width = width
        self.field = []
        self.blockNum = 0
        self.block = None

        for i in range( height ):
            line = []

            for j in range( width ):
                line.append( '.' )

            self.field.append( line )

    def __str__( self ):
        s = ''

        for j in range( self.height ):
            s += ''.join( self.field[ j ] ) + '\n'

        s += ''.join( [ '#' for i in range( self.width ) ] ) + '\n'

        return s


    def nextBlock( self ):
        height = 0

        # Find the current height of the field and increase if we're not tall enough
        for j in range( self.height ):
            if '#' in self.field[ j ]:
                height = j

                if height < 7:
                    for i in range( 7 - height ):
                        self.field.insert( 0, [ '.' for i in range( self.width ) ] )
                        self.height += 1

        self.block = Block( 2, 0, self.blockNum )
        self.blockNum = (self.blockNum + 1) % len( Block.shapes )

    def intersects( self ):
        intersection = False

        for i in range( 4 ):
            for j in range( 4 ):
                if i * 4 + j in self.block.getShape():
                    if i + self.block.y > self.height - 1 or \
                        j + self.block.x > self.width - 1 or \
                        j + self.block.x < 0 or \
                        self.field[ i + self.block.y ][ j + self.block.x ] == '#':
                        intersection = True

        return intersection

    def moveDown( self ):
        self.block.y += 1
        
        if self.intersects():
            self.block.y -= 1
            self.freeze()

    def moveSide( self, dx ):
        oldX = self.block.x
        self.block.x += dx

        if self.intersects():
            self.block.x = oldX

    def freeze( self ):
        for i in range( 4 ):
            for j in range( 4 ):
                if i * 4 + j in self.block.getShape():
                    self.field[ i + self.block.y ][ j + self.block.x ] = '#'

        self.block = None

if __name__ == "__main__":
    main( argv=sys.argv )