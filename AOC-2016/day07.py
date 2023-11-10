# --- Day 7: Internet Protocol Version 7 ---

# While snooping around the local network of EBHQ, you compile a list of IP
# addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to
# figure out which IPs support TLS (transport-layer snooping).

# An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA.
# An ABBA is any four-character sequence which consists of a pair of two
# different characters followed by the reverse of that pair, such as xyyx or
# abba. However, the IP also must not have an ABBA within any hypernet
# sequences, which are contained by square brackets.

# For example:

#     abba[mnop]qrst supports TLS (abba outside square brackets).

#     abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even
#     though xyyx is outside square brackets).

#     aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior
#     characters must be different).

#     ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even
#     though it's within a larger string).

# How many IPs in your puzzle input support TLS?

# --- Part Two ---

# You would also like to know which IPs support SSL (super-secret listening).

# An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in
# the supernet sequences (outside any square bracketed sections), and a
# corresponding Byte Allocation Block, or BAB, anywhere in the hypernet
# sequences. An ABA is any three-character sequence which consists of the same
# character twice with a different character between them, such as xyx or aba. A
# corresponding BAB is the same characters but in reversed positions: yxy and
# bab, respectively.

# For example:

#     aba[bab]xyz supports SSL (aba outside square brackets with corresponding
#     bab within square brackets).

#     xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).

#     aaa[kek]eke supports SSL (eke in supernet with corresponding kek in
#     hypernet; the aaa sequence is not related, because the interior character
#     must be different).

#     zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a
#     corresponding bzb, even though zaz and zbz overlap).

# How many IPs in your puzzle input support SSL?

import sys
import re

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day07-input.txt", "r" ) as f:
        data = f.readlines()

    ##
    # Part 1
    ##

    #data = [ 'abba[mnop]qrst', 'abcd[bddb]xyyx', 'aaaa[qwer]tyui', 'ioxxoj[asdfgh]zxcvbn' ]
    #data = [ 'aba[bab]xyz', 'xyx[xyx]xyx', 'aaa[kek]eke', 'zazbz[bzb]cdb' ]
    #data = [ 'zazbz[bzb]cdb' ]

    valid = 0

    for entry in data:
        seq = re.sub( r"\[.+?\]", ' ', entry.strip() ).split()
        hyper = re.findall( r"\[(.+?)\]", entry.strip() )
        
        for s in seq:
            if hasAbba( s ):
                for h in hyper:
                    if hasAbba( h ):
                        break
                else:
                    valid += 1
                    break

    print( f"Part 1 answer: {valid}" )

    ##
    # Part 2
    ##

    # Incorrect values:  208 (too low), 259 (too high)

    valid = 0
    
    for entry in data:
        seq = re.sub( r"\[.+?\]", ' ', entry.strip() ).split()
        hyper = re.findall( r"\[(.+?)\]", entry.strip() )

        ssl = False

        for s in seq:
            bab = getBab( s )

            for b in bab:
                for h in hyper:
                    if b in h:
                        ssl = True

        if ssl:
            valid += 1

    print( f"Part 2 answer: {valid}" )


def hasAbba( seq ):
    for i in range( len( seq ) - 3 ):
        lh = seq[ i:i+2 ]
        rh = seq[ i+2:i+4 ][ ::-1 ]

        if (lh == rh) and (lh[ 0 ] != lh[ 1 ]):
            return True
        
    return False

def getBab( seq ):
    res = []

    for i in range( len( seq ) - 2 ):
        aba = seq[ i:i+3 ]

        if aba[ 0 ] == aba[ 2 ] and aba[ 0 ] != aba[ 1 ]:
            res.append( aba[1] + aba[0] + aba[1] )
        
    return res


if __name__ == "__main__":
    main( argv=sys.argv )
