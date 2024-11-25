# --- Day 7: Recursive Circus ---

# Wandering further through the circuits of the computer, you come upon a tower
# of programs that have gotten themselves into a bit of trouble. A recursive
# algorithm has gotten out of hand, and now they're balanced precariously in a
# large tower.

# One program at the bottom supports the entire tower. It's holding a large
# disc, and on the disc are balanced several more sub-towers. At the bottom of
# these sub-towers, standing on the bottom disc, are other programs, each
# holding their own disc, and so on. At the very tops of these
# sub-sub-sub-...-towers, many programs stand simply keeping the disc below them
# balanced but with no disc of their own.

# You offer to help, but first you need to understand the structure of these
# towers. You ask each program to yell out their name, their weight, and (if
# they're holding a disc) the names of the programs immediately above them
# balancing on that disc. You write this information down (your puzzle input).
# Unfortunately, in their panic, they don't do this in an orderly fashion; by
# the time you're done, you're not sure which program gave which information.

# For example, if your list is the following:

# pbga (66)
# xhth (57)
# ebii (61)
# havc (66)
# ktlj (57)
# fwft (72) -> ktlj, cntj, xhth
# qoyq (66)
# padx (45) -> pbga, havc, qoyq
# tknk (41) -> ugml, padx, fwft
# jptl (61)
# ugml (68) -> gyxo, ebii, jptl
# gyxo (61)
# cntj (57)

# ...then you would be able to recreate the structure of the towers that looks
# like this:

#                 gyxo
#               /     
#          ugml - ebii
#        /      \     
#       |         jptl
#       |        
#       |         pbga
#      /        /
# tknk --- padx - havc
#      \        \
#       |         qoyq
#       |             
#       |         ktlj
#        \      /     
#          fwft - cntj
#               \     
#                 xhth

# In this example, tknk is at the bottom of the tower (the bottom program), and
# is holding up ugml, padx, and fwft. Those programs are, in turn, holding up
# other programs; in this example, none of those programs are holding up any
# other programs, and are all the tops of their own towers. (The actual tower
# balancing in front of you is much larger.)

# Before you're ready to help them, you need to make sure your information is
# correct. What is the name of the bottom program?

# --- Part Two ---

# The programs explain the situation: they can't get down. Rather, they could
# get down, if they weren't expending all of their energy trying to keep the
# tower balanced. Apparently, one program has the wrong weight, and until it's
# fixed, they're stuck here.

# For any program holding a disc, each program standing on that disc forms a
# sub-tower. Each of those sub-towers are supposed to be the same weight, or the
# disc itself isn't balanced. The weight of a tower is the sum of the weights of
# the programs in that tower.

# In the example above, this means that for ugml's disc to be balanced, gyxo,
# ebii, and jptl must all have the same weight, and they do: 61.

# However, for tknk to be balanced, each of the programs standing on its disc
# and all programs above it must each match. This means that the following sums
# must all be the same:

#     ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
#     padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
#     fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243

# As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the
# other two. Even though the nodes above ugml are balanced, ugml itself is too
# heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep the
# towers balanced. If this change were made, its weight would be 60.

# Given that exactly one program is the wrong weight, what would its weight need
# to be to balance the entire tower?

import sys

def main( argv ):

    # Read in input file and add up the sums
	with open( "input/day07-input.txt", "r" ) as f:
		data = [ line.rstrip( '\n' ) for line in f ]
             
	#data = [ 'pbga (66)',
	#		 'xhth (57)',
	#		 'ebii (61)',
	#		 'havc (66)',
	#		 'ktlj (57)',
	#		 'fwft (72) -> ktlj, cntj, xhth',
	#		 'qoyq (66)',
	#		 'padx (45) -> pbga, havc, qoyq',
	#		 'tknk (41) -> ugml, padx, fwft',
	#		 'jptl (61)',
	#		 'ugml (68) -> gyxo, ebii, jptl',
	#		 'gyxo (61)',
	#		 'cntj (57)' ]
	
	weights = { l.split()[ 0 ].strip(): int( l.split()[ 1 ][ 1:-1 ] ) for l in data }
	parents = { l.split()[ 0 ].strip(): l.split( ' -> ' )[ 1 ].split( ', ' ) for l in data if '->' in l }

    ##
    # Part 1
    ##

	# The root node will be the one that does not appear as a child to any others
	for p in parents.keys():
		for c in parents.values():
			if p in c:
				break
		else:
			root = p

	print( f"Part 1 answer: {root}" )

    ##
    # Part 2
    ##

	# Not my most impressive work but it does arrive at the correct answer.

	tree = createTree( root, parents, weights )

	print( f"Part 2 answer: {findUnbalanced( tree, 0 )}" )

def createTree( nodeName, parents, weights ):
	# Create the subtree
	node = Node( nodeName, weights[ nodeName ] )

	# Add the children recursively
	if nodeName in parents.keys(): # Has children
		for child in parents[ nodeName ]:
			node.addChild( createTree( child, parents, weights ) )

	# Return the subtree to the parent
	return node

def findUnbalanced( tree, offset ):
	bal, off = isBalanced( tree )

	if bal == None:
		return tree.weight + offset
	else:
		return findUnbalanced( bal, off )

# Check to see if tree is balanced and returns sub tree that is not balanced if false
# Returns None if balanced.
def isBalanced( tree ):
	weights = {}

	# Tally up the weights
	for subtree in tree.children:
		weight = findWeight( subtree )

		if weight in weights.keys():
			weights[ weight ].append( subtree )
		else:
			weights[ weight ] = [ subtree ]

	# See which weights only occurred once
	oneWeight = None
	offset = 0

	# This assumes that there is only 1 weight that is different in the subtrees
	for weight in weights.keys():
		if len( weights[ weight ] ) == 1:
			oneWeight = weights[ weight ][ 0 ]
			
			if weight == max( weights.keys() ):
				offset = min( weights.keys() ) - max( weights.keys() )
			else:
				offset = max( weights.keys() ) - min( weights.keys() )

	return oneWeight, offset

def findWeight( tree ):
	w = tree.weight

	for subtree in tree.children:
		w += findWeight( subtree )

	return w

class Node( object ):
	def __init__( self, name, weight ):
		self.name = name
		self.weight = weight
		self.children = []

	def __str__( self ):
		return self.name

	def addChild( self, obj ):
		self.children.append( obj )


if __name__ == "__main__":
	main( argv = sys.argv )