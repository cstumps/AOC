# --- Day 4: The Ideal Stocking Stuffer ---

# Santa needs help mining some AdventCoins (very similar to bitcoins) to use as
# gifts for all the economically forward-thinking little girls and boys.

# To do this, he needs to find MD5 hashes which, in hexadecimal, start with at
# least five zeroes. The input to the MD5 hash is some secret key (your puzzle
# input, given below) followed by a number in decimal. To mine AdventCoins, you
# must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...)
# that produces such a hash.

# For example:

#     If your secret key is abcdef, the answer is 609043, because the MD5 hash
#     of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the
#     lowest such number to do so.

#     If your secret key is pqrstuv, the lowest number it combines with to make
#     an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of
#     pqrstuv1048970 looks like 000006136ef....

# Your puzzle input is iwrupvqb.

# --- Part Two ---

# Now find one that starts with six zeroes.

import sys
import hashlib

def main( argv ):

    data = 'iwrupvqb'

    ##
    # Part 1
    ##

    i = 0
 
    while True:
        md5 = hashlib.md5( (data + str( i )).encode() ).hexdigest()
        
        if md5[ :5 ] == '00000':
            break

        i += 1

    print( f"Part 1 answer: {i}" )

    ##
    # Part 2
    ##

    # Brute force works here in part because we're 8 years down the road from when this puzzle
    # came out.  A hint I saw suggested leveraging rot-13 to tackle this in a quicker amount of
    # time.

    while True:
        md5 = hashlib.md5( (data + str( i )).encode() ).hexdigest()
        
        if md5[ :6 ] == '000000':
            break

        i += 1

    print( f"Part 1 answer: {i}" )


if __name__ == "__main__":
    main( argv=sys.argv )