# --- Day 12: Passage Pathing ---

# With your submarine's subterranean subsystems subsisting suboptimally, the
# only way you're getting out of this cave anytime soon is by finding a path
# yourself. Not just a path - the only way to know if you've found the best path
# is to find all of them.

# Fortunately, the sensors are still mostly working, and so you build a rough
# map of the remaining caves (your puzzle input). For example:

# start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end

# This is a list of how all of the caves are connected. You start in the cave
# named start, and your destination is the cave named end. An entry like b-d
# means that cave b is connected to cave d - that is, you can move between them.

# So, the above cave system looks roughly like this:

#     start
#     /   \
# c--A-----b--d
#     \   /
#      end

# Your goal is to find the number of distinct paths that start at start, end at
# end, and don't visit small caves more than once. There are two types of caves:
# big caves (written in uppercase, like A) and small caves (written in
# lowercase, like b). It would be a waste of time to visit any small cave more
# than once, but big caves are large enough that it might be worth visiting them
# multiple times. So, all paths you find should visit small caves at most once,
# and can visit big caves any number of times.

# Given these rules, there are 10 paths through this example cave system:

# start,A,b,A,c,A,end
# start,A,b,A,end
# start,A,b,end
# start,A,c,A,b,A,end
# start,A,c,A,b,end
# start,A,c,A,end
# start,A,end
# start,b,A,c,A,end
# start,b,A,end
# start,b,end

# (Each line in the above list corresponds to a single path; the caves visited
# by that path are listed in the order they are visited and separated by
# commas.)

# Note that in this cave system, cave d is never visited by any path: to do so,
# cave b would need to be visited twice (once on the way to cave d and a second
# time when returning from cave d), and since cave b is small, this is not
# allowed.

# Here is a slightly larger example:

# dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc

# The 19 paths through it are as follows:

# start,HN,dc,HN,end
# start,HN,dc,HN,kj,HN,end
# start,HN,dc,end
# start,HN,dc,kj,HN,end
# start,HN,end
# start,HN,kj,HN,dc,HN,end
# start,HN,kj,HN,dc,end
# start,HN,kj,HN,end
# start,HN,kj,dc,HN,end
# start,HN,kj,dc,end
# start,dc,HN,end
# start,dc,HN,kj,HN,end
# start,dc,end
# start,dc,kj,HN,end
# start,kj,HN,dc,HN,end
# start,kj,HN,dc,end
# start,kj,HN,end
# start,kj,dc,HN,end
# start,kj,dc,end

# Finally, this even larger example has 226 paths through it:

# fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW

# How many paths through this cave system are there that visit small caves at
# most once?

# --- Part Two ---

# After reviewing the available paths, you realize you might have time to visit
# a single small cave twice. Specifically, big caves can be visited any number
# of times, a single small cave can be visited at most twice, and the remaining
# small caves can be visited at most once. However, the caves named start and
# end can only be visited exactly once each: once you leave the start cave, you
# may not return to it, and once you reach the end cave, the path must end
# immediately.

# Now, the 36 possible paths through the first example above are:

# start,A,b,A,b,A,c,A,end
# start,A,b,A,b,A,end
# start,A,b,A,b,end
# start,A,b,A,c,A,b,A,end
# start,A,b,A,c,A,b,end
# start,A,b,A,c,A,c,A,end
# start,A,b,A,c,A,end
# start,A,b,A,end
# start,A,b,d,b,A,c,A,end
# start,A,b,d,b,A,end
# start,A,b,d,b,end
# start,A,b,end
# start,A,c,A,b,A,b,A,end
# start,A,c,A,b,A,b,end
# start,A,c,A,b,A,c,A,end
# start,A,c,A,b,A,end
# start,A,c,A,b,d,b,A,end
# start,A,c,A,b,d,b,end
# start,A,c,A,b,end
# start,A,c,A,c,A,b,A,end
# start,A,c,A,c,A,b,end
# start,A,c,A,c,A,end
# start,A,c,A,end
# start,A,end
# start,b,A,b,A,c,A,end
# start,b,A,b,A,end
# start,b,A,b,end
# start,b,A,c,A,b,A,end
# start,b,A,c,A,b,end
# start,b,A,c,A,c,A,end
# start,b,A,c,A,end
# start,b,A,end
# start,b,d,b,A,c,A,end
# start,b,d,b,A,end
# start,b,d,b,end
# start,b,end

# The slightly larger example above now has 103 paths through it, and the even
# larger example now has 3509 paths through it.

# Given these new rules, how many paths through this cave system are there?

import sys
from collections import deque

def main( argv ):

    # Read in input file
    with open( "input/day12-input.txt", "r" ) as f:
        data = [ i.strip() for i in f.readlines() ]

    #data = [ 'start-A', 'start-b', 'A-c', 'A-b', 'b-d', 'A-end', 'b-end' ]

    g = Graph()

    for line in data:
        v1 = line.split( '-' )[ 0 ]
        v2 = line.split( '-' )[ 1 ]

        g.addVertex( v1 )
        g.addVertex( v2 )
        g.addEdge( v1, v2 )

    # This is a terrible solution.  I repurposed existing search algorithms (recursive and iterative version)
    # because I didn't have a terrible amount of time to work on it.  It's hacked together and while it works,
    # its sloppy.

    ##
    # Part 1
    ##

    print( "Part 1 answer: %s" % g.findPaths( 'start', 'end' ) )
    
    ##
    # Part 2
    ##

    print( "Part 2 answer: %s" % g.findPathsIter( 'start', 'end' ) )

class Graph( object ):
    def __init__( self ):
        self.vertexCount = 0
        self.graph = {}

    def __str__( self ):
        stub = "\n"

        for vertex in self.graph:
            for edge in self.graph[ vertex ]:
                stub += "%s -> %s\n" % (vertex, edge[ 0 ])

        return stub

    def addVertex( self, v ):
        if v in self.graph:
            return
        else:
            self.vertexCount += 1
            self.graph[ v ] = []

    def addEdge( self, v1, v2 ):
        self.graph[ v1 ].append( v2 )
        self.graph[ v2 ].append( v1 )

    def canVisit( self, v, path ):
        if v in path and v.islower():
            smallCaves = [ p for p in path if p.islower() ]
            if len( smallCaves ) == len( set( smallCaves ) ) and v not in [ 'start', 'end' ]:
                return 1

            return 0

        return 1

    def findPathsIter( self, start, goal ):
        q = deque()

        path = []
        path.append( start )
        q.append( path.copy() )

        numPaths = 0

        while q:
            path = q.popleft()
            last = path[ -1 ]

            if ( last == goal ):
                numPaths += 1

            for v in self.graph[ last ]:
                if self.canVisit( v, path ):
                    newPath = path.copy()
                    newPath.append( v )
                    q.append( newPath )

        return numPaths

    def walkGraph( self, start, goal, visited, path, pathSet ):
        visited[ start ] += 1
        path.append( start )

        if start == goal:
            pathSet.append( path.copy() )

        for i in self.graph[ start ]:
            if ( visited[ i ] == 0 or i.isupper() ):
                self.walkGraph( i, goal, visited, path, pathSet )
                
        path.pop()
        visited[ start ] = 0

    def findPaths( self, start, goal ):
        visited = dict.fromkeys( self.graph.keys(), 0 )
        path = []
        pathSet = []

        self.walkGraph( start, goal, visited, path, pathSet )

        return len( pathSet )


if __name__ == "__main__":
    main( argv=sys.argv )