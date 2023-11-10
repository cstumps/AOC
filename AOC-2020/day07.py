# --- Day 7: Handy Haversacks ---

# You land at the regional airport in time for your next flight. In fact, it
# looks like you'll even have time to grab some food: all flights are currently
# delayed due to issues in luggage processing.

# Due to recent aviation regulations, many rules (your puzzle input) are being
# enforced about bags and their contents; bags must be color-coded and must
# contain specific quantities of other color-coded bags. Apparently, nobody
# responsible for these regulations considered how long they would take to
# enforce!

# For example, consider the following rules:

# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.

# These rules specify the required contents for 9 bag types. In this example,
# every faded blue bag is empty, every vibrant plum bag contains 11 bags (5
# faded blue and 6 dotted black), and so on.

# You have a shiny gold bag. If you wanted to carry it in at least one other
# bag, how many different bag colors would be valid for the outermost bag? (In
# other words: how many colors can, eventually, contain at least one shiny gold
# bag?)

# In the above rules, the following options would be available to you:

#     A bright white bag, which can hold your shiny gold bag directly.

#     A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.

#     A dark orange bag, which can hold bright white and muted yellow bags,
#     either of which could then hold your shiny gold bag. 

#     A light red bag, which can hold bright white and muted yellow bags, 
#     either of which could then hold your shiny gold bag.

# So, in this example, the number of bag colors that can eventually contain at
# least one shiny gold bag is 4.

# How many bag colors can eventually contain at least one shiny gold bag? (The
# list of rules is quite long; make sure you get all of it.)

# --- Part Two ---

# It's getting pretty expensive to fly these days - not because of ticket
# prices, but because of the ridiculous number of bags you need to buy!

# Consider again your shiny gold bag and the rules from the above example:

#     faded blue bags contain 0 other bags.
#     dotted black bags contain 0 other bags.
#     vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
#     dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

# So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags
# within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1
# + 1*7 + 2 + 2*11 = 32 bags!

# Of course, the actual rules have a small chance of going several levels deeper
# than this example; be sure to count all of the bags, even if the nesting
# becomes topologically impractical!

# Here's another example:

# shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.

# In this example, a single shiny gold bag must contain 126 other bags.

# How many individual bags are required inside your single shiny gold bag?

import sys 
import re

def main( argv ):

    # This is an absolutely terrible pair of solutions.  It's disjoined, inconsistent
    # in it's implementation, and probably inefficient... It does some up with the right 
    # answers though.  Between work and the kids I didn't really have time to come up 
    # with an elegant solution.

    # Read in input file
    with open( "input/day07-input.txt", "r" ) as f:
        data = f.readlines()

    # data = [ 'light red bags contain 1 bright white bag, 2 muted yellow bags.',
    #          'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    #          'bright white bags contain 1 shiny gold bag.',
    #          'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    #          'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    #          'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    #          'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    #          'faded blue bags contain no other bags.',
    #          'dotted black bags contain no other bags.' ]

    # data = [ 'shiny gold bags contain 2 dark red bags.',
    #          'dark red bags contain 2 dark orange bags.',
    #          'dark orange bags contain 2 dark yellow bags.',
    #          'dark yellow bags contain 2 dark green bags.',
    #          'dark green bags contain 2 dark blue bags.',
    #          'dark blue bags contain 2 dark violet bags.',
    #          'dark violet bags contain no other bags.' ]

    # Parse out the rules
    rules = []

    for line in data:
        line = re.split( " contain ", line.strip() )

        desc = line[ 0 ].split()[ 0 ]
        color = line[ 0 ].split()[ 1 ]

        b = Bag( desc, color )
        r = Rule( b )
        rules.append( r )

        for bag in line[ 1 ].split( ',' ):
            bag = bag.strip().split()

            # Empty bag
            if bag[ 0 ] == 'no':
                break

            # Bag with a sub-bag(s)
            else:  
                r.addBag( Bag( bag[ 1 ], bag[ 2 ] ), bag[ 0 ] )
        
    # Part 1

    # Find rules that carry our shiny gold bag
    counted = []
    nextLevel = [ Bag( "shiny", "gold" ) ]
    addList = []

    while len( nextLevel ):
        for bag in nextLevel:
            for r in rules:
                if r.containsBag( bag ):
                    if r.bag not in counted:
                        counted.append( r.bag )
                    
                    addList.append( r.bag ) # Save off the bags to look for next

        nextLevel.clear()
        nextLevel = addList.copy() # Next data set
        addList.clear()

    print( "Part 1 answer: %s" % len( counted ) )

    # Part 2

    # Find the rule for the shiny gold bag
    goldBag = Bag( "shiny", "gold" )

    for r in rules:
        if r.bag == goldBag:
            break

    # Now traverse down
    count = countBags( rules, r ) - 1 # Don't count the top level bag in the total

    print( "Part 2 answer: %s" % count )

