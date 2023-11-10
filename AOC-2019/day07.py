# --- Day 7: Amplification Circuit ---
#
# Based on the navigational maps, you're going to need to send more power to
# your ship's thrusters to reach Santa in time. To do this, you'll need to
# configure a series of amplifiers already installed on the ship.
#
# There are five amplifiers connected in series; each one receives an input
# signal and produces an output signal. They are connected such that the first
# amplifier's output leads to the second amplifier's input, the second
# amplifier's output leads to the third amplifier's input, and so on. The first
# amplifier's input value is 0, and the last amplifier's output leads to your
# ship's thrusters.
#
#     O-------O  O-------O  O-------O  O-------O  O-------O
# 0 ->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-> (to thrusters)
#     O-------O  O-------O  O-------O  O-------O  O-------O
#
# The Elves have sent you some Amplifier Controller Software (your puzzle
# input), a program that should run on your existing Intcode computer. Each
# amplifier will need to run a copy of the program.
#
# When a copy of the program starts running on an amplifier, it will first use
# an input instruction to ask the amplifier for its current phase setting (an
# integer from 0 to 4). Each phase setting is used exactly once, but the Elves
# can't remember which amplifier needs which phase setting.
#
# The program will then call another input instruction to get the amplifier's
# input signal, compute the correct output signal, and supply it back to the
# amplifier with an output instruction. (If the amplifier has not yet received
# an input signal, it waits until one arrives.)
#
# Your job is to find the largest output signal that can be sent to the
# thrusters by trying every possible combination of phase settings on the
# amplifiers. Make sure that memory is not shared or reused between copies of
# the program.
#
# For example, suppose you want to try the phase setting sequence 3,1,2,4,0,
# which would mean setting amplifier A to phase setting 3, amplifier B to
# setting 1, C to 2, D to 4, and E to 0. Then, you could determine the output
# signal that gets sent from amplifier E to the thrusters with the following
# steps:
#
#     Start the copy of the amplifier controller software that 
#     will run on amplifier A. At its first input instruction, 
#     provide it the amplifier's phase setting, 3. At its second 
#     input instruction, provide it the input signal, 0. After some 
#     calculations, it will use an output instruction to indicate the 
#     amplifier's output signal.
#
#     Start the software for amplifier B. Provide it the phase 
#     setting (1) and then whatever output signal was produced from 
#     amplifier A. It will then produce a new output signal destined 
#     for amplifier C.
#
#     Start the software for amplifier C, provide the phase 
#     setting (2) and the value from amplifier B, then collect 
#     its output signal.
#
#     Run amplifier D's software, provide the phase setting (4) 
#     and input value, and collect its output signal.
#
#     Run amplifier E's software, provide the phase setting (0) 
#     and input value, and collect its output signal.
#
# The final output signal from amplifier E would be sent to the thrusters.
# However, this phase setting sequence may not have been the best one; another
# sequence might have sent a higher signal to the thrusters.
#
# Here are some example programs:
#
#     Max thruster signal 43210 (from phase setting sequence 4,3,2,1,0):
#
#     3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0
#
#     Max thruster signal 54321 (from phase setting sequence 0,1,2,3,4):
#
#     3,23,3,24,1002,24,10,24,1002,23,-1,23,
#     101,5,23,23,1,24,23,23,4,23,99,0,0
#
#     Max thruster signal 65210 (from phase setting sequence 1,0,4,3,2):
#
#     3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
#     1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0
#
# Try every combination of phase settings on the amplifiers. What is the highest
# signal that can be sent to the thrusters?
#

