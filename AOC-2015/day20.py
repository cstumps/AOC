# --- Day 20: Infinite Elves and Infinite Houses ---

# To keep the Elves busy, Santa has them deliver some presents by hand,
# door-to-door. He sends them down a street with infinite houses numbered
# sequentially: 1, 2, 3, 4, 5, and so on.

# Each Elf is assigned a number, too, and delivers presents to houses based on
# that number:

#     The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5, ....
#     The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10, ....
#     Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15, ....

# There are infinitely many Elves, numbered starting with 1. Each Elf delivers
# presents equal to ten times his or her number at each house.

# So, the first nine houses on the street end up like this:

# House 1 got 10 presents.
# House 2 got 30 presents.
# House 3 got 40 presents.
# House 4 got 70 presents.
# House 5 got 60 presents.
# House 6 got 120 presents.
# House 7 got 80 presents.
# House 8 got 150 presents.
# House 9 got 130 presents.

# The first house gets 10 presents: it is visited only by Elf 1, which delivers
# 1 * 10 = 10 presents. The fourth house gets 70 presents, because it is visited
# by Elves 1, 2, and 4, for a total of 10 + 20 + 40 = 70 presents.

# What is the lowest house number of the house to get at least as many presents
# as the number in your puzzle input?

# Your puzzle input is 36000000.

# --- Part Two ---

# The Elves decide they don't want to visit an infinite number of houses.
# Instead, each Elf will stop after delivering presents to 50 houses. To make up
# for it, they decide to deliver presents equal to eleven times their number at
# each house.

# With these changes, what is the new lowest house number of the house to get at
# least as many presents as the number in your puzzle input?

import sys
import numpy as np
import math

def main( argv ):

    data = 36000000

    ##
    # Part 1
    ##
    
    houses = sieve( 1000000, 10, None, data )

    print( f"Part 1 answer: {houses}" )

    ##
    # Part 2
    ##

    houses = sieve( 1000000, 11, 50, data )

    print( f"Part 2 answer: {houses}" )

# So I struggled with this one.  There was a solution on reddit that referenced the Sieve of 
# Eratosthenes:
#
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
#
# Though I understand it now, I created this using both the wiki and someones example code.
def sieve( numHouses, giftsPerHouse, giftQuota, targetGifts ):
    housesAtTarget = set( [] )

    # Create our lists of addresses to deliver to based on the passed in number of houses
    houses = [ address * giftsPerHouse for address in range( numHouses + 1 ) ]
  
    # For each elf
    for elf in range( 2, numHouses ):
        # If there is a quota / max number of houses to visit, constrain to that
        if giftQuota:
            maxHouse = min( elf * giftQuota, numHouses )
        else:
            maxHouse = numHouses

        # Deliver packges to the houses it's responsible for
        for address in range( elf * 2, maxHouse, elf ):
            houses[ address ] += elf * giftsPerHouse

            if houses[ address ] >= targetGifts:
                housesAtTarget.add( address )

    return min( housesAtTarget )

if __name__ == "__main__":
    main( argv=sys.argv )