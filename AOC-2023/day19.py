# --- Day 19: Aplenty ---

# The Elves of Gear Island are thankful for your help and send you on your way.
# They even have a hang glider that someone stole from Desert Island; since
# you're already going that direction, it would help them a lot if you would use
# it to get down there and return it to them.

# As you reach the bottom of the relentless avalanche of machine parts, you
# discover that they're already forming a formidable heap. Don't worry, though -
# a group of Elves is already here organizing the parts, and they have a system.

# To start, each part is rated in each of four categories:

#     x: Extremely cool looking
#     m: Musical (it makes a noise when you hit it)
#     a: Aerodynamic
#     s: Shiny

# Then, each part is sent through a series of workflows that will ultimately
# accept or reject the part. Each workflow has a name and contains a list of
# rules; each rule specifies a condition and where to send the part if the
# condition is true. The first rule that matches the part being considered is
# applied immediately, and the part moves on to the destination described by the
# rule. (The last rule in each workflow has no condition and always applies if
# reached.)

# Consider the workflow ex{x>10:one,m<20:two,a>30:R,A}. This workflow is named
# ex and contains four rules. If workflow ex were considering a specific part,
# it would perform the following steps in order:

#     Rule "x>10:one": If the part's x is more than 10, send the part to the
#     workflow named one.

#     Rule "m<20:two": Otherwise, if the part's m is less than 20, send the part
#     to the workflow named two.

#     Rule "a>30:R": Otherwise, if the part's a is more than 30, the part is
#     immediately rejected (R).

#     Rule "A": Otherwise, because no other rules matched the part, the part is
#     immediately accepted (A).

# If a part is sent to another workflow, it immediately switches to the start of
# that workflow instead and never returns. If a part is accepted (sent to A) or
# rejected (sent to R), the part immediately stops any further processing.

# The system works, but it's not keeping up with the torrent of weird metal
# shapes. The Elves ask if you can help sort a few parts and give you the list
# of workflows and some part ratings (your puzzle input). For example:

# px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
# rfg{s<537:gd,x>2440:R,A}
# qs{s>3448:A,lnx}
# qkq{x<1416:A,crn}
# crn{x>2662:A,R}
# in{s<1351:px,qqz}
# qqz{s>2770:qs,m<1801:hdj,R}
# gd{a>3333:R,R}
# hdj{m>838:A,pv}

# {x=787,m=2655,a=1222,s=2876}
# {x=1679,m=44,a=2067,s=496}
# {x=2036,m=264,a=79,s=2244}
# {x=2461,m=1339,a=466,s=291}
# {x=2127,m=1623,a=2188,s=1013}

# The workflows are listed first, followed by a blank line, then the ratings of
# the parts the Elves would like you to sort. All parts begin in the workflow
# named in. In this example, the five listed parts go through the following
# workflows:

#     {x=787,m=2655,a=1222,s=2876}: in -> qqz -> qs -> lnx -> A
#     {x=1679,m=44,a=2067,s=496}: in -> px -> rfg -> gd -> R
#     {x=2036,m=264,a=79,s=2244}: in -> qqz -> hdj -> pv -> A
#     {x=2461,m=1339,a=466,s=291}: in -> px -> qkq -> crn -> R
#     {x=2127,m=1623,a=2188,s=1013}: in -> px -> rfg -> A

# Ultimately, three parts are accepted. Adding up the x, m, a, and s rating for
# each of the accepted parts gives 7540 for the part with x=787, 4623 for the
# part with x=2036, and 6951 for the part with x=2127. Adding all of the ratings
# for all of the accepted parts gives the sum total of 19114.

# Sort through all of the parts you've been given; what do you get if you add
# together all of the rating numbers for all of the parts that ultimately get
# accepted?

# --- Part Two ---

# Even with your help, the sorting process still isn't fast enough.

# One of the Elves comes up with a new plan: rather than sort parts individually
# through all of these workflows, maybe you can figure out in advance which
# combinations of ratings will be accepted or rejected.

# Each of the four ratings (x, m, a, s) can have an integer value ranging from a
# minimum of 1 to a maximum of 4000. Of all possible distinct combinations of
# ratings, your job is to figure out which ones will be accepted.

# In the above example, there are 167409079868000 distinct combinations of
# ratings that will be accepted.

# Consider only your list of workflows; the list of part ratings that the Elves
# wanted you to sort is no longer relevant. How many distinct combinations of
# ratings will be accepted by the Elves' workflows?