# --- Day 5: Sunny with a Chance of Asteroids ---
#
# You're starting to sweat as the ship makes its way toward Mercury. The Elves
# suggest that you get the air conditioner working by upgrading your ship
# computer to support the Thermal Environment Supervision Terminal.
#
# The Thermal Environment Supervision Terminal (TEST) starts by running a
# diagnostic program (your puzzle input). The TEST diagnostic program will run
# on your existing Intcode computer after a few modifications:
#
# First, you'll need to add two new instructions:
#
#     Opcode 3 takes a single integer as input and saves it to the position given 
#     by its only parameter. For example, the instruction 3,50 would take an input 
#     value and store it at address 50.
#
#     Opcode 4 outputs the value of its only parameter. For example, the instruction 
#     4,50 would output the value at address 50.
#
# Programs that use these instructions will come with documentation that
# explains what should be connected to the input and output. The program
# 3,0,4,0,99 outputs whatever it gets as input, then halts.
#
# Second, you'll need to add support for parameter modes:
#
# Each parameter of an instruction is handled based on its parameter mode. Right
# now, your ship computer already understands parameter mode 0, position mode,
# which causes the parameter to be interpreted as a position - if the parameter
# is 50, its value is the value stored at address 50 in memory. Until now, all
# parameters have been in position mode.
#
# Now, your ship computer will also need to handle parameters in mode 1,
# immediate mode. In immediate mode, a parameter is interpreted as a value - if
# the parameter is 50, its value is simply 50.
#
# Parameter modes are stored in the same value as the instruction's opcode. The
# opcode is a two-digit number based only on the ones and tens digit of the
# value, that is, the opcode is the rightmost two digits of the first value in
# an instruction. Parameter modes are single digits, one per parameter, read
# right-to-left from the opcode: the first parameter's mode is in the hundreds
# digit, the second parameter's mode is in the thousands digit, the third
# parameter's mode is in the ten-thousands digit, and so on. Any missing modes
# are 0.
#
# For example, consider the program 1002,4,3,4,33.
#
# The first instruction, 1002,4,3,4, is a multiply instruction - the rightmost
# two digits of the first value, 02, indicate opcode 2, multiplication. Then,
# going right to left, the parameter modes are 0 (hundreds digit), 1 (thousands
# digit), and 0 (ten-thousands digit, not present and therefore zero):
#
# ABCDE 1002
#
# DE - two-digit opcode, 02 == opcode 2 
#  C - mode of 1st parameter,  0 == position mode 
#  B - mode of 2nd parameter,  1 == immediate mode 
#  A - mode of 3rd parameter,  0 == position mode, omitted due to being a leading zero
#
# This instruction multiplies its first two parameters. The first parameter, 4
# in position mode, works like it did before - its value is the value stored at
# address 4 (33). The second parameter, 3 in immediate mode, simply has value 3.
# The result of this operation, 33 * 3 = 99, is written according to the third
# parameter, 4 in position mode, which also works like it did before - 99 is
# written to address 4.
#
# Parameters that an instruction writes to will never be in immediate mode.
#
# Finally, some notes:
#
#     It is important to remember that the instruction pointer should increase 
#     by the number of values in the instruction after the instruction finishes. 
#     Because of the new instructions, this amount is no longer always 4.
#
#     Integers can be negative: 1101,100,-1,4,0 is a valid program (find 100 + -1, 
#     store the result in position 4).
#
# The TEST diagnostic program will start by requesting from the user the ID of
# the system to test by running an input instruction - provide it 1, the ID for
# the ship's air conditioner unit.
#
# It will then perform a series of diagnostic tests confirming that various
# parts of the Intcode computer, like parameter modes, function correctly. For
# each test, it will run an output instruction indicating how far the result of
# the test was from the expected value, where 0 means the test was successful.
# Non-zero outputs mean that a function is not working correctly; check the
# instructions that were run before the output instruction to see which one
# failed.
#
# Finally, the program will output a diagnostic code and immediately halt. This
# final output isn't an error; an output followed immediately by a halt means
# the program finished. If all outputs were zero except the diagnostic code, the
# diagnostic program ran successfully.
#
# After providing 1 to the only input instruction and passing all the tests,
# what diagnostic code does the program produce?
#
# --- Part Two ---
#
# The air conditioner comes online! Its cold air feels good for a while, but
# then the TEST alarms start to go off. Since the air conditioner can't vent its
# heat anywhere but back into the spacecraft, it's actually making the air
# inside the ship warmer.
#
# Instead, you'll need to use the TEST to extend the thermal radiators.
# Fortunately, the diagnostic program (your puzzle input) is already equipped
# for this. Unfortunately, your Intcode computer is not.
#
# Your computer is only missing a few opcodes:
#
#     Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the 
#     instruction pointer to the value from the second parameter. Otherwise, it 
#     does nothing.
#
#     Opcode 6 is jump-if-false: if the first parameter is zero, it sets the 
#     instruction pointer to the value from the second parameter. Otherwise, it 
#     does nothing.
#
#     Opcode 7 is less than: if the first parameter is less than the second 
#     parameter, it stores 1 in the position given by the third parameter. 
#     Otherwise, it stores 0.
#
#     Opcode 8 is equals: if the first parameter is equal to the second parameter, 
#     it stores 1 in the position given by the third parameter. Otherwise, it 
#     stores 0.
#
# Like all instructions, these instructions need to support parameter modes as
# described above.
#
# Normally, after an instruction is finished, the instruction pointer increases
# by the number of values in that instruction. However, if the instruction
# modifies the instruction pointer, that value is used and the instruction
# pointer is not automatically increased.
#
# For example, here are several programs that take one input, compare it to the
# value 8, and then produce one output:
#
#     3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input 
#     is equal to 8; output 1 (if it is) or 0 (if it is not).
#
#     3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is 
#     less than 8; output 1 (if it is) or 0 (if it is not).
#
#     3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is 
#     equal to 8; output 1 (if it is) or 0 (if it is not).
#
#     3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is 
#     less than 8; output 1 (if it is) or 0 (if it is not).
#
# Here are some jump tests that take an input, then output 0 if the input was
# zero or 1 if the input was non-zero:
#
#     3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
#     3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)
#
# Here's a larger example:
#
# 3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
# 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
# 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
#
# The above example program uses an input instruction to ask for a single
# number. The program will then output 999 if the input value is below 8, output
# 1000 if the input value is equal to 8, or output 1001 if the input value is
# greater than 8.
#
# This time, when the TEST diagnostic program runs its input instruction to get
# the ID of the system to test, provide it 5, the ID for the ship's thermal
# radiator controller. This diagnostic test suite only outputs one number, the
# diagnostic code.
#
# What is the diagnostic code for system ID 5?
# 
# --- Part Two ---
#
# It's no good - in this configuration, the amplifiers can't generate a large
# enough output signal to produce the thrust you'll need. The Elves quickly talk
# you through rewiring the amplifiers into a feedback loop:
#
#       O-------O  O-------O  O-------O  O-------O  O-------O
# 0 -+->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-. |  O-------O
#    O-------O  O-------O  O-------O  O-------O |
#    |                                                        |
#    '--------------------------------------------------------+
#                                                             |
#                                                             v
#                                                      (to thrusters)
#
# Most of the amplifiers are connected as they were before; amplifier A's output
# is connected to amplifier B's input, and so on. However, the output from
# amplifier E is now connected into amplifier A's input. This creates the
# feedback loop: the signal will be sent through the amplifiers many times.
#
# In feedback loop mode, the amplifiers need totally different phase settings:
# integers from 5 to 9, again each used exactly once. These settings will cause
# the Amplifier Controller Software to repeatedly take input and produce output
# many times before halting. Provide each amplifier its phase setting at its
# first input instruction; all further input/output instructions are for
# signals.
#
# Don't restart the Amplifier Controller Software on any amplifier during this
# process. Each one should continue receiving and sending signals until it
# halts.
#
# All signals sent or received in this process will be between pairs of
# amplifiers except the very first signal and the very last signal. To start the
# process, a 0 signal is sent to amplifier A's input exactly once.
#
# Eventually, the software on the amplifiers will halt after they have processed
# the final loop. When this happens, the last output signal from amplifier E is
# sent to the thrusters. Your job is to find the largest output signal that can
# be sent to the thrusters using the new phase settings and feedback loop
# arrangement.
#
# Here are some example programs:
#
#     Max thruster signal 139629729 (from phase setting sequence 9,8,7,6,5):
#
#     3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
#     27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
#
#     Max thruster signal 18216 (from phase setting sequence 9,7,8,5,6):
#
#     3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
#     -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
#     53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10
#
# Try every combination of the new phase settings on the amplifier feedback
# loop. What is the highest signal that can be sent to the thrusters?

