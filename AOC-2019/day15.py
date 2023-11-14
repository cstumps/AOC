# --- Day 15: Oxygen System ---

# Out here in deep space, many things can go wrong. Fortunately, many of those
# things have indicator lights. Unfortunately, one of those lights is lit: the
# oxygen system for part of the ship has failed!

# According to the readouts, the oxygen system must have failed days ago after a
# rupture in oxygen tank two; that section of the ship was automatically sealed
# once oxygen levels went dangerously low. A single remotely-operated repair
# droid is your only option for fixing the oxygen system.

# The Elves' care package included an Intcode program (your puzzle input) that
# you can use to remotely control the repair droid. By running that program, you
# can direct the repair droid to the oxygen system and fix the problem.

# The remote control program executes the following steps in a loop forever:

#     Accept a movement command via an input instruction.
#     Send the movement command to the repair droid.
#     Wait for the repair droid to finish the movement operation.
#     Report on the status of the repair droid via an output instruction.

# Only four movement commands are understood: north (1), south (2), west (3),
# and east (4). Any other command is invalid. The movements differ in direction,
# but not in distance: in a long enough east-west hallway, a series of commands
# like 4,4,4,4,3,3,3,3 would leave the repair droid back where it started.

# The repair droid can reply with any of the following status codes:

#     0: The repair droid hit a wall. Its position has not changed.
#     1: The repair droid has moved one step in the requested direction.
#     2: The repair droid has moved one step in the requested direction; its new
#     position is the location of the oxygen system.

# You don't know anything about the area around the repair droid, but you can
# figure it out by watching the status codes.

# For example, we can draw the area using D for the droid, # for walls, . for
# locations the droid can traverse, and empty space for unexplored locations.
# Then, the initial state looks like this:
     
#    D  
      
# To make the droid go north, send it 1. If it replies with 0, you know that
# location is a wall and that the droid didn't move:
    
#    #  
#    D  
      
# To move east, send 4; a reply of 1 means the movement was successful:
     
#    #  
#    .D 

# Then, perhaps attempts to move north (1), south (2), and east (4) are all met
# with replies of 0:
      
#    ## 
#    .D#
#     # 
      
# Now, you know the repair droid is in a dead end. Backtrack with 3 (which you
# already know will get a reply of 1 because you already know that location is
# open):
  
#    ## 
#    D.#
#     # 
      
# Then, perhaps west (3) gets a reply of 0, south (2) gets a reply of 1, south
# again (2) gets a reply of 0, and then west (3) gets a reply of 2:
    
#    ## 
#   #..#
#   D.# 
#    #  

# Now, because of the reply of 2, you know you've found the oxygen system! In
# this example, it was only 2 moves away from the repair droid's starting
# position.

# What is the fewest number of movement commands required to move the repair
# droid from its starting position to the location of the oxygen system?

# --- Part Two ---

# You quickly repair the oxygen system; oxygen gradually fills the area.

# Oxygen starts in the location containing the repaired oxygen system. It takes
# one minute for oxygen to spread to all open locations that are adjacent to a
# location that already contains oxygen. Diagonal locations are not adjacent.

# In the example above, suppose you've used the droid to explore the area fully
# and have the following map (where locations that currently contain oxygen are
# marked O):

#  ##   
# #..## 
# #.#..#
# #.O.# 
#  ###  

# Initially, the only location which contains oxygen is the location of the
# repaired oxygen system. However, after one minute, the oxygen spreads to all
# open (.) locations that are adjacent to a location containing oxygen:

#  ##   
# #..## 
# #.#..#
# #OOO# 
#  ###  

# After a total of two minutes, the map looks like this:

#  ##   
# #..## 
# #O#O.#
# #OOO# 
#  ###  

# After a total of three minutes:

#  ##   
# #O.## 
# #O#OO#
# #OOO# 
#  ###  

# And finally, the whole region is full of oxygen after a total of four minutes:

#  ##   
# #OO## 
# #O#OO#
# #OOO# 
#  ###  

# So, in this example, all locations contain oxygen after 4 minutes.

# Use the repair droid to get a complete map of the area. How many minutes will
# it take to fill with oxygen?

import sys
import queue
import copy
import math

def main( argv ):

    # Read in the input file
    with open( 'input/day15-input.txt', "r" ) as f:
        data = f.readline().split( ',' )

    # Convert to integers
    data = [ int( i ) for i in data ] 

    ##
    # Part 1
    ##

    robot = Robot( data[:], (50, 50) )
    maze, steps = robot.generateMaze() 

    print( f"Part 1 answer: {steps}" )

    ##
    # Part 2
    ##

    # Find the goal from the completed map
    goal = (0,0)

    for row in range( 50 ):
        for col in range( 50 ):
            if maze[ row ][ col ] == Robot.CELL_GOAL:
                goal = (row, col)

    maxSteps = robot.exploreMaze( maze, goal )

    print( f"Part 2 answer: {maxSteps}" )

def printMaze( maze ):
    for row in range( 50 ):
        r = ''.join( map( mapMazeRow, maze[ row ] ) )
        print( r )

def mapMazeRow( x ):
    if x == Robot.CELL_WALL:
        return '#'
    elif x == Robot.CELL_GOAL:
        return 'G'
    else:
        return ' '

class MyError( Exception ):
    def __init__( self, value ):
        self.value = value

    def __str__( self ):
        return repr( self.value )

