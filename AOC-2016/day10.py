# --- Day 10: Balance Bots ---

# You come upon a factory in which many robots are zooming around handing small
# microchips to each other.

# Upon closer examination, you notice that each bot only proceeds when it has
# two microchips, and once it does, it gives each one to a different bot or puts
# it in a marked "output" bin. Sometimes, bots take microchips from "input"
# bins, too.

# Inspecting one of the microchips, it seems like they each contain a single
# number; the bots must use some logic to decide what to do with each chip. You
# access the local control computer and download the bots' instructions (your
# puzzle input).

# Some of the instructions specify that a specific-valued microchip should be
# given to a specific bot; the rest of the instructions indicate what a given
# bot should do with its lower-value or higher-value chip.

# For example, consider the following instructions:

# value 5 goes to bot 2 bot 2 gives low to bot 1 and high to bot 0 value 3 goes
# to bot 1 bot 1 gives low to output 1 and high to bot 0 bot 0 gives low to
# output 2 and high to output 0 value 2 goes to bot 2

#     Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a
#     value-2 chip and a value-5 chip.

#     Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and
#     its higher one (5) to bot 0.

#     Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and
#     gives the value-3 chip to bot 0.

#     Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in
#     output 0.

# In the end, output bin 0 contains a value-5 microchip, output bin 1 contains a
# value-2 microchip, and output bin 2 contains a value-3 microchip. In this
# configuration, bot number 2 is responsible for comparing value-5 microchips
# with value-2 microchips.

# Based on your instructions, what is the number of the bot that is responsible
# for comparing value-61 microchips with value-17 microchips?

# --- Part Two ---

# What do you get if you multiply together the values of one chip in each of
# outputs 0, 1, and 2?

import sys

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day10-input.txt", "r" ) as f:
        data = f.readlines()

    #data = [ 'value 5 goes to bot 2',
    #         'bot 2 gives low to bot 1 and high to bot 0',
    #         'value 3 goes to bot 1',
    #         'bot 1 gives low to output 1 and high to bot 0',
    #         'bot 0 gives low to output 2 and high to output 0',
    #         'value 2 goes to bot 2' ]

    operations = {}
    bots = {}
    outputs = {}

    # Initialize the bots
    for line in data:
        if 'value' in line:
            line = line.strip().split()

            bot = int( line[ -1 ] )
            val = int( line[ 1 ] )

            if bot not in bots.keys():
                bots[ bot ] = Bot( bot )

            bots[ bot ].addValue( val )

    # Initialize the outputs
    for line in data:
        if 'output' in line:
            line = line.strip().split()

            if line[ 5 ] == 'output':
                outputs[ int( line[ 6 ] ) ] = Bot( int( line[ 6 ] ) )

            if line[ 10 ] == 'output':
                outputs[ int( line[ 11 ] ) ] = Bot( int( line[ 11 ] ) )

    # Set up the operations
    for line in data:
        if 'gives' in line:
            line = line.strip().split()

            bot   = int( line[ 1 ] )
            loTgt = int( line[ 6 ] )
            hiTgt = int( line[ -1 ] )

            if bot not in bots.keys():
                bots[ bot ] = Bot( bot )

            if line[ 5 ] == 'bot':
                if loTgt not in bots.keys():
                    bots[ loTgt ] = Bot( loTgt )

            if line[ -2 ] == 'bot':
                if hiTgt not in bots.keys():
                    bots[ hiTgt ] = Bot( hiTgt )

            loTgt = bots[ int( line[ 6 ] ) ] if line[ 5 ] == 'bot' else outputs[ int( line[ 6 ] ) ]
            hiTgt = bots[ int( line[ -1 ] ) ] if line[ -2 ] == 'bot' else outputs[ int( line[ -1 ] ) ]

            operations[ bot ] = Operation( bot, loTgt, hiTgt )

    ##
    # Part 1
    ##

    answer = -1
    repeat = True

    while repeat:
        for n, b in bots.items():
            if len( b.values ) >= 2:
                if b.values[ 0 ] == 17 and b.values[ -1 ] == 61: # Win condition
                    answer = n
            
                op = operations[ n ]
                b.compare( op.loTgt, op.hiTgt )

                break
        else:
            repeat = False
        
    print( f"Part 1 answer: {answer}" )

    ##
    # Part 2
    ##

    answer = outputs[ 0 ].values[ 0 ] * outputs[ 1 ].values[ 0 ] * outputs[ 2 ].values[ 0 ]

    print( f"Part 2 answer: {answer}" )

class Bot:
    def __init__( self, number ):
        self.number = number
        self.values = []

    def addValue( self, value ):
        self.values.append( value )
        self.values.sort()

    def compare( self, loBot, hiBot ):
        loBot.addValue( self.values[ 0 ] )
        hiBot.addValue( self.values[ -1 ] )

        self.values = []

class Operation:
    def __init__( self, number, loTgt, hiTgt ):
        self.number = number
        self.loTgt = loTgt
        self.hiTgt = hiTgt

 
if __name__ == "__main__":
    main( argv=sys.argv )