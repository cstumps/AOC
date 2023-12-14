# --- Day 12: Hot Springs ---

# You finally reach the hot springs! You can see steam rising from secluded
# areas attached to the primary, ornate building.

# As you turn to enter, the researcher stops you. "Wait - I thought you were
# looking for the hot springs, weren't you?" You indicate that this definitely
# looks like hot springs to you.

# "Oh, sorry, common mistake! This is actually the onsen! The hot springs are
# next door."

# You look in the direction the researcher is pointing and suddenly notice the
# massive metal helixes towering overhead. "This way!"

# It only takes you a few more steps to reach the main gate of the massive
# fenced-off area containing the springs. You go through the gate and into a
# small administrative building.

# "Hello! What brings you to the hot springs today? Sorry they're not very hot
# right now; we're having a lava shortage at the moment." You ask about the
# missing machine parts for Desert Island.

# "Oh, all of Gear Island is currently offline! Nothing is being manufactured at
# the moment, not until we get more lava to heat our forges. And our springs.
# The springs aren't very springy unless they're hot!"

# "Say, could you go up and see why the lava stopped flowing? The springs are
# too cold for normal operation, but we should be able to find one springy
# enough to launch you up there!"

# There's just one problem - many of the springs have fallen into disrepair, so
# they're not actually sure which springs would even be safe to use! Worse yet,
# their condition records of which springs are damaged (your puzzle input) are
# also damaged! You'll need to help them repair the damaged records.

# In the giant field just outside, the springs are arranged into rows. For each
# row, the condition records show every spring and whether it is operational (.)
# or damaged (#). This is the part of the condition records that is itself
# damaged; for some springs, it is simply unknown (?) whether the spring is
# operational or damaged.

# However, the engineer that produced the condition records also duplicated some
# of this information in a different format! After the list of springs for a
# given row, the size of each contiguous group of damaged springs is listed in
# the order those groups appear in the row. This list always accounts for every
# damaged spring, and each number is the entire size of its contiguous group
# (that is, groups are always separated by at least one operational spring: ####
# would always be 4, never 2,2).

# So, condition records with no unknown spring conditions might look like this:

# #.#.### 1,1,3
# .#...#....###. 1,1,3
# .#.###.#.###### 1,3,1,6
# ####.#...#... 4,1,1
# #....######..#####. 1,6,5
# .###.##....# 3,2,1

# However, the condition records are partially damaged; some of the springs'
# conditions are actually unknown (?). For example:

# ???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1

# Equipped with this information, it is your job to figure out how many
# different arrangements of operational and broken springs fit the given
# criteria in each row.

# In the first line (???.### 1,1,3), there is exactly one way separate groups of
# one, one, and three broken springs (in that order) can appear in that row: the
# first three unknown springs must be broken, then operational, then broken
# (#.#), making the whole row #.#.###.

# The second line is more interesting: .??..??...?##. 1,1,3 could be a total of
# four different arrangements. The last ? must always be broken (to satisfy the
# final contiguous group of three broken springs), and each ?? must hide exactly
# one of the two broken springs. (Neither ?? could be both broken springs or
# they would form a single contiguous group of two; if that were true, the
# numbers afterward would have been 2,3 instead.) Since each ?? can either be #.
# or .#, there are four possible arrangements of springs.

# The last line is actually consistent with ten different arrangements! Because
# the first number is 3, the first and second ? must both be . (if either were
# #, the first number would have to be 4 or higher). However, the remaining run
# of unknown spring conditions have many different ways they could hold groups
# of two and one broken springs:

# ?###???????? 3,2,1
# .###.##.#...
# .###.##..#..
# .###.##...#.
# .###.##....#
# .###..##.#..
# .###..##..#.
# .###..##...#
# .###...##.#.
# .###...##..#
# .###....##.#

# In this example, the number of possible arrangements for each row is:

#     ???.### 1,1,3 - 1 arrangement
#     .??..??...?##. 1,1,3 - 4 arrangements
#     ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
#     ????.#...#... 4,1,1 - 1 arrangement
#     ????.######..#####. 1,6,5 - 4 arrangements
#     ?###???????? 3,2,1 - 10 arrangements

# Adding all of the possible arrangement counts together produces a total of 21
# arrangements.

# For each row, count all of the different arrangements of operational and
# broken springs that meet the given criteria. What is the sum of those counts?

# --- Part Two ---

# As you look out at the field of springs, you feel like there are way more
# springs than the condition records list. When you examine the records, you
# discover that they were actually folded up this whole time!

# To unfold the records, on each row, replace the list of spring conditions with
# five copies of itself (separated by ?) and replace the list of contiguous
# groups of damaged springs with five copies of itself (separated by ,).

# So, this row:

# .# 1

# Would become:

# .#?.#?.#?.#?.# 1,1,1,1,1

# The first line of the above example would become:

# ???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3

# In the above example, after unfolding, the number of possible arrangements for
# some rows is now much larger:

#     ???.### 1,1,3 - 1 arrangement
#     .??..??...?##. 1,1,3 - 16384 arrangements
#     ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
#     ????.#...#... 4,1,1 - 16 arrangements
#     ????.######..#####. 1,6,5 - 2500 arrangements
#     ?###???????? 3,2,1 - 506250 arrangements

# After unfolding, adding all of the possible arrangement counts together
# produces 525152.

# Unfold your condition records; what is the new sum of possible arrangement
# counts?

import sys
import itertools as it
import functools

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day12-input.txt", "r" ) as f:
        data = [ line.rstrip( '\n' ) for line in f ]

  
    #data = [ '???.### 1,1,3',
    #         '.??..??...?##. 1,1,3',
    #         '?#?#?#?#?#?#?#? 1,3,1,6',
    #         '????.#...#... 4,1,1',
    #         '????.######..#####. 1,6,5',
    #         '?###???????? 3,2,1' ]

    templates = []

    for line in data:
        line = line.split()
        
        str = line[ 0 ]
        pattern = [ int( v ) for v in line[ 1 ].split( ',' ) ]

        templates.append( [ str, pattern ] )

    ##
    # Part 1
    ##

    arr = 0

    for t in templates:
        arr += checkString( t[ 0 ], tuple( t[ 1 ] ) )

        # Calls old functions that while they do work for part 1,
        # aren't work crap for part 2.

        # opt = findOptions( t[ 1 ], len( t[ 0 ] ) )

        # for o in opt:
        #     if validString( o, t[ 0 ] ):
        #         arr += 1

    print( f"Part 1 answer: {arr}" )

    ##
    # Part 2
    ##

    arr = 0

    # First expand the templates
    for t in templates:
        pattern = t[ 1 ] * 5
        t = t[ 0 ] + (('?' + t[ 0 ]) * 4)

        arr += checkString( t, tuple( pattern ) )

    print( f"Part 2 answer: {arr}" )


# A post on reddit got me on the right track with this function.  I had to add other conditionals and debug it.
# The logic here could probably be cleaner and reduced however it works as-is.  It's amazing how much the 
# caching makes a difference.  Goes from something that won't complete for hours to something that completes 
# in less than 5 seconds.

@functools.lru_cache(maxsize=None)
def checkString( template, patterns ):
    if not len( template ):
        if len( patterns ):
            return 0
        else:
            return 1
        
    elif not len( patterns ):
        if not '#' in template:
            return 1
        else:
            return 0

    if template[ 0 ] == '.':
        return checkString( template[ 1: ], patterns )
    
    elif template[ 0 ] == '?':
        return checkString( '.' + template[ 1: ], patterns ) + checkString( '#' + template[ 1: ], patterns )
    
    elif template[ 0 ] == '#' and len( template ) >= patterns[ 0 ] and '.' not in template[ 0:patterns[ 0 ] ]:
        if len( template ) > patterns[ 0 ]:
            if template[ patterns[ 0 ] ] == '#':
                return 0
            else:
                return checkString( template[ patterns[ 0 ]+1: ], patterns[ 1: ] )
            
        return checkString( template[ patterns[ 0 ]: ], patterns[ 1: ] )
    
    return 0


# Saving this post off reddit in case I ever need to try to remember how to tackle string validation in a recursive
# fashion.  It's much better to go at it like that rather than using combinations / permutation:

# well, you could analyze the string left to right.

# if it starts with a ., discard the . and recursively check again.

# if it starts with a ?, replace the ? with a . and recursively check again, AND
# replace it with a # and recursively check again.

# it it starts with a #, check if it is long enough for the first group, check
# if all characters in the first [grouplength] characters are not '.', and then
# remove the first [grouplength] chars and the first group number, recursively
# check again.

# at some point you will get to the point of having an empty string and more
# groups to do - that is a zero. or you have an empty string with zero gropus to
# do - that is a one.

# there are more rules to check than these few, which are up to you to find. but
# this is a way to work out the solution.


# This works for part 1 but can't even handle a simple pattern for part 2.  Leaving in for posterity.
def findOptions( pattern, length ):
    options = []

    groups = len( pattern )
    blanks = length - sum( pattern ) - groups + 1
    patternOnes = [ [1] * i for i in pattern ]
    places = groups + blanks

    # Get the indexes of the groups in the row
    for p in it.combinations( range( groups + blanks ), groups ):
        # At this point:
        #  patternOnes = a list of the correct number of hash marks for the pattern
        #  p = the indexes where the 1's are supposed to go in the final list
        opt = [[0]] * places

        # Now sub in each patternOnes at the correct index
        for i, po in zip( p, patternOnes ):
            opt[ i ] = po + [0]

        opt = list( it.chain.from_iterable( opt ) )[ :-1 ]

        options.append( opt )

    return options

def validString( str, template ):
    for s, t in zip( str, template ):
        if t == '?':
            continue
        elif t == '.' and s != 0:
            return False
        elif t == '#' and s != 1:
            return False
        
    return True


if __name__ == "__main__":
    main( argv=sys.argv )