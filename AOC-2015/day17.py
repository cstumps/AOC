# --- Day 17: No Such Thing as Too Much ---

# The elves bought too much eggnog again - 150 liters this time. To fit it all
# into your refrigerator, you'll need to move it into smaller containers. You
# take an inventory of the capacities of the available containers.

# For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters.
# If you need to store 25 liters, there are four ways to do it:

#     15 and 10
#     20 and 5 (the first 5)
#     20 and 5 (the second 5)
#     15, 5, and 5

# Filling all containers entirely, how many different combinations of containers
# can exactly fit all 150 liters of eggnog?

# --- Part Two ---

# While playing with all the containers in the kitchen, another load of eggnog
# arrives! The shipping and receiving department is requesting as many
# containers as you can spare.

# Find the minimum number of containers that can exactly fit all 150 liters of
# eggnog. How many different ways can you fill that number of containers and
# still hold exactly 150 litres?

# In the example above, the minimum number of containers was two. There were
# three ways to use that many containers, and so the answer there would be 3.

import sys
import itertools as it
import numpy as np

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day17-input.txt", "r" ) as f:
        data = f.readlines()

    data = [ int( line.strip() ) for line in data ]
    target = 150

    #data     = [ 20, 15, 10, 5, 5 ]
    indicies = [ i for i in range( len( data ) ) ]
    #target   = 25

    ##
    # Part 1
    ##

    count = 0
    validSeq = []

    for i in range( len( data ) ):
        for seq in it.combinations( indicies, i ):
            numbers = np.array( [ data[ n ] for n in seq ] )

            if numbers.sum() == target:
                validSeq.append( numbers )
                count += 1

    print( f"Part 1 answer: {count}" )

    ##
    # Part 2
    ##

    minLength = sorted( [ len( s ) for s in validSeq ] )[ 0 ]
    smallSeq = [ tuple( s ) for s in validSeq if len( s ) == minLength ]

    print( f"Part 2 answer: {len( smallSeq )}" )

if __name__ == "__main__":
    main( argv=sys.argv )