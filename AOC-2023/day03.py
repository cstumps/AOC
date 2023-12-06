# --- Day 3: Gear Ratios ---

# You and the Elf eventually reach a gondola lift station; he says the gondola
# lift will take you up to the water source, but this is as far as he can bring
# you. You go inside.

# It doesn't take long to find the gondolas, but there seems to be a problem:
# they're not moving.

# "Aaah!"

# You turn around to see a slightly-greasy Elf with a wrench and a look of
# surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working
# right now; it'll still be a while before I can fix it." You offer to help.

# The engineer explains that an engine part seems to be missing from the engine,
# but nobody can figure out which one. If you can add up all the part numbers in
# the engine schematic, it should be easy to work out which part is missing.

# The engine schematic (your puzzle input) consists of a visual representation
# of the engine. There are lots of numbers and symbols you don't really
# understand, but apparently any number adjacent to a symbol, even diagonally,
# is a "part number" and should be included in your sum. (Periods (.) do not
# count as a symbol.)

# Here is an example engine schematic:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# In this schematic, two numbers are not part numbers because they are not
# adjacent to a symbol: 114 (top right) and 58 (middle right). Every other
# number is adjacent to a symbol and so is a part number; their sum is 4361.

# Of course, the actual engine schematic is much larger. What is the sum of all
# of the part numbers in the engine schematic?

# --- Part Two ---

# The engineer finds the missing part and installs it in the engine! As the
# engine springs to life, you jump in the closest gondola, finally ready to
# ascend to the water source.

# You don't seem to be going very fast, though. Maybe something is still wrong?
# Fortunately, the gondola has a phone labeled "help", so you pick it up and the
# engineer answers.

# Before you can explain the situation, she suggests that you look out the
# window. There stands the engineer, holding a phone in one hand and waving with
# the other. You're going so slowly that you haven't even left the station. You
# exit the gondola.

# The missing part wasn't the only issue - one of the gears in the engine is
# wrong. A gear is any * symbol that is adjacent to exactly two part numbers.
# Its gear ratio is the result of multiplying those two numbers together.

# This time, you need to find the gear ratio of every gear and add them all up
# so that the engineer can figure out which gear needs to be replaced.

# Consider the same engine schematic again:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# In this schematic, there are two gears. The first is in the top left; it has
# part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the
# lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear
# because it is only adjacent to one part number.) Adding up all of the gear
# ratios produces 467835.

# What is the sum of all of the gear ratios in your engine schematic?

import sys
import re

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day03-input.txt", "r" ) as f:
        data = [ line.rstrip( '\n' ) for line in f ]

    #data = [ '467..114..',
    #         '...*......',
    #         '..35..633.',
    #         '......#...',
    #         '617*......',
    #         '.....+.58.',
    #         '..592.....',
    #         '......755.',
    #         '...$.*....',
    #         '.664.598..' ]

    #data = [ '12.......*..', # 413
    #         '+.........34',
    #         '.......-12..',
    #         '..78........',
    #         '..*....60...',
    #         '78..........',
    #         '.......23...',
    #         '....90*12...',
    #         '............',
    #         '2.2......12.',
    #         '.*.........*',
    #         '1.1.......56' ]
    
    #data = [ '12.......*..', # 925
    #         '+.........34', 
    #         '.......-12..', 
    #         '..78........', 
    #         '..*....60...', 
    #         '78.........9', 
    #         '.5.....23..$', 
    #         '8...90*12...', 
    #         '............', 
    #         '2.2......12.', 
    #         '.*.........*', 
    #         '1.1..503+.56' ]
    
    #data = [ '........', # 4
    #         '.24..4..',
    #         '......*.' ]
    
    # ( deltaX, deltaY )
    lut = [ [ None ], 
            [ (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1) ],
            [ (-1, 0), (2, 0), (-1, -1), (-1, 1), (2, -1), (2, 1), (0, -1), (0, 1), (1, -1), (1, 1) ],
            [ (-1, 0), (3, 0), (-1, -1), (-1, 1), (3, -1), (3, 1), (0, -1), (0, 1), (1, -1), (1, 1), (2, -1), (2, 1) ] ] 

    numData = []

    # Could be done in a single line list comprehension however this is much more readable
    for y, line in enumerate( data ):
        for m in re.finditer( '(\d+)', line ):
            numData.append( [ m.group(), (m.start(), y) ] )
    
    ##
    # Part 1
    ##

    partSum = 0
    table = [ list( l ) for l in data ]  
    gears = {}

    for n in numData:
        for delta in lut[ len( n[ 0 ] ) ]:
            dx = n[ 1 ][ 0 ] + delta[ 0 ]
            dy = n[ 1 ][ 1 ] + delta[ 1 ]

            if dx < 0 or dy < 0 or dx >= len( table[ 0 ] ) or dy >= len( table ):
                continue

            c = table[ dy ][ dx ]

            # We need the gear data for part 2
            if c == '*':
                hash = str( dx ) + str( dy )

                if hash not in gears.keys():
                    gears[ hash ] = [ int( n[ 0 ] ) ]
                else:
                    gears[ hash ].append( int( n[ 0 ] ) )

            if c != '.' and not c.isdigit():
                partSum += int( n[ 0 ] )
                break # Only count the first symbol it's adjacent to

    print( f"Part 1 answer: {partSum}" )

    ##
    # Part 2
    ##

    gearSum = 0

    for v in gears.values():
        if len( v ) == 2:
            gearSum += (v[ 0 ] * v[ 1 ])

    print( f"Part 2 answer: {gearSum}" )


if __name__ == "__main__":
    main( argv=sys.argv )