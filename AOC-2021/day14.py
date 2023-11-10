# --- Day 14: Extended Polymerization ---

# The incredible pressures at this depth are starting to put a strain on your
# submarine. The submarine has polymerization equipment that would produce
# suitable materials to reinforce the submarine, and the nearby
# volcanically-active caves should even have the necessary input elements in
# sufficient quantities.

# The submarine manual contains instructions for finding the optimal polymer
# formula; specifically, it offers a polymer template and a list of pair
# insertion rules (your puzzle input). You just need to work out what polymer
# would result after repeating the pair insertion process a few times.

# For example:

# NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C

# The first line is the polymer template - this is the starting point of the
# process.

# The following section defines the pair insertion rules. A rule like AB -> C
# means that when elements A and B are immediately adjacent, element C should be
# inserted between them. These insertions all happen simultaneously.

# So, starting with the polymer template NNCB, the first step simultaneously
# considers all three pairs:

#     The first pair (NN) matches the rule NN -> C, so element C is inserted
#     between the first N and the second N.

#     The second pair (NC) matches the rule NC -> B, so element B is inserted
#     between the N and the C.

#     The third pair (CB) matches the rule CB -> H, so element H is inserted
#     between the C and the B.

# Note that these pairs overlap: the second element of one pair is the first
# element of the next pair. Also, because all pairs are considered
# simultaneously, inserted elements are not considered to be part of a pair
# until the next step.

# After the first step of this process, the polymer becomes NCNBCHB.

# Here are the results of a few steps using the above rules:

# Template:     NNCB
# After step 1: NCNBCHB
# After step 2: NBCCNBBBCBHCB
# After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
# After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB

# This polymer grows quickly. After step 5, it has length 97; After step 10, it
# has length 3073. After step 10, B occurs 1749 times, C occurs 298 times, H
# occurs 161 times, and N occurs 865 times; taking the quantity of the most
# common element (B, 1749) and subtracting the quantity of the least common
# element (H, 161) produces 1749 - 161 = 1588.

# Apply 10 steps of pair insertion to the polymer template and find the most and
# least common elements in the result. What do you get if you take the quantity
# of the most common element and subtract the quantity of the least common
# element?

# --- Part Two ---

# The resulting polymer isn't nearly strong enough to reinforce the submarine.
# You'll need to run more steps of the pair insertion process; a total of 40
# steps should do it.

# In the above example, the most common element is B (occurring 2192039569602
# times) and the least common element is H (occurring 3849876073 times);
# subtracting these produces 2188189693529.

# Apply 40 steps of pair insertion to the polymer template and find the most and
# least common elements in the result. What do you get if you take the quantity
# of the most common element and subtract the quantity of the least common
# element?

import sys
import itertools
import string

def main( argv ):

    # Read in input file
    with open( "input/day14-input.txt", "r" ) as f:
        template = list( f.readline().strip() )
        recipes = {}

        for p in f:
            if len( p.strip() ):
                p = p.split()
                recipes[ p[ 0 ].strip() ] = Recipe( p[ 0 ].strip(), p[ 2 ].strip() )

    #template = list( 'NNCB' )
    #recipes = { 'CH': Recipe( 'CH', 'B' ),
    #            'HH': Recipe( 'HH', 'N' ),
    #            'CB': Recipe( 'CB', 'H' ),
    #            'NH': Recipe( 'NH', 'C' ),
    #            'HB': Recipe( 'HB', 'C' ),
    #            'HC': Recipe( 'HC', 'B' ),
    #            'HN': Recipe( 'HN', 'C' ),
    #            'NN': Recipe( 'NN', 'C' ),
    #            'BH': Recipe( 'BH', 'H' ),
    #            'NC': Recipe( 'NC', 'B' ),
    #            'NB': Recipe( 'NB', 'B' ),
    #            'BN': Recipe( 'BN', 'B' ),
    #            'BB': Recipe( 'BB', 'N' ),
    #            'BC': Recipe( 'BC', 'B' ),
    #            'CC': Recipe( 'CC', 'N' ),
    #            'CN': Recipe( 'CN', 'C' ) }

    ##
    # Part 1
    ##

    print( "Part 1 answer: %s" % runLoops( template, recipes, 10 ) )

    ##
    # Part 2
    ##

    for r in recipes.keys():
        recipes[ r ].reset()

    print( "Part 2 answer: %s" % runLoops( template, recipes, 40 ) )


class Recipe( object ):
    def __init__( self, start, end ):
        self.start = start
        self.end = end

        self.next = [ start[ 0 ] + end, end + start[ 1 ] ]
        self.count = 0
        self.nextCount = 0

    def reset( self ):
        self.count = 0
        self.nextCount = 0

def runLoops( template, recipes, loops ):
    # Init freq table
    freq = { i: 0 for i in list( string.ascii_uppercase ) }

    for x in template:
        freq[ x ] += 1

    # Init with the template
    for x in pairwise( template ):
        recipes[ x[ 0 ] + x[ 1 ] ].count += 1

    # Run the loops
    for loop in range( loops ):
        # Stage the update
        for r in recipes.keys():
            if recipes[ r ].count:
                recipes[ recipes[ r ].next[ 0 ] ].nextCount += recipes[ r ].count
                recipes[ recipes[ r ].next[ 1 ] ].nextCount += recipes[ r ].count

                freq[ recipes[ r ].end ] += recipes[ r ].count

        # Process the update
        for r in recipes.keys():
            recipes[ r ].count = recipes[ r ].nextCount
            recipes[ r ].nextCount = 0

    # Tally the counts
    minChar = min( i for i in freq.values() if i > 0 )
    maxChar = max( freq.values() )

    return maxChar - minChar

def pairwise( iterable ):
    a, b = itertools.tee( iterable )
    next( b, None )

    return zip( a, b )
            

if __name__ == "__main__":
    main( argv=sys.argv )