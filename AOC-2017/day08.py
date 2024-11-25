# --- Day 8: I Heard You Like Registers ---

# You receive a signal directly from the CPU. Because of your recent assistance
# with jump instructions, it would like you to compute the result of a series of
# unusual register instructions.

# Each instruction consists of several parts: the register to modify, whether to
# increase or decrease that register's value, the amount by which to increase or
# decrease it, and a condition. If the condition fails, skip the instruction
# without modifying the register. The registers all start at 0. The instructions
# look like this:

# b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10

# These instructions would be processed as follows:

#     Because a starts at 0, it is not greater than 1, and so b is not modified.
#     a is increased by 1 (to 1) because b is less than 5 (it is 0).
#     c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
#     c is increased by -20 (to -10) because c is equal to 10.

# After this process, the largest value in any register is 1.

# You might also encounter <= (less than or equal to) or != (not equal to).
# However, the CPU doesn't have the bandwidth to tell you what all the registers
# are named, and leaves that to you to determine.

# What is the largest value in any register after completing the instructions in
# your puzzle input?

# --- Part Two ---

# To be safe, the CPU also needs to know the highest value held in any register
# during this process so that it can decide how much memory to allocate to these
# operations. For example, in the above instructions, the highest value ever
# held was 10 (in register c after the third instruction was evaluated).

import sys

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day08-input.txt", "r" ) as f:
        data = [ line.rstrip( '\n' ) for line in f ]

    #data = [ 'b inc 5 if a > 1',
    #         'a inc 1 if b < 5',
    #         'c dec -10 if a >= 1',
    #         'c inc -20 if c == 10' ]

    ##
    # Part 1
    ##

    cpu = CPU()

    # r1 op v1 if r2 cond v2
    for line in data:
        line = line.split()

        r1 = line[ 0 ]
        op = line[ 1 ]
        v1 = line[ 2 ]
        cond = line[ -3: ]

        cpu.run( r1, op, v1, cond )

    print( f"Part 1 answer: {max( cpu.regs.values() )}" )

    ##
    # Part 2
    ##

    print( f"Part 2 answer: {cpu.maxValue}" )

class CPU:
    def __init__( self ):
        self.regs = {}
        self.maxValue = 0

    def run( self, r1, op, v1, cond ): 
        r2 = str( self.regs.get( cond[ 0 ], 0 ) )

        if eval( r2 + ' '.join( cond[ 1: ] ) ):
            tmp = self.regs.get( r1, 0 )

            if  op == 'inc':
                tmp += int( v1 )
            elif op == 'dec':
                tmp -= int( v1 )
            else:
                raise( "Undefined operation" )
            
            self.regs[ r1 ] = tmp
            self.maxValue = max( self.maxValue, tmp )

if __name__ == "__main__":
    main( argv=sys.argv )