import sys
import itertools

def main( argv ):

    # Read in input file
    with open( "input/day07-input.txt", "r" ) as f:
        data = f.readline().split( ',' )

    #data = [ '3', '15', '3', '16', '1002', '16', '10', '16', '1', '16', '15', '15', '4', '15' ,'99' ,'0' ,'0' ]
    #data = [ '3','26','1001','26','-4','26','3','27','1002','27','2','27','1','27','26','27','4','27','1001','28','-1','28','1005','28','6','99','0','0','5' ]

    # Convert to integers
    data = [ int( i ) for i in data ]

    # Part 1
    maxThrust = 0
    phase     = 0

    a1 = Intcode( data[:] )
    a2 = Intcode( data[:] )
    a3 = Intcode( data[:] )
    a4 = Intcode( data[:] )
    a5 = Intcode( data[:] )

    for p in itertools.permutations( [ 0, 1, 2, 3, 4 ] ):

        a1.reset( data[:] )
        a2.reset( data[:] )
        a3.reset( data[:] )
        a4.reset( data[:] )
        a5.reset( data[:] )

        a1.addInput( [ p[ 0 ], 0 ] )
        a1.runProg()

        a2.addInput( [ p[ 1 ], a1.getOutput() ] )
        a2.runProg()

        a3.addInput( [ p[ 2 ], a2.getOutput() ] )
        a3.runProg()

        a4.addInput( [ p[ 3 ], a3.getOutput() ] )
        a4.runProg()

        a5.addInput( [ p[ 4 ], a4.getOutput() ] )
        a5.runProg()
        
        thrust = a5.getOutput()

        if thrust > maxThrust:
            maxThrust = thrust
            phase = p

    print( "Part 1 max thrust %s at phase %s." % (maxThrust, phase) )

    # Part 2
    maxThrust = 0
    phase     = 0

    for p in itertools.permutations( [ 5, 6, 7, 8, 9 ] ):

        # Init memory
        a1.reset( data[:] )
        a2.reset( data[:] )
        a3.reset( data[:] )
        a4.reset( data[:] )
        a5.reset( data[:] )

        # Send phase
        a1.addInput( p[ 0 ] )
        a2.addInput( p[ 1 ] )
        a3.addInput( p[ 2 ] )
        a4.addInput( p[ 3 ] )
        a5.addInput( p[ 4 ] )

        # Initial signal
        feedback = 0

        while True:
            a1.addInput( feedback )
            a1.runProg()

            a2.addInput( a1.getOutput() )
            a2.runProg()

            a3.addInput( a2.getOutput() )
            a3.runProg()

            a4.addInput( a3.getOutput() )
            a4.runProg()

            a5.addInput( a4.getOutput() )
            a5.runProg()

            feedback = a5.getOutput()

            if ( not a1.isRunning() and 
                 not a2.isRunning() and 
                 not a3.isRunning() and 
                 not a4.isRunning() and 
                 not a5.isRunning() ):
                break

        if feedback > maxThrust:
            maxThrust = feedback
            phase = p

    print( "Part 2 max thrust %s at phase %s." % (maxThrust, phase) )

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
        
    def reset( self, mem ):
        self.__init__( mem )

    def isRunning( self ):
        return (self.state == 1)

    def getOutput( self ):
        # No output generated yet
        if not len( self.outTape ):
            r = None

        # Return most recent output and increment if we're not at the end
        else:
            r = self.outTape[ self.outPtr ]

            if self.outPtr < len( self.outTape ):
                self.outPtr += 1

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
            op    = int( str( self.mem[ self.pc ] ), 16 ) & 0x000FF
            mode1 = int( str( self.mem[ self.pc ] ), 16 ) & 0x00F00
            mode2 = int( str( self.mem[ self.pc ] ), 16 ) & 0x0F000
            mode3 = int( str( self.mem[ self.pc ] ), 16 ) & 0xF0000

            # Addition
            if op == 0x01:
                a = self.mem[ self.pc + 1 ] 
                b = self.mem[ self.pc + 2 ] 
                x = self.mem[ self.pc + 3 ]

                a = self.mem[ a ] if not mode1 else a
                b = self.mem[ b ] if not mode2 else b

                self.mem[ x ] = a + b
                self.pc += 4

            # Multiplication
            elif op == 0x02:
                a = self.mem[ self.pc + 1 ] 
                b = self.mem[ self.pc + 2 ]
                x = self.mem[ self.pc + 3 ]

                a = self.mem[ a ] if not mode1 else a
                b = self.mem[ b ] if not mode2 else b

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
                    self.mem[ a ] = self.inTape[ self.inPtr ]

                    self.pc += 2
                    self.inPtr += 1 # Next input

            # Output
            elif op == 0x04:
                a = self.mem[ self.pc + 1 ] 
                a = self.mem[ a ] if not mode1 else a

                self.outTape.append( a )
                self.pc += 2

            # Jump if true
            elif op == 0x05:
                a = self.mem[ self.pc + 1 ] 
                b = self.mem[ self.pc + 2 ]

                a = self.mem[ a ] if not mode1 else a
                b = self.mem[ b ] if not mode2 else b

                if a != 0:
                    self.pc = b
                else:
                    self.pc += 3

            # Jump if false
            elif op == 0x06:
                a = self.mem[ self.pc + 1 ] 
                b = self.mem[ self.pc + 2 ]

                a = self.mem[ a ] if not mode1 else a
                b = self.mem[ b ] if not mode2 else b

                if a == 0:
                    self.pc = b
                else: 
                    self.pc += 3

            # Less than
            elif op == 0x07:
                a = self.mem[ self.pc + 1 ] 
                b = self.mem[ self.pc + 2 ]
                x = self.mem[ self.pc + 3 ]

                a = self.mem[ a ] if not mode1 else a
                b = self.mem[ b ] if not mode2 else b

                if a < b:
                    self.mem[ x ] = 1
                else:
                    self.mem[ x ] = 0

                pc += 4

            # Equals
            elif op == 0x08:
                a = self.mem[ self.pc + 1 ] 
                b = self.mem[ self.pc + 2 ]
                x = self.mem[ self.pc + 3 ]
    
                a = self.mem[ a ] if not mode1 else a
                b = self.mem[ b ] if not mode2 else b
    
                if a == b:
                    self.mem[ x ] = 1
                else:
                    self.mem[ x ] = 0
    
                self.pc += 4
    
            # Terminate
            elif op == 0x99:
                self.state = 0

            else:
                raise MyError( "Unknown opcode encountered: pc = %s, op = %s" % (self.pc, op) )

if __name__ == "__main__":
    main( argv=sys.argv )