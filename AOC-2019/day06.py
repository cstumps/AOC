# --- Day 6: Universal Orbit Map ---
#
# You've landed at the Universal Orbit Map facility on Mercury. Because
# navigation in space often involves transferring between orbits, the orbit maps
# here are useful for finding efficient routes between, for example, you and
# Santa. You download a map of the local orbits (your puzzle input).
#
# Except for the universal Center of Mass (COM), every object in space is in
# orbit around exactly one other object. An orbit looks roughly like this:
#
#                   \
#                    \
#                     |
#                     |
# AAA--> o            o <--BBB
#                     |
#                     |
#                    /
#                   /
#
# In this diagram, the object BBB is in orbit around AAA. The path that BBB
# takes around AAA (drawn with lines) is only partly shown. In the map data,
# this orbital relationship is written AAA)BBB, which means "BBB is in orbit
# around AAA".
#
# Before you use your map data to plot a course, you need to make sure it wasn't
# corrupted during the download. To verify maps, the Universal Orbit Map
# facility uses orbit count checksums - the total number of direct orbits (like
# the one shown above) and indirect orbits.
#
# Whenever A orbits B and B orbits C, then A indirectly orbits C. This chain can
# be any number of objects long: if A orbits B, B orbits C, and C orbits D, then
# A indirectly orbits D.
#
# For example, suppose you have the following map:
#
# COM)B B)C C)D D)E E)F B)G G)H D)I E)J J)K K)L
#
# Visually, the above map of orbits looks like this:
#
#         G - H       J - K - L
#        /           /
# COM - B - C - D - E - F
#                \
#                 I
#
# In this visual representation, when two objects are connected by a line, the
# one on the right directly orbits the one on the left.
#
# Here, we can count the total number of orbits as follows:
#
#     D directly orbits C and indirectly orbits B and COM, a total of 3 orbits.
#     L directly orbits K and indirectly orbits J, E, D, C, B, and COM, a total of 7 orbits.
#     COM orbits nothing.
#
# The total number of direct and indirect orbits in this example is 42.
#
# What is the total number of direct and indirect orbits in your map data?
#
# --- Part Two ---
#
# Now, you just need to figure out how many orbital transfers you (YOU) need to
# take to get to Santa (SAN).
#
# You start at the object YOU are orbiting; your destination is the object SAN
# is orbiting. An orbital transfer lets you move from any object to an object
# orbiting or orbited by that object.
#
# For example, suppose you have the following map:
#
# COM)B B)C C)D D)E E)F B)G G)H D)I E)J J)K K)L K)YOU I)SAN
#
# Visually, the above map of orbits looks like this:
#
#                           YOU
#                          /
#         G - H       J - K - L
#        /           /
# COM - B - C - D - E - F
#                \
#                 I - SAN
#
# In this example, YOU are in orbit around K, and SAN is in orbit around I. To
# move from K to I, a minimum of 4 orbital transfers are required:
#
#     K to J
#     J to E
#     E to D
#     D to I
#
# Afterward, the map of orbits looks like this:
#
#         G - H       J - K - L
#        /           /
# COM - B - C - D - E - F
#                \
#                 I - SAN
#                  \
#                   YOU
#
# What is the minimum number of orbital transfers required to move from the
# object YOU are orbiting to the object SAN is orbiting? (Between the objects
# they are orbiting - not between YOU and SAN.)

# This one sucked.  This is by far not an optimal solution though it does come up
# with the right answers.

import sys

class Node( object ):
    def __init__( self, value, parent ):
        self.value = value
        self.parent = parent
        self.children = []

    def __str__( self ):
        return self.value

    def addChild( self, obj ):
        self.children.append( obj )

class Tree( object ):
    def __init__( self ):
        self.root = None

    def __contains__( self, value ):
        if self.findNode( self.root, value ) != None:
            return True
        else:
            return False

    def addValue( self, value, parent ):
        if self.root == None:
            self.root = Node( value, None )
        else:
            p = self.findNode( self.root, parent )
            p.addChild( Node( value, p ) )

    def findNode( self, node, value ):
        if node.value == value:
            return node
        else:
            for child in node.children:
                n = self.findNode( child, value )

                if n != None:
                    return n
            else:
                return None

    def findDirect( self, node=None ):
        if node == None:
            node = self.root

        return self.countChildren( node )

    def findIndirect( self, node=None ):
        count = 0

        if node == None:
            node = self.root

        for child in node.children:
            count += self.countChildren( child )
            count += self.findIndirect( child )

        return count

    def countChildren( self, node ):
        count = len( node.children )

        for child in node.children:
            count += self.countChildren( child )

        return count

    def findDist( self, v1, v2 ):
        n1 = self.findNode( self.root, v1 )
        n2 = self.findNode( self.root, v2 )

        # If v2 is a child of v1
        if self.findNode( n1, v2 ) != None:
            print( "calling 1" )
            return self.findDist2( n1, n2, 0 )

        # If v1 is a child of v2
        elif self.findNode( n2, v1 ) != None:
            print( "calling 2" )
            return self.findDist2( n2, n1, 0 )

        # Else find common parent
        else:
            cur = n1.parent

            while self.findNode( cur, v2 ) == None:
                cur = cur.parent

            return self.findDist2( cur, n1, 0 ) + self.findDist2( cur, n2, 0 )

    def findDist2( self, start, target, count ):
        if start.value == target.value:
            return count
        else:
            for child in start.children:
                c = self.findDist2( child, target, count + 1 )

                if c != 0:
                    return c

        return 0

def main( argv ):

    # Read in input file
    with open( "input/day06-input.txt", "r" ) as f:
        data = f.readlines()

    #data = [ 'COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L' ]
    #data = [ 'COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN' ]

    t = Tree()
    t.addValue( 'COM', None )

    # Data in file is out of order, will take many passes thru to get all items added
    while len( data ):
        for item in data:
            p = item.split( ')' )[ 0 ]
            c = item.split( ')' )[ 1 ].strip()

            if p in t:
                t.addValue( c, p )
                data.remove( item )

    d = t.findDirect()
    print( "Direct connections: %s" % d )

    i = t.findIndirect()
    print( "Indirect connections: %s" % i )

    print( "Part 1 total connections: %s" % (d + i) )

    m = t.findDist( 'SAN', 'YOU' ) - 2
    print( "Part 2 total moves: %s" % m )

    return 0

if __name__ == "__main__":
    main( argv=sys.argv )