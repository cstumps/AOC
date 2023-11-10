# --- Day 13: Care Package ---
#
# As you ponder the solitude of space and the ever-increasing three-hour
# roundtrip for messages between you and Earth, you notice that the Space Mail
# Indicator Light is blinking. To help keep you sane, the Elves have sent you a
# care package.
#
# It's a new game for the ship's arcade cabinet! Unfortunately, the arcade is
# all the way on the other end of the ship. Surely, it won't be hard to build
# your own - the care package even comes with schematics.
#
# The arcade cabinet runs Intcode software like the game the Elves sent (your
# puzzle input). It has a primitive screen capable of drawing square tiles on a
# grid. The software draws tiles to the screen with output instructions: every
# three output instructions specify the x position (distance from the left), y
# position (distance from the top), and tile id. The tile id is interpreted as
# follows:
#
#     0 is an empty tile. No game object appears in this tile.
#     1 is a wall tile. Walls are indestructible barriers.
#     2 is a block tile. Blocks can be broken by the ball.
#     3 is a horizontal paddle tile. The paddle is indestructible.
#     4 is a ball tile. The ball moves diagonally and bounces off objects.
#
# For example, a sequence of output values like 1,2,3,6,5,4 would draw a
# horizontal paddle tile (1 tile from the left and 2 tiles from the top) and a
# ball tile (6 tiles from the left and 5 tiles from the top).
#
# Start the game. How many block tiles are on the screen when the game exits?
# 
# --- Part Two ---
#
# The game didn't run because you didn't put in any quarters. Unfortunately, you
# did not bring any quarters. Memory address 0 represents the number of quarters
# that have been inserted; set it to 2 to play for free.
#
# The arcade cabinet has a joystick that can move left and right. The software
# reads the position of the joystick with input instructions:
#
#     If the joystick is in the neutral position, provide 0.
#     If the joystick is tilted to the left, provide -1.
#     If the joystick is tilted to the right, provide 1.
#
# The arcade cabinet also has a segment display capable of showing a single
# number that represents the player's current score. When three output
# instructions specify X=-1, Y=0, the third output instruction is not a tile;
# the value instead specifies the new score to show in the segment display. For
# example, a sequence of output values like -1,0,12345 would show 12345 as the
# player's current score.
#
# Beat the game by breaking all the blocks. What is your score after the last
# block is broken?
# 

import os
import sys

TILE_WALL   = 1
TILE_BLOCK  = 2
TILE_PADDLE = 3
TILE_BALL   = 4

def main( argv ):
    if sys.version_info[ 0 ] < 3:
        print( "This script requires Python 3" )
        sys.exit( 1 )

    # Read in the input file
    with open( 'input/day13-input.txt', "r" ) as f:
        data = f.readline().split( ',' )

    # Convert to integers
    data = [ int( i ) for i in data ] 

    ####
    # Part 1
    game = Intcode( data[:], 10000 )
    game.runProg()
    
    tiles = game.getOutput( True )
    blockCount = 0

    for i in range( 0, len( tiles ), 3 ):
        if tiles[ i+2 ] == TILE_BLOCK:
            blockCount += 1

    print( "Part 1: Found %s block tiles" % blockCount )
    ####

    ####
    # Part 2
    data[ 0 ] = 2
    game.reset( data[:], 10000 )

    game.runProg()
    tiles = game.getOutput( True )

    lastBall = 0
    lastPaddle = 0

    while game.isRunning():
        for i in range( 0, len( tiles ), 3 ):
            if tiles[ i+2 ] == TILE_PADDLE:
                lastPaddle = tiles[ i ]

            elif tiles[ i+2 ] == TILE_BALL:
                lastBall = tiles[ i ]

        # Adjust the paddle position
        if lastBall > lastPaddle:
            game.addInput( 1 )
        elif lastBall < lastPaddle:
            game.addInput( -1 )
        else:
            game.addInput( 0 )

        game.runProg()
        tiles = game.getOutput( True )

    # Get the last score logged
    for i in range( 0, len( tiles ), 3 ):
        if tiles[ i ] == -1 and tiles[ i+1 ] == 0:
            print( "Part 2: Score %s" % tiles[ i+2 ] )
    ##

    return 0

class MyError( Exception ):
    def __init__( self, value ):
        self.value = value

    def __str__( self ):
        return repr( self.value )

class Tile( object ):
    def __init__( self, x, y, type ):
        self.x = x
        self.y = y
        self.type = type

