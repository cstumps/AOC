# --- Day 11: Space Police ---
#
# On the way to Jupiter, you're pulled over by the Space Police.
#
# "Attention, unmarked spacecraft! You are in violation of Space Law! All
# spacecraft must have a clearly visible registration identifier! You have 24
# hours to comply or be sent to Space Jail!"
#
# Not wanting to be sent to Space Jail, you radio back to the Elves on Earth for
# help. Although it takes almost three hours for their reply signal to reach
# you, they send instructions for how to power up the emergency hull painting
# robot and even provide a small Intcode program (your puzzle input) that will
# cause it to paint your ship appropriately.
#
# There's just one problem: you don't have an emergency hull painting robot.
#
# You'll need to build a new emergency hull painting robot. The robot needs to
# be able to move around on the grid of square panels on the side of your ship,
# detect the color of its current panel, and paint its current panel black or
# white. (All of the panels are currently black.)
#
# The Intcode program will serve as the brain of the robot. The program uses
# input instructions to access the robot's camera: provide 0 if the robot is
# over a black panel or 1 if the robot is over a white panel. Then, the program
# will output two values:
#
#     First, it will output a value indicating the color to paint the panel the 
#     robot is over: 0 means to paint the panel black, and 1 means to paint the 
#     panel white.
#
#     Second, it will output a value indicating the direction the robot should 
#     turn: 0 means it should turn left 90 degrees, and 1 means it should turn 
#     right 90 degrees.
#
# After the robot turns, it should always move forward exactly one panel. The
# robot starts facing up.
#
# The robot will continue running for a while like this and halt when it is
# finished drawing. Do not restart the Intcode computer inside the robot during
# this process.
#
# For example, suppose the robot is about to start running. Drawing black panels
# as ., white panels as #, and the robot pointing the direction it is facing (<
# ^ > v), the initial state and region near the robot looks like this:
#
# .....
# .....
# ..^..
# .....
# .....
#
# The panel under the robot (not visible here because a ^ is shown instead) is
# also black, and so any input instructions at this point should be provided 0.
# Suppose the robot eventually outputs 1 (paint white) and then 0 (turn left).
# After taking these actions and moving forward one panel, the region now looks
# like this:
#
# .....
# .....
# .<#..
# .....
# .....
#
# Input instructions should still be provided 0. Next, the robot might output 0
# (paint black) and then 0 (turn left):
#
# .....
# .....
# ..#..
# .v...
# .....
#
# After more outputs (1,0, 1,0):
#
# .....
# .....
# ..^..
# .##..
# .....
#
# The robot is now back where it started, but because it is now on a white
# panel, input instructions should be provided 1. After several more outputs
# (0,1, 1,0, 1,0), the area looks like this:
#
# .....
# ..<#.
# ...#.
# .##..
# .....
#
# Before you deploy the robot, you should probably have an estimate of the area
# it will cover: specifically, you need to know the number of panels it paints
# at least once, regardless of color. In the example above, the robot painted 6
# panels at least once. (It painted its starting panel twice, but that panel is
# still only counted once; it also never painted the panel it ended on.)
#
# Build a new emergency hull painting robot and run the Intcode program on it.
# How many panels does it paint at least once?
#
# --- Part Two ---
#
# You're not sure what it's trying to paint, but it's definitely not a
# registration identifier. The Space Police are getting impatient.
#
# Checking your external ship cameras again, you notice a white panel marked
# "emergency hull painting robot starting panel". The rest of the panels are
# still black, but it looks like the robot was expecting to start on a white
# panel, not a black one.
#
# Based on the Space Law Space Brochure that the Space Police attached to one of
# your windows, a valid registration identifier is always eight capital letters.
# After starting the robot on a single white panel instead, what registration
# identifier does it paint on your hull?
#

import sys
import math

SHIP_WIDTH  = 100
SHIP_HEIGHT = 100

DIR_UP    = 0
DIR_LEFT  = 1
DIR_DOWN  = 2
DIR_RIGHT = 3

def main( argv ):

    panelList = []

    # Read in input file
    with open( "input/day11-input.txt", "r" ) as f:
        data = f.readline().split( ',' )

    # Convert to integers
    data = [ int( i ) for i in data ]

    # Create an array of panels for our ship
    panels = [ [ Panel( x, y, 0 ) for x in range( SHIP_WIDTH ) ] for y in range( SHIP_HEIGHT ) ]

    # Init the robot position 
    curPos = panels[ int( math.floor( SHIP_HEIGHT / 2 ) ) ][ int( math.floor( SHIP_WIDTH / 2 ) ) ]
    curDir = DIR_UP

    # Part 1:  Start on a black panel (0)
    # Part 2:  Start on a white panel (1)
    curPos.color = 1

    # Start the robot
    robot = Intcode( data[:], 10000 )
    robot.runProg()

    while robot.isRunning():
        # Feed it the current camera input
        robot.addInput( curPos.color )

        # Run until the next two outputs
        robot.runProg()
        robot.runProg()

        # Read out the color and new direction
        curPos.color = robot.getOutput()
        newDir       = robot.getOutput()

        # Update direction
        if not newDir: # Turn left 90 degrees
            curDir = (curDir - 1) % 4
        else:          # Turn right 90 degrees
            curDir = (curDir + 1) % 4

        # Move
        if curDir == DIR_UP:
            curPos = panels[ curPos.y - 1 ][ curPos.x ]
        elif curDir == DIR_LEFT:
            curPos = panels[ curPos.y ][ curPos.x + 1 ]
        elif curDir == DIR_DOWN:
            curPos = panels[ curPos.y + 1 ][ curPos.x ]
        else:
            curPos = panels[ curPos.y ][ curPos.x - 1 ]

        # Add the panel to our list
        if curPos not in panelList:
            panelList.append( curPos )

    # How many unique panels did we touch?
    print( "Part 1: Painted %s unique panels" % len( panelList ) )

    # Part 2:
    printShip( panels, curPos, curDir )

    return 0

def printShip( ship, pos, dir ):
    for y in range( SHIP_HEIGHT ):
        line = ''

        for x in range( SHIP_WIDTH ):
            if x == pos.x and y == pos.y:
                if dir == DIR_UP:
                    line += '^ '
                elif dir == DIR_LEFT:
                    line += '> '
                elif dir == DIR_DOWN:
                    line += 'v '
                else:
                    line += '< '

            else:
                line = line + str( ship[ y ][ x ] ) + ' '

        print( line )

class MyError( Exception ):
    def __init__( self, value ):
        self.value = value

    def __str__( self ):
        return repr( self.value )

class Panel( object ):
    def __init__( self, x, y, color ):
        self.x = x
        self.y = y
        self.color = color

    def __eq__( self, other ):
        return (self.x == other.x) and (self.y == other.y)

    def __str__( self ):
        return "%s" % self.color

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