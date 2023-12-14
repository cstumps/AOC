import sys

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day01-input.txt", "r" ) as f:
        data = [ line.rstrip( '\n' ) for line in f ]

    ##
    # Part 1
    ##
    
    joined = ''.join( [ line for line in data ] )
    print( f"Part 1 answer: {eval( joined )}" )

    ##
    # Part 2
    ##

    # This is sort of odd:  Using a list instead of a set doesn't
    # compelete in any amount of time I'm willing to wait for.

    i = 0
    val = 0

    totals = set()
    totals.add( 0 )

    while True:
        val += int( data[ i % len( data ) ] )

        if val in totals:
            break

        totals.add( val )
        i += 1

    print( f"Part 2 answer: {val}" )


if __name__ == "__main__":
    main( argv=sys.argv )