class Intcode( object ):
    def __init__( self, mem, ram ):
        self.mem     = mem
        self.pc      = 0
        self.state   = 0
        self.inTape  = []
        self.outTape = []
        self.inPtr   = 0
        self.outPtr  = 0
        self.relBase = 0

        # Create some extra memory beyond the program
        mem += [ 0 ] * (ram - len( mem ) )
        
    def reset( self, mem, ram ):
        self.__init__( mem, ram )

    def isRunning( self ):
        return (self.state == 1)

    def getOutput( self, all=False ):
        # No output generated yet
        if not len( self.outTape ):
            r = None

        # Return most recent output and increment if we're not at the end
        elif not all:
            r = self.outTape[ self.outPtr ]

            if self.outPtr < len( self.outTape ):
                self.outPtr += 1

        else:
            r = self.outTape[ self.outPtr: ]
            self.outPtr = len( self.outTape )

        return r

    def getOutputCount( self ):
        return len( self.outTape )

    def addInput( self, inTape ):
        if type( inTape ) == list:
            self.inTape = self.inTape + inTape
        else:
            self.inTape.append( inTape )
        
    def runProg( self ):
        self.state = 1 # Start running

        # Begin processing
        while self.state:
            op    =  int( str( self.mem[ self.pc ] ), 16 ) & 0x000FF
            mode1 = (int( str( self.mem[ self.pc ] ), 16 ) & 0x00F00) >> 8
            mode2 = (int( str( self.mem[ self.pc ] ), 16 ) & 0x0F000) >> 12
            mode3 = (int( str( self.mem[ self.pc ] ), 16 ) & 0xF0000) >> 16

            # Addition
            if op == 0x01:
                a = self.mem[ self.pc + 1 ] 
                b = self.mem[ self.pc + 2 ] 
                x = self.mem[ self.pc + 3 ]

                a = self.mem[ self._off( a, mode1 ) ] if not (mode1 % 2) else a
                b = self.mem[ self._off( b, mode2 ) ] if not (mode2 % 2) else b
                x = self._off( x, mode3 ) 

                self.mem[ x ] = a + b
                self.pc += 4

            # Multiplication
            elif op == 0x02:
                a = self.mem[ self.pc + 1 ] 
                b = self.mem[ self.pc + 2 ]
                x = self.mem[ self.pc + 3 ]

                a = self.mem[ self._off( a, mode1 ) ] if not (mode1 % 2) else a
                b = self.mem[ self._off( b, mode2 ) ] if not (mode2 % 2) else b
                x = self._off( x, mode3 ) 

                self.mem[ x ] = a * b
                self.pc += 4

            # Input
            elif op == 0x03:
                # If there is no new input, wait for it
                if len( self.inTape ) == self.inPtr:
                    break

                # Otherwise grab and process the next input
                else:
                    a = self.mem[ self.pc + 1 ]
                    a = self._off( a, mode1 ) if not (mode1 % 2) else a

                    self.mem[ a ] = self.inTape[ self.inPtr ]

                    self.pc += 2
                    self.inPtr += 1 # Next input

            # Output
            elif op == 0x04:
                a = self.mem[ self.pc + 1 ] 
                a = self.mem[ self._off( a, mode1 ) ] if not (mode1 % 2) else a

                self.outTape.append( a )
                self.pc += 2

            # Jump if true
            elif op == 0x05:
                a = self.mem[ self.pc + 1 ] 
                b = self.mem[ self.pc + 2 ]

                a = self.mem[ self._off( a, mode1 ) ] if not (mode1 % 2) else a
                b = self.mem[ self._off( b, mode2 ) ] if not (mode2 % 2) else b

                if a != 0:
                    self.pc = b
                else:
                    self.pc += 3

            # Jump if false
            elif op == 0x06:
                a = self.mem[ self.pc + 1 ] 
                b = self.mem[ self.pc + 2 ]

                a = self.mem[ self._off( a, mode1 ) ] if not (mode1 % 2) else a
                b = self.mem[ self._off( b, mode2 ) ] if not (mode2 % 2) else b

                if a == 0:
                    self.pc = b
                else: 
                    self.pc += 3

            # Less than
            elif op == 0x07:
                a = self.mem[ self.pc + 1 ] 
                b = self.mem[ self.pc + 2 ]
                x = self.mem[ self.pc + 3 ]

                a = self.mem[ self._off( a, mode1 ) ] if not (mode1 % 2) else a
                b = self.mem[ self._off( b, mode2 ) ] if not (mode2 % 2) else b
                x = self._off( x, mode3 )

                if a < b:
                    self.mem[ x ] = 1
                else:
                    self.mem[ x ] = 0

                self.pc += 4

            # Equals
            elif op == 0x08:
                a = self.mem[ self.pc + 1 ] 
                b = self.mem[ self.pc + 2 ]
                x = self.mem[ self.pc + 3 ]
    
                a = self.mem[ self._off( a, mode1 ) ] if not (mode1 % 2) else a
                b = self.mem[ self._off( b, mode2 ) ] if not (mode2 % 2) else b
                x = self._off( x, mode3 )
    
                if a == b:
                    self.mem[ x ] = 1
                else:
                    self.mem[ x ] = 0
    
                self.pc += 4

            # Change relative base
            elif op == 0x09:
                a = self.mem[ self.pc + 1 ] 
                a = self.mem[ self._off( a, mode1 ) ] if not (mode1 % 2) else a

                self.relBase += a
                self.pc += 2
    
            # Terminate
            elif op == 0x99:
                self.state = 0

            else:
                raise MyError( "Unknown opcode encountered: pc = %s, op = %s" % (self.pc, op) )

    def _off( self, var, mode ):
        if mode == 2:
            return self.relBase + var
        else:
            return var


if __name__ == "__main__":
    main( argv=sys.argv )