class Robot( object ):
    CELL_EMPTY   = 0
    CELL_WALL    = 1
    CELL_GOAL    = 2
    CELL_UNKNOWN = 3

    DIR_NORTH = 1
    DIR_SOUTH = 2
    DIR_WEST  = 3
    DIR_EAST  = 4

    def __init__( self, pgm, mapSize ):
        self.cx = math.floor( mapSize[ 0 ] / 2 )
        self.cy = math.floor( mapSize[ 1 ] / 2 )

        self.cpu = Intcode( pgm, 10000 )
        self.cpu.runProg()

    def exploreMaze( self, maze, start ):
        rowNum = [-1, 0, 0, 1]
        colNum = [0, -1, 1, 0]

        maxDistance = 0

        sx = start[ 0 ]
        sy = start[ 1 ]

        visited = [ [False] * self.cx * 2 for i in range( self.cy * 2 ) ]
        visited[ sx ][ sy ] = True

        q = queue.Queue()
        q.put( [ start, 0 ] )

        while not q.empty():
            c = q.get()
            maxDistance = max( maxDistance, c[ 1 ] )

            for i in range( 4 ):
                row = c[ 0 ][ 0 ] + rowNum[ i ]
                col = c[ 0 ][ 1 ] + colNum[ i ]

                if maze[ row ][ col ] != Robot.CELL_WALL and not visited[ row ][ col ]:
                        visited[ row ][ col ] = True
                        q.put( [ (row, col), c[ 1 ] + 1 ] )

        return maxDistance

    # Returns fully explored maze grid, shortest path to goal, maxSteps taken to fully explore
    def generateMaze( self ):
        maze = [ [Robot.CELL_UNKNOWN] * self.cx * 2 for i in range( self.cy * 2 ) ]
        steps = 999

        states = queue.Queue()

        # New position, new direction, machine state, distance from start
        states.put( [ (1, 0),  Robot.DIR_EAST,  self.cpu.saveState(), 1 ] )
        states.put( [ (-1, 0), Robot.DIR_WEST,  self.cpu.saveState(), 1 ] )
        states.put( [ (0, 1),  Robot.DIR_NORTH, self.cpu.saveState(), 1 ] )
        states.put( [ (0, -1), Robot.DIR_SOUTH, self.cpu.saveState(), 1 ] )

        maze[ self.cx ][ self.cy ] = Robot.CELL_EMPTY

        while not states.empty():
            state = states.get()

            pos       = state[ 0 ]
            dir       = state[ 1 ]
            machState = state[ 2 ]
            dist      = state[ 3 ]

            # Attempt to run the program to the desired location
            self.cpu.loadState( machState )
            self.cpu.addInput( dir )
            self.cpu.runProg()

            rc = self.cpu.getOutput()

            # See if we hit a wall or an empty space and only proceed if we were able to move to the space
            if rc == 1 or rc == 2:
                # Mark that we've visited the current location
                if rc == 1:
                    cellType = Robot.CELL_EMPTY
                else:
                    cellType = Robot.CELL_GOAL
                    steps = min( dist, steps )

                maze[ pos[ 0 ] + self.cx ][ pos[ 1 ] + self.cy ] = cellType

                # From here, queue up an additional move in each direction
                newMachState = self.cpu.saveState()

                # East
                newPos = (pos[ 0 ] + 1, pos[ 1 ])
                
                if maze[ newPos[ 0 ] + self.cx ][ newPos[ 1 ] + self.cy ] == Robot.CELL_UNKNOWN:
                    states.put( [ newPos, Robot.DIR_EAST,  copy.deepcopy( newMachState ), dist + 1 ] )

                # West  
                newPos = (pos[ 0 ] - 1, pos[ 1 ])

                if maze[ newPos[ 0 ] + self.cx ][ newPos[ 1 ] + self.cy ] == Robot.CELL_UNKNOWN:
                    states.put( [ newPos, Robot.DIR_WEST,  copy.deepcopy( newMachState ), dist + 1 ] )

                # North
                newPos = (pos[ 0 ], pos[ 1 ] + 1)

                if maze[ newPos[ 0 ] + self.cx ][ newPos[ 1 ] + self.cy ] == Robot.CELL_UNKNOWN:
                    states.put( [ newPos, Robot.DIR_NORTH, copy.deepcopy( newMachState ), dist + 1 ] )

                # South
                newPos = (pos[ 0 ], pos[ 1 ] - 1)

                if maze[ newPos[ 0 ] + self.cx ][ newPos[ 1 ] + self.cy ] == Robot.CELL_UNKNOWN:
                    states.put( [ newPos, Robot.DIR_SOUTH, copy.deepcopy( newMachState ), dist + 1 ] )

            else:
                maze[ pos[ 0 ] + self.cx ][ pos[ 1 ] + self.cy ] = Robot.CELL_WALL

        return maze, steps

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

    def saveState( self ):
        return [ self.pc, self.mem[:], self.state, self.inTape[:], self.outTape[:], self.inPtr, self.outPtr, self.relBase ]

    def loadState( self, state ):
        self.pc      = state[ 0 ]
        self.mem     = state[ 1 ]
        self.state   = state[ 2 ]
        self.inTape  = state[ 3 ]
        self.outTape = state[ 4 ]
        self.inPtr   = state[ 5 ]
        self.outPtr  = state[ 6 ]
        self.relBase = state[ 7 ] 

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