def countBags( ruleTable, rule ):
    # Bottom of tree
    if not len( rule.contains ):
        return 1

    # Otherwise return the sum of what's in the contains
    else:
        sum = 1

        for bag in rule.contains:
            # Find the rule for this bag
            for r in ruleTable:
                if r.bag == bag[ 0 ]:
                    sum += (int( bag[ 1 ] ) * countBags( ruleTable, r ) )
                    break

        return sum

class Rule( object ):
    def __init__( self, bag ):
        self.bag = bag
        self.contains = []

    def __str__( self ):
        s = "<%s> =" % self.bag

        if len( self.contains ):
            for bag in self.contains:
                s += " <%s %s>" % (bag[ 1 ], bag[ 0 ])

        else:
            s += " Empty"

        return s

    def addBag( self, bag, count ):
        self.contains.append( [bag, count] )

    def containsBag( self, bag ):
        for b in self.contains:
            if bag == b[ 0 ]:
                return b[ 1 ]
        else:
            return 0

class Bag( object ):
    def __init__( self, desc, color ):
        self.desc  = desc   # Descriptor
        self.color = color  # Color
    
    def __str__( self ):
        return "%s %s" % (self.desc, self.color)

    def __eq__( self, other ):
        return (self.desc == other.desc) and (self.color == other.color)

if __name__ == "__main__":
    main( argv=sys.argv )

# The below code is a pretty printer for this puzzle that prints the tree from the raw 
# data.  This seems a very elegant solution (well, a solution could be derived from this
# rather easily I believe) however it contains a lot of python constructs that aren't
# completely clear to me.  It would be worth understanding this code better.

# import re

# def prefix(first, rest, lines):
#     it = iter(lines.splitlines())
#     yield first + next(it)
#     for line in it:
#         yield rest + line

# class Bag:
#     def __init__(self, name, bags):
#         self.name = name + " bag"
#         self.bags = bags

#     def __str__(self):
#         if not self.bags:
#             return self.name

#         *body, last = self.bags.items()
#         return '\n'.join(
#             (
#                 self.name,
#                 *(line for bag, n in body for line in prefix(' ├─', ' | ', f"{n} {bag}")),
#                 *prefix(" ╰─", "   ", f"{last[1]} {last[0]}"),
#             )
#         )

# with open("day_07_input.txt") as f:
#     raw = f.read()

# def parse_raw():
#     bag_description = r"([a-z]+ [a-z]+) bags contain (.+)"
#     formula = re.compile(r"(\d+) ([a-z]+ [a-z]+) bag")
#     bags = {bag: Bag(bag, contents) for bag, contents in re.findall(bag_description, raw)}
#     for bag in bags.values():
#         bag.bags = {bags[inner]: n for n, inner in formula.findall(bag.bags)}
#     return bags

# bags = parse_raw()

# def pp(bag):
#     print(bags[bag])