import sys
import copy

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day19-input.txt", "r" ) as f:
        data = [ line.rstrip( '\n' ) for line in f ]

    #data = [ 'px{a<2006:qkq,m>2090:A,rfg}',
    #         'pv{a>1716:R,A}',
    #         'lnx{m>1548:A,A}',
    #         'rfg{s<537:gd,x>2440:R,A}',
    #         'qs{s>3448:A,lnx}',
    #         'qkq{x<1416:A,crn}',
    #         'crn{x>2662:A,R}',
    #         'in{s<1351:px,qqz}',
    #         'qqz{s>2770:qs,m<1801:hdj,R}',
    #         'gd{a>3333:R,R}',
    #         'hdj{m>838:A,pv}',
    #         '',
    #         '{x=787,m=2655,a=1222,s=2876}',
    #         '{x=1679,m=44,a=2067,s=496}',
    #         '{x=2036,m=264,a=79,s=2244}',
    #         '{x=2461,m=1339,a=466,s=291}',
    #         '{x=2127,m=1623,a=2188,s=1013}' ]

    # Read in rules
    rules = {}

    for i, line in enumerate( data ):
        if line == '':
            start = i
            break

        rule, exp = line.split( '{' )
        rules[ rule ] = exp[ :-1 ].split( ',' )

    # Read in parts
    parts = []

    for line in data[ start+1: ]:
        part = {}

        for v in line[ 1:-1 ].split( ',' ):
            v = v.split( '=' )
            part[ v[ 0 ] ] = int( v[ 1 ] )

        parts.append( part )

    ##
    # Part 1
    ##

    accepted = [ p for p in parts if evalPart( p, rules ) ]
    s = sum( [ sum( p.values() ) for p in accepted ] )

    print( f"Part 1 answer: {s}" )


    ##
    # Part 2
    ##

    # Flatten the tree (this makes it easier for me to follow and debug)
    flatRules = flattenRules( rules )    

    # Establish our upper and lower bounds
    low  = { 'x': 1,    'm': 1,    'a': 1,    's': 1    }
    high = { 'x': 4001, 'm': 4001, 'a': 4001, 's': 4001 } # Note 4000 is inclusive

    # Traverse the tree. Note that with the flattened rules entry node is 'in1'
    comb = processNode( 'in1', flatRules, low, high )

    print( f"Part 2 answer: {comb}" )


def processNode( node, rules, low, high ):
    # We hit a leaf
    if node == 'A':
        count = 1

        for l, h in zip( low.values(), high.values() ):
            count *= (h - l)

        return count
    
    elif node == 'R':
        return 0
    
    # Otherwise look up our node
    rule = rules[ node ]

    # Do bound updating here
    left, right = rule
    cost, sym = left.split( ':' )

    l, h, invL, invH = updateBounds( low, high, cost )

    # Process the left and right recursively
    return processNode( sym, rules, l, h ) + processNode( right, rules, invL, invH )
    

# Takes a low and high bounds and updates them based on the condition
# Returns both the positive and negative bound sets.  This is so much
# easier than trying to manipulate ranges.
def updateBounds( low, high, cond ):
    var, sym = cond[ :2 ]
    val = int( cond[ 2: ] )

    invLow = copy.deepcopy( low )
    invHigh = copy.deepcopy( high )

    if sym == '<': 
        high[ var ] = min( high[ var ], val )          # x < 1234
        invLow[ var ] = max( low[ var ], val )         # x >= 1234
    else:          
        low[ var ] = max( low[ var ], val + 1 )        # x > 1234
        invHigh[ var ] = min( low[ var ], val + 1 )    # x <= 1234

    return low, high, invLow, invHigh


# Probably not the most efficiently written code but it works and that's
# what's important.
def flattenRules( rules ):
    flatRules = {}

    for lhs, rhs in rules.items():
        count = 0

        for i, v in enumerate( rhs[ :-2 ] ):
            if v[ -1 ] not in [ 'A', 'R' ]:
                v = v + '1'

            flatRules[ lhs + str( i+1 ) ] = [ v, lhs + str( i+2 ) ]
            count += 1

        if rhs[ -2 ][ -1 ] not in [ 'A', 'R' ]:
            rhs[ -2 ] += '1'

        if rhs[ -1 ][ -1 ] not in [ 'A', 'R' ]:
            rhs[ -1 ] += '1'

        flatRules[ lhs + str( count + 1 ) ] = rhs[ -2: ]

    return flatRules


def evalPart( part, rules ):
    # Always start with the 'in' rule
    rule = rules[ 'in' ]
    
    while True:
        default = rule[ -1 ] # Fall thru

        for exp in rule[ :-1 ]: # For each check in the rule
            e, d = exp.split( ':' )

            # Eval seems to corrupt the local variable dict so we copy it
            if eval( e, copy.deepcopy( part ) ): 
                if d == 'A':
                    return True
                elif d == 'R':
                    return False
                else:
                    rule = rules[ d ]
                    break
        else:
            # Got all thru list, use default
            if default == 'A':
                return True
            elif default == 'R':
                return False
            else:
                rule = rules[ default ]

