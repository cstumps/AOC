import sys

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day01-input.txt", "r" ) as f:
        data = f.readlines()

    ##
    # Part 1
    ##
    
    data = ''.join( [ line.strip() for line in data ] )
    print( "Part 1 answer: %s" % eval( data ) )

    ##
    # Part 2
    ##

    #print( "Part 2 answer: %s" % (max1 + max2 + max3) )


if __name__ == "__main__":
    main( argv=sys.argv )
