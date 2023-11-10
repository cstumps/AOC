# --- Day 20: Grove Positioning System ---

# It's finally time to meet back up with the Elves. When you try to contact
# them, however, you get no reply. Perhaps you're out of range?

# You know they're headed to the grove where the star fruit grows, so if you can
# figure out where that is, you should be able to meet back up with them.

# Fortunately, your handheld device has a file (your puzzle input) that contains
# the grove's coordinates! Unfortunately, the file is encrypted - just in case
# the device were to fall into the wrong hands.

# Maybe you can decrypt it?

# When you were still back at the camp, you overheard some Elves talking about
# coordinate file encryption. The main operation involved in decrypting the file
# is called mixing.

# The encrypted file is a list of numbers. To mix the file, move each number
# forward or backward in the file a number of positions equal to the value of
# the number being moved. The list is circular, so moving a number off one end
# of the list wraps back around to the other end as if the ends were connected.

# For example, to move the 1 in a sequence like 4, 5, 6, 1, 7, 8, 9, the 1 moves
# one position forward: 4, 5, 6, 7, 1, 8, 9. To move the -2 in a sequence like
# 4, -2, 5, 6, 7, 8, 9, the -2 moves two positions backward, wrapping around: 4,
# 5, 6, 7, 8, -2, 9.

# The numbers should be moved in the order they originally appear in the
# encrypted file. Numbers moving around during the mixing process do not change
# the order in which the numbers are moved.

# Consider this encrypted file:

# 1
# 2
# -3
# 3
# -2
# 0
# 4

# Mixing this file proceeds as follows:

# Initial arrangement:
# 1, 2, -3, 3, -2, 0, 4

# 1 moves between 2 and -3:
# 2, 1, -3, 3, -2, 0, 4

# 2 moves between -3 and 3:
# 1, -3, 2, 3, -2, 0, 4

# -3 moves between -2 and 0:
# 1, 2, 3, -2, -3, 0, 4

# 3 moves between 0 and 4:
# 1, 2, -2, -3, 0, 3, 4

# -2 moves between 4 and 1:
# 1, 2, -3, 0, 3, 4, -2

# 0 does not move:
# 1, 2, -3, 0, 3, 4, -2

# 4 moves between -3 and 0:
# 1, 2, -3, 4, 0, 3, -2

# Then, the grove coordinates can be found by looking at the 1000th, 2000th, and
# 3000th numbers after the value 0, wrapping around the list as necessary. In
# the above example, the 1000th number after 0 is 4, the 2000th is -3, and the
# 3000th is 2; adding these together produces 3.

# Mix your encrypted file exactly once. What is the sum of the three numbers
# that form the grove coordinates?

# --- Part Two ---

# The grove coordinate values seem nonsensical. While you ponder the mysteries
# of Elf encryption, you suddenly remember the rest of the decryption routine
# you overheard back at camp.

# First, you need to apply the decryption key, 811589153. Multiply each number
# by the decryption key before you begin; this will produce the actual list of
# numbers to mix.

# Second, you need to mix the list of numbers ten times. The order in which the
# numbers are mixed does not change during mixing; the numbers are still moved
# in the order they appeared in the original, pre-mixed list. (So, if -3 appears
# fourth in the original list of numbers to mix, -3 will be the fourth number to
# move during each round of mixing.)

# Using the same example as above:

# Initial arrangement:
# 811589153, 1623178306, -2434767459, 2434767459, -1623178306, 0, 3246356612

# After 1 round of mixing:
# 0, -2434767459, 3246356612, -1623178306, 2434767459, 1623178306, 811589153

# After 2 rounds of mixing:
# 0, 2434767459, 1623178306, 3246356612, -2434767459, -1623178306, 811589153

# After 3 rounds of mixing:
# 0, 811589153, 2434767459, 3246356612, 1623178306, -1623178306, -2434767459

# After 4 rounds of mixing:
# 0, 1623178306, -2434767459, 811589153, 2434767459, 3246356612, -1623178306

# After 5 rounds of mixing:
# 0, 811589153, -1623178306, 1623178306, -2434767459, 3246356612, 2434767459