# This was a really neat puzzle.  My first introduction to K-d 
# trees.  I needed a nudge from the subreddit but all code is my own.  
# Flattening the rules list helped tremendously even though it's 
# probably not required.  The recursive function could have been written
# without it but it helped me wrap my head around it.  Below are select 
# comments from the subreddit that help explain the puzzle.

"""
 If you're struggling to understand Part 2, here's a modified version of the
 example to try (but that will give the same answer) that might help you to see
 the puzzle for what it is:

px1{a<2006:qkq1,px2}
px2{m>2090:A,rfg1}
pv1{a>1716:R,A}
lnx1{m>1548:A,A}
rfg1{s<537:gd1,rfg2}
rfg2{x>2440:R,A}
qs1{s>3448:A,lnx1}
qkq1{x<1416:A,crn1}
crn1{x>2662:A,R}
in{s<1351:px1,qqz1}
qqz1{s>2770:qs1,qqz2}
qqz2{m<1801:hdj1,R}
gd1{a>3333:R,R}
hdj1{m>838:A,pv1}

All I've done here is to number each of the original rules (except for in) with
a 1, and then split out each subsequent clause into a new workflow rule with an
incremented number. Fairly mechanical. So

px{a<2006:qkq,m>2090:A,rfg}

becomes:

px1{a<2006:qkq1,px2}
px2{m>2090:A,rfg1}

But with the workflows flattened like this, we can now see the rules for what
they represent: a binary k-d tree! Here are the workflow rules above reordered
and indented to show the tree structure:

in{s<1351:px1,qqz1}
  px1{a<2006:qkq1,px2}
    qkq1{x<1416:A,crn1}
      crn1{x>2662:A,R}
    px2{m>2090:A,rfg1}
      rfg1{s<537:gd1,rfg2}
        gd1{a>3333:R,R}
        rfg2{x>2440:R,A}
  qqz1{s>2770:qs1,qqz2}
    qs1{s>3448:A,lnx1}
      lnx1{m>1548:A,A}
    qqz2{m<1801:hdj1,R}
      hdj1{m>838:A,pv1}
        pv1{a>1716:R,A}

Beginning with the initial 4-d hypervolume, each node of the tree here beginning
with the root at in simply slices the current hypercube into two along an
axis-aligned hyperplane, with one child for each of the two halves. The A's and
R's denote edges that go to the leaves of the tree (imagine each A and R as a
distinct leaf.) And spatially, the tree is entirely disjoint; you don't have to
worry at all about any node overlapping any other.

So all we really need to do is walk through the tree, keeping track of the
extents of the hypercube for each node and totaling up the volume at each 'A'
leaf.

The workflows as written in the puzzle input just condense the nodes of the k-d
tree a bit to disguise this.

---

Sure. We start with a 4d cube from (1,1,1,1) to (4000,4000,4000,4000) in
(x,m,a,s) at the root node, in.

The rule at that node is s<1351, so we split that initial cube into one half
that covers the cube from (1,1,1,1) to (4000,4000,4000,1350) and is passed to
the first child, px1. The remaining half covers the cube from (1,1,1,1351) to
(4000,4000,4000,4000) and is passed to the other child, qqz1.

Continue recursively splitting cubes and passing one half to one child in the
tree and the other half to the other child. When you come to a leaf in the tree,
stop recursing, and if the leaf is marked A, find the volume of cube that was
passed in by multiplying the lengths of the sides and add it to the total. That
total is the number you're looking for.

(More ELI8: Imagine drawing a rectangle on a sheet of graph paper. Draw a line
through it to break it into two smaller rectangles, possibly unequal in size.
Now draw lines through each of those rectangles. Continue until you get bored.
Fill some, but not all of the rectangles in. How do you add up the area of the
filled rectangles?)

---

I never bothered to check if it formed a tree, assuming that the input we had
could jump in and out of each section (albeit never with infinite loops).

Instead I recurse at each predicate within a rule, keeping track of the bounds
implied by that rule. So in your example, the first recursion would put an upper
bound on s of 1350 and then continue recursing and refining those bounds until
we hit an A or R.

When that unrolls, we move to the next predicate using the opposite bounds (as
we know the first predicate didn't match) and recurse down that path, again
narrowing the bounds until we hit an A or R.

When we hit an R we return 0. When we hit an A then return the product of all
the bounds we've limited along the way, and sum all of those up to get the
answer.
"""

if __name__ == "__main__":
    main( argv=sys.argv )