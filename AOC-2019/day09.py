# --- Day 9: Sensor Boost ---
#
# You've just said goodbye to the rebooted rover and left Mars when you receive
# a faint distress signal coming from the asteroid belt. It must be the Ceres
# monitoring station!
#
# In order to lock on to the signal, you'll need to boost your sensors. The
# Elves send up the latest BOOST program - Basic Operation Of System Test.
#
# While BOOST (your puzzle input) is capable of boosting your sensors, for
# tenuous safety reasons, it refuses to do so until the computer it runs on
# passes some checks to demonstrate it is a complete Intcode computer.
#
# Your existing Intcode computer is missing one key feature: it needs support
# for parameters in relative mode.
#
# Parameters in mode 2, relative mode, behave very similarly to parameters in
# position mode: the parameter is interpreted as a position. Like position mode,
# parameters in relative mode can be read from or written to.
#
# The important difference is that relative mode parameters don't count from
# address 0. Instead, they count from a value called the relative base. The
# relative base starts at 0.
#
# The address a relative mode parameter refers to is itself plus the current
# relative base. When the relative base is 0, relative mode parameters and
# position mode parameters with the same value refer to the same address.
#
# For example, given a relative base of 50, a relative mode parameter of -7
# refers to memory address 50 + -7 = 43.
#
# The relative base is modified with the relative base offset instruction:
#
#     Opcode 9 adjusts the relative base by the value of its only parameter. 
#     The relative base increases (or decreases, if the value is negative) by 
#     the value of the parameter.
#
# For example, if the relative base is 2000, then after the instruction 109,19,
# the relative base would be 2019. If the next instruction were 204,-34, then
# the value at address 1985 would be output.
#
# Your Intcode computer will also need a few other capabilities:
#
#     The computer's available memory should be much larger than the initial 
#     program. Memory beyond the initial program starts with the value 0 and 
#     can be read or written like any other memory. (It is invalid to try to 
#     access memory at a negative address, though.)
#
#     The computer should have support for large numbers. Some instructions 
#     near the beginning of the BOOST program will verify this capability.
#
# Here are some example programs that use these features:
#
#     109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99 takes no input 
#     and produces a copy of itself as output.
#
#     1102,34915192,34915192,7,4,7,99,0 should output a 16-digit number.
#
#     104,1125899906842624,99 should output the large number in the middle.
#
# The BOOST program will ask for a single input; run it in test mode by
# providing it the value 1. It will perform a series of checks on each opcode,
# output any opcodes (and the associated parameter modes) that seem to be
# functioning incorrectly, and finally output a BOOST keycode.
#
# Once your Intcode computer is fully functional, the BOOST program should
# report no malfunctioning opcodes when run in test mode; it should only output
# a single value, the BOOST keycode. What BOOST keycode does it produce?
#
# --- Part Two ---
#
# You now have a complete Intcode computer.
#
# Finally, you can lock on to the Ceres distress signal! You just need to boost
# your sensors using the BOOST program.
#
# The program runs in sensor boost mode by providing the input instruction the
# value 2. Once run, it will boost the sensors automatically, but it might take
# a few seconds to complete the operation on slower hardware. In sensor boost
# mode, the program will output a single value: the coordinates of the distress
# signal.
#
# Run the BOOST program in sensor boost mode. What are the coordinates of the
# distress signal?
#

import sys
import itertools

def main( argv ):

    # Read in input file
    with open( "input/day09-input.txt", "r" ) as f:
        data = f.readline().split( ',' )

    #data = [ '109', '1', '204', '-1', '1001', '100', '1', '100', '1008', '100', '16', '101', '1006', '101', '0', '99' ]
    #data = [ '1102', '34915192', '34915192', '7', '4', '7', '99', '0' ]
    #data = [ '104', '1125899906842624', '99' ]

    # Convert to integers
    data = [ int( i ) for i in data ]

    a1 = Intcode( data[:] )

    a1.addInput( 1 )
    a1.runProg()
    
    results = a1.getOutput( True )

    print( "Part 1 answer: %s" % results[ 0 ] )

    # Part 2

    a1.reset( data[:] )
    a1.addInput( 2 )
    a1.runProg()

    results = a1.getOutput( True )

    print( "Part 2 answer: %s" % results[ 0 ] )


    return 0

class MyError( Exception ):
    def __init__( self, value ):
        self.value = value

    def __str__( self ):
        return repr( self.value )

class Intcode( object ):
    def __init__( self, mem ):
        self.mem     = mem
        self.pc      = 0
        self.state   = 0
        self.inTape  = []
        self.outTape = []
        self.inPtr   = 0
        self.outPtr  = 0
        self.relBase = 0

        # Create some extra memory beyond the program
        mem += [ 0 ] * (10000 - len( mem ) )
        
    def reset( self, mem ):
        self.__init__( mem )

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