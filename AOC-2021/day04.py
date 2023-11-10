# --- Day 4: Giant Squid ---

# You're already almost 1.5km (almost a mile) below the surface of the ocean,
# already so deep that you can't see any sunlight. What you can see, however, is
# a giant squid that has attached itself to the outside of your submarine.

# Maybe it wants to play bingo?

# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers.
# Numbers are chosen at random, and the chosen number is marked on all boards on
# which it appears. (Numbers may not appear on all boards.) If all numbers in
# any row or any column of a board are marked, that board wins. (Diagonals don't
# count.)

# The submarine has a bingo subsystem to help passengers (currently, you and the
# giant squid) pass the time. It automatically generates a random order in which
# to draw numbers and a random set of boards (your puzzle input). For example:

# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7

# After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no
# winners, but the boards are marked as follows (shown here adjacent to each
# other to save space):

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

# After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are
# still no winners:

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

# Finally, 24 is drawn:

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

# At this point, the third board wins because it has at least one complete row
# or column of marked numbers (in this case, the entire top row is marked: 14 21
# 17 24 4).

# The score of the winning board can now be calculated. Start by finding the sum
# of all unmarked numbers on that board; in this case, the sum is 188. Then,
# multiply that sum by the number that was just called when the board won, 24,
# to get the final score, 188 * 24 = 4512.

# To guarantee victory against the giant squid, figure out which board will win
# first. What will your final score be if you choose that board?

# --- Part Two ---

# On the other hand, it might be wise to try a different strategy: let the giant
# squid win.

# You aren't sure how many bingo boards a giant squid could play at once, so
# rather than waste time counting its arms, the safe thing to do is to figure
# out which board will win last and choose that one. That way, no matter which
# boards it picks, it will win for sure.

# In the above example, the second board is the last to win, which happens after
# 13 is eventually called and its middle column is completely marked. If you
# were to keep playing until this point, the second board would have a sum of
# unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

# Figure out which board will win last. Once it wins, what would its final score
# be?


import sys
from math import prod

def main( argv ):

    cards = []
    winMasks = []
    winStates = [ 
                 [ [ 1, 1, 1, 1, 1 ], [ 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0 ] ], # Row 1
                 [ [ 0, 0, 0, 0, 0 ], [ 1, 1, 1, 1, 1 ], [ 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0 ] ], # Row 2
                 [ [ 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0 ], [ 1, 1, 1, 1, 1 ], [ 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0 ] ], # Row 3
                 [ [ 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0 ], [ 1, 1, 1, 1, 1 ], [ 0, 0, 0, 0, 0 ] ], # Row 4
                 [ [ 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0 ], [ 1, 1, 1, 1, 1 ] ], # Row 5

                 [ [ 1, 0, 0, 0, 0 ], [ 1, 0, 0, 0, 0 ], [ 1, 0, 0, 0, 0 ], [ 1, 0, 0, 0, 0 ], [ 1, 0, 0, 0, 0 ] ], # Col 1
                 [ [ 0, 1, 0, 0, 0 ], [ 0, 1, 0, 0, 0 ], [ 0, 1, 0, 0, 0 ], [ 0, 1, 0, 0, 0 ], [ 0, 1, 0, 0, 0 ] ], # Col 2
                 [ [ 0, 0, 1, 0, 0 ], [ 0, 0, 1, 0, 0 ], [ 0, 0, 1, 0, 0 ], [ 0, 0, 1, 0, 0 ], [ 0, 0, 1, 0, 0 ] ], # Col 3
                 [ [ 0, 0, 0, 1, 0 ], [ 0, 0, 0, 1, 0 ], [ 0, 0, 0, 1, 0 ], [ 0, 0, 0, 1, 0 ], [ 0, 0, 0, 1, 0 ] ], # Col 4
                 [ [ 0, 0, 0, 0, 1 ], [ 0, 0, 0, 0, 1 ], [ 0, 0, 0, 0, 1 ], [ 0, 0, 0, 0, 1 ], [ 0, 0, 0, 0, 1 ] ]  # Col 5
               ]

    # Read in input file
    with open( "input/day04-input.txt", "r" ) as f:
        # Values to call
        callVals = [ int( i ) for i in f.readline().split( ',' ) ]
        card = []

        # Cards
        for line in f:
            line = line.strip()
        
            if not line:
                if len( card ):
                    cards.append( BingoCard( card ) )
                    card.clear()
            else:
                card.append( [ int( l ) for l in line.split() ] )

        cards.append( BingoCard( card ) )

    # Compute hashes of the win states
    for win in winStates:
        b = BitArray()

        for col in range( len( win ) ):
            for row in range( len( win[ col ] ) ):
                if win[ col ][ row ]:
                    b.setBit( row, col )

        winMasks.append( b )

    ##
    # Part 1
    ##

    # For each val, go thru the bingo cards and mark them.  After each val check for a winning card.
    finalScore = 0

    for val in callVals:
        for card in cards:
            card.markCard( val )

            if ( card.checkWin( winMasks ) ):
                finalScore = card.scoreCard() * val
                break
        else:
            continue
        break

    print( "Part 1 answer: %s" % finalScore )

    ##
    # Part 2
    ##

    # Reset from part 1
    for card in cards:
        card.reset()

    winCount = 0

    for val in callVals:
        for card in cards:
            card.markCard( val )

            if ( not card.winner and card.checkWin( winMasks ) ) :
                card.winner = True
                winCount += 1

                # Last winning card found
                if winCount == len( cards ):
                    finalScore = card.scoreCard() * val
                    break
        else:
            continue
        break

    print( "Part 2 answer: %s" % finalScore )

class BingoCard( object ):
    def __init__( self, card ):
        self.card = card.copy()
        self.cardState = BitArray()
        self.winner = False

    def __str__( self ):
        return '\n'.join( [ ' '.join( [ str( r ).rjust( 2, ' ' ) for r in row ] ) for  row in self.card ] ) + '\n'

    def markCard( self, value ):
        for i, row in enumerate( self.card ):
            try:
                index = row.index( value )
                self.cardState.setBit( index, i )
            except ValueError:
                pass

    def checkWin( self, winMasks ):
        for w in winMasks:
            if w == (self.cardState & w):
                return True
            
        return False

    # Sum up all unmarked numbers
    def scoreCard( self ):
        unmarkedSum = 0
        
        for col in range( len( self.card ) ):
            for row in range( len( self.card[ col ] ) ):
                if not self.cardState.isSet( row, col ):
                    unmarkedSum += self.card[ col ][ row ]
        
        return unmarkedSum

    def reset( self ):
        self.cardState.reset()



class BitArray( object ):
    def __init__( self, val=0 ):
        self.data = val

    def __eq__( self, other ):
        return self.data == other.data

    def __and__( self, other ):
        return BitArray( self.data & other.data )

    def __str__( self ):
        return str( self.data )

    def setBit( self, row, col ):
        self.data |= (1 << ((row * 5) + col))

    def isSet( self, row, col ):
        return self.data & (1 << ((row * 5) + col))

    def reset( self, val=0 ):
        self.data = val

if __name__ == "__main__":
    main( argv=sys.argv )