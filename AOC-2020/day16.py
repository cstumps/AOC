# --- Day 16: Ticket Translation ---

# As you're walking to yet another connecting flight, you realize that one of
# the legs of your re-routed trip coming up is on a high-speed train. However,
# the train ticket you were given is in a language you don't understand. You
# should probably figure out what it says before you get to the train station
# after the next flight.

# Unfortunately, you can't actually read the words on the ticket. You can,
# however, read the numbers, and so you figure out the fields these tickets must
# have and the valid ranges for values in those fields.

# You collect the rules for ticket fields, the numbers on your ticket, and the
# numbers on other nearby tickets for the same train service (via the airport
# security cameras) together into a single document you can reference (your
# puzzle input).

# The rules for ticket fields specify a list of fields that exist somewhere on
# the ticket and the valid ranges of values for each field. For example, a rule
# like class: 1-3 or 5-7 means that one of the fields in every ticket is named
# class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3
# and 5 are both valid in this field, but 4 is not).

# Each ticket is represented by a single line of comma-separated values. The
# values are the numbers on the ticket in the order they appear; every ticket
# has the same format. For example, consider this ticket:

# .--------------------------------------------------------.
# | ????: 101    ?????: 102   ??????????: 103     ???: 104 |
# |                                                        |
# | ??: 301  ??: 302             ???????: 303      ??????? |
# | ??: 401  ??: 402           ???? ????: 403    ????????? |
# '--------------------------------------------------------'

# Here, ? represents text in a language you don't understand. This ticket might
# be represented as 101,102,103,104,301,302,303,401,402,403; of course, the
# actual train tickets you're looking at are much more complicated. In any case,
# you've extracted just the numbers in such a way that the first number is
# always the same specific field, the second number is always a different
# specific field, and so on - you just don't know what each position actually
# means!

# Start by determining which tickets are completely invalid; these are tickets
# that contain values which aren't valid for any field. Ignore your ticket for
# now.

# For example, suppose you have the following notes:

# class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50

# your ticket:
# 7,1,14

# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12

# It doesn't matter which position corresponds to which field; you can identify
# invalid nearby tickets by considering only whether tickets contain values that
# are not valid for any field. In this example, the values on the first nearby
# ticket are all valid for at least one field. This is not true of the other
# three nearby tickets: the values 4, 55, and 12 are are not valid for any
# field. Adding together all of the invalid values produces your ticket scanning
# error rate: 4 + 55 + 12 = 71.

# Consider the validity of the nearby tickets you scanned. What is your ticket
# scanning error rate?

# --- Part Two ---

# Now that you've identified which tickets contain invalid values, discard those
# tickets entirely. Use the remaining valid tickets to determine which field is
# which.

# Using the valid ranges for each field, determine what order the fields appear
# on the tickets. The order is consistent between all tickets: if seat is the
# third field, it is the third field on every ticket, including your ticket.

# For example, suppose you have the following notes:

# class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19

# your ticket:
# 11,12,13

# nearby tickets:
# 3,9,18
# 15,1,5
# 5,14,9

# Based on the nearby tickets in the above example, the first position must be
# row, the second position must be class, and the third position must be seat;
# you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

# Once you work out which field is which, look for the six fields on your ticket
# that start with the word departure. What do you get if you multiply those six
# values together?

import sys 
import re 

def main( argv ):

    ruleRegex = re.compile( "^(.+?): (\d*)-(\d*) or (\d*)-(\d*)$" )

    # Read in input file
    with open( "input/day16-input.txt", "r" ) as f:
        data = [ line.rstrip() for line in f ]

    # data = [ 'class: 1-3 or 5-7',
    #          'row: 6-11 or 33-44',
    #          'seat: 13-40 or 45-50',
    #          '',
    #          'your ticket:',
    #          '7,1,14',
    #          '',
    #          'nearby tickets:',
    #          '7,3,47',
    #          '40,4,50',
    #          '55,2,20',
    #          '38,6,12' ]

    # data = [ 'class: 0-1 or 4-19',
    #           'row: 0-5 or 8-19',
    #           'seat: 0-13 or 16-19',
    #           '',
    #           'your ticket:',
    #           '11,12,13',
    #           '',
    #           'nearby tickets:',
    #           '3,9,18',
    #           '15,1,5',
    #           '5,14,9' ]

    # Parse out rules
    rules = [ Rule( m.group(1),
                    m.group(2),
                    m.group(3),
                    m.group(4),
                    m.group(5) ) for l in data for m in [ ruleRegex.search( l ) ] if m ]

    # Part 1

    # Check for invalid tickets
    invCount = 0
    validTickets = []
    delList = []

    i = data.index( 'nearby tickets:' )

    for t in data[ i+1: ]:
        for val in t.split( ',' ):
            for r in rules:
                if r.inRange( val ):
                    break
            else: # No rule matches this value
                invCount += int( val )
                delList.append( t )

    validTickets = [ t.split( ',' ) for t in data[ i+1: ] if t not in delList ]

    print( "Part 1 answer: %s" % invCount )

    # Part 2

    # Initialize a dictionary of lists for each rule.  This dictionary will record for
    # a given rule (key), the counts per position that it passed.
    rulesDict = { r: [0] * 20 for r in rules }

    for t in validTickets:
        for i, val in enumerate( t ):
            for r in rules:
                if r.inRange( val ):
                    rulesDict[ r ][ i ] += 1 # Record the position that passed

    # We should now be able to search the rules dict for the positions where each rule
    # passed on all the tickets
    rulesVerified = 0

    while rulesVerified != len( rules ):
        for r in rulesDict.keys():
            # For each rule position list, if the rule is the only one thatapplied, we now 
            # know what position the rule applies to
            if rulesDict[ r ].count( len( validTickets ) ) == 1:
                r.pos = rulesDict[ r ].index( len( validTickets ) )
                rulesVerified += 1

                # Now go through and invalidate that position for all rules
                for s in rulesDict.keys():
                    rulesDict[ s ][ r.pos ] = 0
    
    # Finally, get our ticket and look up the fields that we care about
    ticket = data[ data.index( 'your ticket:' ) + 1 ].split( ',' )
    ans = 1

    for r in rules:
        if 'departure' in r.name:
            ans *= int( ticket[ r.pos ] )

    print( "Part 2 answer: %s" % ans )


class Rule( object ):
    def __init__( self, name, minRangeL, minRangeH, maxRangeL, maxRangeH ):
        self.name = name
        self.minStart = int( minRangeL )
        self.minStop  = int( minRangeH )
        self.maxStart = int( maxRangeL )
        self.maxStop  = int( maxRangeH )
        self.pos      = None

    def __str__( self ):
        return "%s" % (self.name)

    def __eq__( self, other ):
        return (self.name == other.name)

    def __hash__( self ):
        return hash( str( self ) )

    def inRange( self, val ):
        return (self.minStart <= int( val ) <= self.minStop) or (self.maxStart <= int( val ) <= self.maxStop)


if __name__ == "__main__":
    main( argv=sys.argv )