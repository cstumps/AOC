# --- Day 21: Allergen Assessment ---

# You reach the train's last stop and the closest you can get to your vacation
# island without getting wet. There aren't even any boats here, but nothing can
# stop you now: you build a raft. You just need a few days' worth of food for
# your journey.

# You don't speak the local language, so you can't read any ingredients lists.
# However, sometimes, allergens are listed in a language you do understand. You
# should be able to use this information to determine which ingredient contains
# which allergen and work out which foods are safe to take with you on your
# trip.

# You start by compiling a list of foods (your puzzle input), one food per line.
# Each line includes that food's ingredients list followed by some or all of the
# allergens the food contains.

# Each allergen is found in exactly one ingredient. Each ingredient contains
# zero or one allergen. Allergens aren't always marked; when they're listed (as
# in (contains nuts, shellfish) after an ingredients list), the ingredient that
# contains each listed allergen will be somewhere in the corresponding
# ingredients list. However, even if an allergen isn't listed, the ingredient
# that contains that allergen could still be present: maybe they forgot to label
# it, or maybe it was labeled in a language you don't know.

# For example, consider the following list of foods:

# mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)

# The first food in the list has four ingredients (written in a language you
# don't understand): mxmxvkd, kfcds, sqjhc, and nhms. While the food might
# contain other allergens, a few allergens the food definitely contains are
# listed afterward: dairy and fish.

# The first step is to determine which ingredients can't possibly contain any of
# the allergens in any food in your list. In the above example, none of the
# ingredients kfcds, nhms, sbzzf, or trh can contain an allergen. Counting the
# number of times any of these ingredients appear in any ingredients list
# produces 5: they all appear once each except sbzzf, which appears twice.

# Determine which ingredients cannot possibly contain any of the allergens in
# your list. How many times do any of those ingredients appear?

# --- Part Two ---

# Now that you've isolated the inert ingredients, you should have enough
# information to figure out which ingredient contains which allergen.

# In the above example:

#     mxmxvkd contains dairy.
#     sqjhc contains fish.
#     fvjkl contains soy.

# Arrange the ingredients alphabetically by their allergen and separate them by
# commas to produce your canonical dangerous ingredient list. (There should not
# be any spaces in your canonical dangerous ingredient list.) In the above
# example, this would be mxmxvkd,sqjhc,fvjkl.

# Time to stock your raft with supplies. What is your canonical dangerous
# ingredient list?

import sys 
from itertools import combinations

def main( argv ):

    # Read in input file
    with open( "input/day21-input.txt", "r" ) as f:
        data = [ line.rstrip() for line in f ]

    # data = [ 'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
    #          'trh fvjkl sbzzf mxmxvkd (contains dairy)',
    #          'sqjhc fvjkl (contains soy)',
    #          'sqjhc mxmxvkd sbzzf (contains fish)' ]

    lhs = []
    rhs = []

    redLhs = []
    redRhs = []

    # Parse the input into left hand and right hand sides of each 'equation'
    for line in data:
        items = ''.join( i for i in line if not i in [ ',', ')', '(' ] ).split( 'contains' )

        lhs.append( items[ 0 ].strip().split() )
        rhs.append( items[ 1 ].strip().split() )

    # Create a complete list of all the allergens and ingredients
    allergens   = { a for l in rhs for a in l }
    ingredients = { i for l in lhs for i in l }

    badList = [] # List of ingredients with allergens
    
    # For each allergen, get a list of all the rules that contain it
    for alg in allergens:
        setList = [ ingList for ingList, allList in zip( lhs, rhs ) if alg in allList ]
        algList = [ allList for allList in rhs if alg in allList ] # Part 2

        # Find the common elements between all the lists
        comIng = set.intersection( *map( set, setList ) )
        comAlg = set.intersection( *map( set, algList ) ) # Part 2

        # For part 2 we save off the reduced lists
        redLhs.append( list( comIng ) )
        redRhs.append( list( comAlg ) )

        # These will be the ingredients that DO contain allergens
        badList.append( comIng )

    # After we've gone through everyting, get the list of 'good' ingredients
    badList  = set.union( *map( set, badList ) )
    goodList = ingredients - badList

    # Part 1 asks us to add up how often each of the items in the goodList appear in the
    # ingredient lists
    count = 0

    for good in goodList:
        for i in lhs:
            if good in i:
                count += 1

    print( "Part 1 answer: %s" % count )

    # For part 2, take the reduced lists and figure out the mappings
    # This isn't nice and pretty like part 1 was but it works.  I'd
    # be willing to be there is a smarter way to do this as part of
    # the part 1 solution above.
    solution = []
    delList = []

    while len( redLhs ):
        for ingList, algList in zip( redLhs, redRhs ):
            if len( ingList ) == 1:
                solution.append( ingList + algList )
                delList.append( ingList + algList )

        for i in delList:
            for j in redLhs:
                if i[ 0 ] in j and len( j ) > 1:
                    j.remove( i[ 0 ] )

        for i in delList:
            redLhs.remove( [ i[ 0 ] ] )
            redRhs.remove( [ i[ 1 ] ] )

        delList.clear()

    solution.sort( key=lambda x: x[ 1 ] )

    print( "Part 2 answer: %s" % ','.join( [ x[ 0 ] for x in solution ] ) )


if __name__ == "__main__":
    main( argv=sys.argv )