# After 6 rounds of mixing:
# 0, 811589153, -1623178306, 3246356612, -2434767459, 1623178306, 2434767459

# After 7 rounds of mixing:
# 0, -2434767459, 2434767459, 1623178306, -1623178306, 811589153, 3246356612

# After 8 rounds of mixing:
# 0, 1623178306, 3246356612, 811589153, -2434767459, 2434767459, -1623178306

# After 9 rounds of mixing:
# 0, 811589153, 1623178306, -2434767459, 3246356612, 2434767459, -1623178306

# After 10 rounds of mixing:
# 0, -2434767459, 1623178306, 3246356612, -1623178306, 2434767459, 811589153

# The grove coordinates can still be found in the same way. Here, the 1000th
# number after 0 is 811589153, the 2000th is 2434767459, and the 3000th is
# -1623178306; adding these together produces 1623178306.

# Apply the decryption key and mix your encrypted file ten times. What is the
# sum of the three numbers that form the grove coordinates?

# This is fugly but works.  Needed a little help on part one with removing the
# node before moving.  The directions are unclear on this point.  

import sys
import math

def main( argv ):

    with open( "input/day20-input.txt" ) as f:
        data = f.readlines()

    #data = [ '1', '2', '-3', '3', '-2', '0', '4' ]
    #data = [ '1', '5', '-2', '0' ]
    #data = [ '0', '4', '5', '1', '2', '3' ]

    ##
    # Part 1
    ##

    ll = LinkedList()

    for line in data:
        ll.append( Node( int( line ) ) )

    for node in ll.master:
        sign = int( math.copysign( 1, node.value ) )
        n = node

        if node.value != 0:
            ll.detach( node )

        # Figure out where to insert
        for i in range( 0, abs( node.value ) ):
            if sign > 0:
                n = n.next
            elif sign < 0:
                n = n.prev

        # Our insert add it after the given value so going backwards we have to go one more back
        if sign < 0:
            n = n.prev

        if node.value != 0:
            ll.insert( node, n )

    value = 0
    node = ll.zero

    for i in range( 0, 3000 ):
        node = node.next

        if i in [ 999, 1999, 2999 ]:
            value += node.value

    print( f"Part 1 answer: {value}" )

    ## 
    # Part 2
    ##

    ll = LinkedList()
    key = 811589153

    for line in data:
        ll.append( Node( int( line ) * key ) )

    for i in range( 10 ):
        for node in ll.master:
            n = node
            dist = node.value % (len( ll.master ) - 1) 

            if node.value != 0 and dist > 0:
                ll.detach( node )

            # Figure out where to insert
            for i in range( 0, dist ):
                    n = n.next

            if node.value != 0 and dist > 0:
                ll.insert( node, n )

    value = 0
    node = ll.zero

    for i in range( 0, 3000 ):
        node = node.next

        if i in [ 999, 1999, 2999 ]:
            value += node.value

    print( f"Part 2 answer: {value}" )

class Node:
    def __init__( self, value ):
        self.value = value

        self.prev = None
        self.next = None

class LinkedList:
    def __init__( self ):
        self.head = None
        self.zero = None
        self.master = []

    def printList( self ):
        cur = self.head

        while cur != self.head.prev:
            print( cur.value )
            cur = cur.next

        print( cur.value )
            
    def append( self, node ):
        if self.head == None: # First item in list
            node.next = node
            node.prev = node

            self.head = node

        else: # Add to end
            node.next = self.head
            node.prev = self.head.prev

            self.head.prev.next = node
            self.head.prev = node

        self.master.append( node )

        if node.value == 0:
            self.zero = node

    def detach( self, node ):
        if node == self.head:
            self.head = node.next

        node.prev.next = node.next
        node.next.prev = node.prev

    # Insert node AFTER middle
    def insert( self, node, middle ):
        if middle.next == self.head:
            self.head = node

        old = middle.next

        middle.next.prev = node
        middle.next = node

        node.prev = middle
        node.next = old

if __name__ == "__main__":
    main( argv=sys.argv )