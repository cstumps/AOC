# --- Day 9: Explosives in Cyberspace ---

# Wandering around a secure area, you come across a datalink port to a new part
# of the network. After briefly scanning it for interesting files, you find one
# file in particular that catches your attention. It's compressed with an
# experimental format, but fortunately, the documentation for the format is
# nearby.

# The format compresses a sequence of characters. Whitespace is ignored. To
# indicate that some sequence should be repeated, a marker is added to the file,
# like (10x2). To decompress this marker, take the subsequent 10 characters and
# repeat them 2 times. Then, continue reading the file after the repeated data.
# The marker itself is not included in the decompressed output.

# If parentheses or other characters appear within the data referenced by a
# marker, that's okay - treat it like normal data, not a marker, and then resume
# looking for markers after the decompressed section.

# For example:

#     ADVENT contains no markers and decompresses to itself with no changes,
#     resulting in a decompressed length of 6.

#     A(1x5)BC repeats only the B a total of 5 times, becoming ABBBBBC for a
#     decompressed length of 7.

#     (3x3)XYZ becomes XYZXYZXYZ for a decompressed length of 9.

#     A(2x2)BCD(2x2)EFG doubles the BC and EF, becoming ABCBCDEFEFG for a
#     decompressed length of 11.

#     (6x1)(1x3)A simply becomes (1x3)A - the (1x3) looks like a marker, but
#     because it's within a data section of another marker, it is not treated
#     any differently from the A that comes after it. It has a decompressed
#     length of 6.

#     X(8x2)(3x3)ABCY becomes X(3x3)ABC(3x3)ABCY (for a decompressed length of
#     18), because the decompressed data from the (8x2) marker (the (3x3)ABC) is
#     skipped and not processed further.

# What is the decompressed length of the file (your puzzle input)? Don't count
# whitespace.

# --- Part Two ---

# Apparently, the file actually uses version two of the format.

# In version two, the only difference is that markers within decompressed data
# are decompressed. This, the documentation explains, provides much more
# substantial compression capabilities, allowing many-gigabyte files to be
# stored in only a few kilobytes.

# For example:

#     (3x3)XYZ still becomes XYZXYZXYZ, as the decompressed section contains no
#     markers.

#     X(8x2)(3x3)ABCY becomes XABCABCABCABCABCABCY, because the decompressed
#     data from the (8x2) marker is then further decompressed, thus triggering
#     the (3x3) marker twice for a total of six ABC sequences.

#     (27x12)(20x12)(13x14)(7x10)(1x12)A decompresses into a string of A
#     repeated 241920 times.

#     (25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN becomes 445
#     characters long.

# Unfortunately, the computer you brought probably doesn't have enough memory to
# actually decompress the file; you'll have to come up with another way to get
# its decompressed length.

# What is the decompressed length of the file using this improved format?

import sys

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day09-input.txt", "r" ) as f:
        data = f.readline().strip()

    #data = 'ADVENT'            # ADVENT, 6
    #data = 'A(1x5)BC'          # ABBBBBC, 7
    #data = '(3x3)XYZ'          # XYZXYZXYZ, 9
    #data = 'A(2x2)BCD(2x2)EFG' # ABCBCDEFEFG, 11
    #data = '(6x1)(1x3)A'       # (1x3)A, 6
    #data = 'X(8x2)(3x3)ABCY'   # X(3x3)ABC(3x3)ABCY, 18

    #data = '(3x3)XYZ'                                                 # XYZXYZXYZ
    #data = 'X(8x2)(3x3)ABCY'                                          # XABCABCABCABCABCABCY
    #data = '(27x12)(20x12)(13x14)(7x10)(1x12)A'                       # A 241920 times
    #data = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN' # 445 characters long

    ##
    # Part 1
    ##

    print( f"Part 1 answer: {len( processBytes( data ) )}" )

    ##
    # Part 2
    ##

    # I believe the proper way to solve this is to work on string lengths rather
    # than saving the actual full decomposed string.  Computing power has come
    # a bit since 2016 tho and my machine had no problem.

    print( f"Part 2 answer: {len( processBytes( data, recurse=True ) ) }" )


def processBytes( bytes, recurse=False ):
    outStr = ""
    i = 0

    while i < len( bytes ):
        if bytes[ i ] == '(':
            exp = ''
            i += 1 # Get past the paren

            # Get the expression
            while bytes[ i ] != ')':
                exp += bytes[ i ]
                i += 1

            count = int( exp.split( 'x' )[ 0 ] )
            repeat = int( exp.split( 'x' )[ 1 ] )

            i += 1 # Get past the paren
            exp = ''

            # Read in what needs to repeat
            for j in range( count ):
                exp += bytes[ i + j ]

            # Advance the counter
            i += j

            # Perform the repeat recursively
            if recurse:
                exp = processBytes( exp, recurse=True )
                
            for j in range( repeat ):
                outStr += exp

        else:
            outStr += bytes[ i ]
            
        i += 1

    return outStr


if __name__ == "__main__":
    main( argv=sys.argv )
