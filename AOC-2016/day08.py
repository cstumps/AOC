# --- Day 8: Two-Factor Authentication ---

# You come across a door implementing what you can only assume is an
# implementation of two-factor authentication after a long game of requirements
# telephone.

# To get past the door, you first swipe a keycard (no problem; there was one on
# a nearby desk). Then, it displays a code on a little screen, and you type that
# code on a keypad. Then, presumably, the door unlocks.

# Unfortunately, the screen has been smashed. After a few minutes, you've taken
# everything apart and figured out how it works. Now you just have to work out
# what the screen would have displayed.

# The magnetic strip on the card you swiped encodes a series of instructions for
# the screen; these instructions are your puzzle input. The screen is 50 pixels
# wide and 6 pixels tall, all of which start off, and is capable of three
# somewhat peculiar operations:

#     rect AxB turns on all of the pixels in a rectangle at the top-left of the
#     screen which is A wide and B tall.

#     rotate row y=A by B shifts all of the pixels in row A (0 is the top row)
#     right by B pixels. Pixels that would fall off the right end appear at the
#     left end of the row.

#     rotate column x=A by B shifts all of the pixels in column A (0 is the left
#     column) down by B pixels. Pixels that would fall off the bottom appear at
#     the top of the column.

# For example, here is a simple sequence on a smaller screen:

#     rect 3x2 creates a small rectangle in the top-left corner:

#     ###....
#     ###....
#     .......

#     rotate column x=1 by 1 rotates the second column down by one pixel:

#     #.#....
#     ###....
#     .#.....

#     rotate row y=0 by 4 rotates the top row right by four pixels:

#     ....#.#
#     ###....
#     .#.....

#     rotate column x=1 by 1 again rotates the second column down by one pixel,
#     causing the bottom pixel to wrap back to the top:

#     .#..#.#
#     #.#....
#     .#.....

# As you can see, this display technology is extremely powerful, and will soon
# dominate the tiny-code-displaying-screen market. That's what the advertisement
# on the back of the display tries to convince you, anyway.

# There seems to be an intermediate check of the voltage used by the display:
# after you swipe your card, if the screen did work, how many pixels should be
# lit?

# --- Part Two ---

# You notice that the screen is only capable of displaying capital letters; in
# the font it uses, each letter is 5 pixels wide and 6 tall.

# After you swipe your card, what code is the screen trying to display?

import sys
import numpy as np

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day08-input.txt", "r" ) as f:
        data = f.readlines()

    #data = [ 'rect 3x2', 'rotate column x=1 by 1', 'rotate row y=0 by 4', 'rotate column x=1 by 1' ]

    screen = np.zeros( (6,50), dtype=int )
    #screen = np.zeros( (3, 7) )

    for line in data:
        if 'rect' in line:
            line = line.strip().split( 'x' )

            a = int( line[ 0 ].split()[ -1 ] )
            b = int( line[ 1 ][ 0: ] )

            for i in range( a ):
                for j in range( b ):
                    screen[ j, i ] = 1

        else:
            line = line.split( ' by ' )

            l = int( line[ 0 ].split( '=' )[ -1 ] )
            x = int( line[ 1 ].split()[ 0 ] )

            if 'column' in line[ 0 ]:
                screen = rollCol( screen, l, x )
            elif 'row' in line[ 0 ]:
                screen = rollRow( screen, l, x )

    ##
    # Part 1
    ##

    print( f"Part 1 answer: {np.count_nonzero( screen )}" )

    ##
    # Part 2
    ##

    print( f"Part 2 answer:" )
    printScreen( screen )

    
def rollCol( a, c, x ):
    col = a[ :, c ]

    for _ in range( x ):
        col = np.concatenate( ([ col[ -1 ] ], col[ 0:-1 ]) )

    a[ :, c ] = col

    return a

def rollRow( a, r, x ):
    row = a[ r ]

    for _ in range( x ):
        row = np.concatenate( ([ row[ -1 ] ], row[ 0:-1 ]) )

    a[ r ] = row

    return a

def printScreen( a ):
    print( '\n' + '\n'.join( [ ''.join( [ '#' if r == 1 else ' ' for r in row ] ) for row in a ] ) + '\n' )

if __name__ == "__main__":
    main( argv=sys.argv )
