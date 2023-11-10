# --- Day 23: Opening the Turing Lock ---

# Little Jane Marie just got her very first computer for Christmas from some
# unknown benefactor. It comes with instructions and an example program, but the
# computer itself seems to be malfunctioning. She's curious what the program
# does, and would like you to help her run it.

# The manual explains that the computer supports two registers and six
# instructions (truly, it goes on to remind the reader, a state-of-the-art
# technology). The registers are named a and b, can hold any non-negative
# integer, and begin with a value of 0. The instructions are as follows:

#     hlf r sets register r to half its current value, then continues with the
#     next instruction.

#     tpl r sets register r to triple its current value, then continues with the
#     next instruction.

#     inc r increments register r, adding 1 to it, then continues with the next
#     instruction.

#     jmp offset is a jump; it continues with the instruction offset away
#     relative to itself.

#     jie r, offset is like jmp, but only jumps if register r is even ("jump if
#     even").

#     jio r, offset is like jmp, but only jumps if register r is 1 ("jump if
#     one", not odd).

# All three jump instructions work with an offset relative to that instruction.
# The offset is always written with a prefix + or - to indicate the direction of
# the jump (forward or backward, respectively). For example, jmp +1 would simply
# continue with the next instruction, while jmp +0 would continuously jump back
# to itself forever.

# The program exits when it tries to run an instruction beyond the ones defined.

# For example, this program sets a to 2, because the jio instruction causes it
# to skip the tpl instruction:

# inc a
# jio a, +2
# tpl a
# inc a

# What is the value in register b when the program in your puzzle input is
# finished executing?

# --- Part Two ---

# The unknown benefactor is very thankful for releasi-- er, helping little Jane
# Marie with her computer. Definitely not to distract you, what is the value in
# register b after the program is finished executing if register a starts as 1
# instead?

import sys

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day23-input.txt", "r" ) as f:
        data = [ line.strip() for line in f ]

    ##
    # Part 1
    ##

    mach = Interp()
    mach.runProg( data[:] )

    print( f"Part 1 answer: {mach.b}" )

    ##
    # Part 2
    ##

    mach = Interp( a=1 )
    mach.runProg( data[:] )

    print( f"Part 2 answer: {mach.b}" )

class Interp:
    def __init__( self, a=0 ):
        self.pc = 0
        self.a = a
        self.b = 0

    def runProg( self, mem ):
        while self.pc < len( mem ): # Terminate when we get past the list of instructions
            op, parms = mem[ self.pc ].split(maxsplit=1)

            if op == 'hlf':
                self.a = (self.a / 2) if parms[ 0 ] == 'a' else self.a
                self.b = (self.b / 2) if parms[ 0 ] == 'b' else self.b
                self.pc += 1

            elif op == 'tpl':
                self.a = (self.a * 3) if parms[ 0 ] == 'a' else self.a
                self.b = (self.b * 3) if parms[ 0 ] == 'b' else self.b
                self.pc += 1

            elif op == 'inc':
                self.a = (self.a + 1) if parms[ 0 ] == 'a' else self.a
                self.b = (self.b + 1) if parms[ 0 ] == 'b' else self.b
                self.pc += 1

            elif op == 'jmp':
                self.pc += int( parms )

            else:
                r = parms[ 0 ]
                j = int( parms.split( ',' )[ 1 ].strip() )

                if r == 'a':
                    val = self.a
                else:
                    val = self.b

                if op == 'jie':
                    self.pc = (self.pc + j) if (val % 2 == 0) else (self.pc + 1)
                elif op == 'jio':
                    self.pc = (self.pc + j) if (val == 1) else (self.pc + 1)
                else:
                    raise( f"Illegal instruction {op}" )

            
if __name__ == "__main__":
    main( argv=sys.argv )