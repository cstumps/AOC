# --- Day 17: Clumsy Crucible ---

# The lava starts flowing rapidly once the Lava Production Facility is
# operational. As you leave, the reindeer offers you a parachute, allowing you
# to quickly reach Gear Island.

# As you descend, your bird's-eye view of Gear Island reveals why you had
# trouble finding anyone on your way up: half of Gear Island is empty, but the
# half below you is a giant factory city!

# You land near the gradually-filling pool of lava at the base of your new
# lavafall. Lavaducts will eventually carry the lava throughout the city, but to
# make use of it immediately, Elves are loading it into large crucibles on
# wheels.

# The crucibles are top-heavy and pushed by hand. Unfortunately, the crucibles
# become very difficult to steer at high speeds, and so it can be hard to go in
# a straight line for very long.

# To get Desert Island the machine parts it needs as soon as possible, you'll
# need to find the best way to get the crucible from the lava pool to the
# machine parts factory. To do this, you need to minimize heat loss while
# choosing a route that doesn't require the crucible to go in a straight line
# for too long.

# Fortunately, the Elves here have a map (your puzzle input) that uses traffic
# patterns, ambient temperature, and hundreds of other parameters to calculate
# exactly how much heat loss can be expected for a crucible entering any
# particular city block.

# For example:

# 2413432311323
# 3215453535623
# 3255245654254
# 3446585845452
# 4546657867536
# 1438598798454
# 4457876987766
# 3637877979653
# 4654967986887
# 4564679986453
# 1224686865563
# 2546548887735
# 4322674655533

# Each city block is marked by a single digit that represents the amount of heat
# loss if the crucible enters that block. The starting point, the lava pool, is
# the top-left city block; the destination, the machine parts factory, is the
# bottom-right city block. (Because you already start in the top-left block, you
# don't incur that block's heat loss unless you leave that block and then return
# to it.)

# Because it is difficult to keep the top-heavy crucible going in a straight
# line for very long, it can move at most three blocks in a single direction
# before it must turn 90 degrees left or right. The crucible also can't reverse
# direction; after entering each city block, it may only turn left, continue
# straight, or turn right.

# One way to minimize heat loss is this path:

# 2>>34^>>>1323
# 32v>>>35v5623
# 32552456v>>54
# 3446585845v52
# 4546657867v>6
# 14385987984v4
# 44578769877v6
# 36378779796v>
# 465496798688v
# 456467998645v
# 12246868655<v
# 25465488877v5
# 43226746555v>

# This path never moves more than three consecutive blocks in the same direction
# and incurs a heat loss of only 102.

# Directing the crucible from the lava pool to the machine parts factory, but
# not moving more than three consecutive blocks in the same direction, what is
# the least heat loss it can incur?

# --- Part Two ---

# The crucibles of lava simply aren't large enough to provide an adequate supply
# of lava to the machine parts factory. Instead, the Elves are going to upgrade
# to ultra crucibles.

# Ultra crucibles are even more difficult to steer than normal crucibles. Not
# only do they have trouble going in a straight line, but they also have trouble
# turning!

# Once an ultra crucible starts moving in a direction, it needs to move a
# minimum of four blocks in that direction before it can turn (or even before it
# can stop at the end). However, it will eventually start to get wobbly: an
# ultra crucible can move a maximum of ten consecutive blocks without turning.

# In the above example, an ultra crucible could follow this path to minimize
# heat loss:

# 2>>>>>>>>1323
# 32154535v5623
# 32552456v4254
# 34465858v5452
# 45466578v>>>>
# 143859879845v
# 445787698776v
# 363787797965v
# 465496798688v
# 456467998645v
# 122468686556v
# 254654888773v
# 432267465553v

# In the above example, an ultra crucible would incur the minimum possible heat
# loss of 94.

# Here's another example:

# 111111111111
# 999999999991
# 999999999991
# 999999999991
# 999999999991

# Sadly, an ultra crucible would need to take an unfortunate path like this one:

# 1>>>>>>>1111
# 9999999v9991
# 9999999v9991
# 9999999v9991
# 9999999v>>>>

# This route causes the ultra crucible to incur the minimum possible heat loss
# of 71.

# Directing the ultra crucible from the lava pool to the machine parts factory,
# what is the least heat loss it can incur?

import sys
import numpy as np
import queue

def main( argv ):

    # Read in input file and add up the sums
    with open( "input/day17-input.txt", "r" ) as f:
        data = [ line.rstrip( '\n' ) for line in f ]

    #data = [ '2413432311323',
    #         '3215453535623',
    #         '3255245654254',
    #         '3446585845452',
    #         '4546657867536',
    #         '1438598798454',
    #         '4457876987766',
    #         '3637877979653',
    #         '4654967986887', 
    #         '4564679986453',
    #         '1224686865563',
    #         '2546548887735',
    #         '4322674655533' ]
    
    #data = [ '112999',
    #         '911111' ]        # Should be 7 (part 1)

    #data = [ '111111111111',
    #         '999999999991',
    #         '999999999991',
    #         '999999999991',
    #         '999999999991' ]  # Should be 71 (part 2)
    
    grid = np.array( [ list( map( int, line ) ) for line in data ] )

    # Has a miserable time with this day, in large part because I had trouble understanding
    # how Dijkstra works so had to spend some time re-learning that.  In the end, relied pretty
    # heavily on hints in the subreddit, this website:

    # https://www.redblobgames.com/pathfinding/a-star/introduction.html

    # And for part 2, this guys code:

    # https://github.com/maafy6/advent-of-code/blob/main/aoc/aoc_2023/advent_2023_17.py

    # Also had limited time to work on this puzzle due to family committments.  Hopefully 
    # I'll remember this for next year's path finding puzzle.  It's pretty amazing to see
    # how short some people's solutions were.

    ##
    # Part 1
    ##

    g = Graph( grid )

    print( f"Part 1 answer: {g.astar( 1, 3 )}" )

    ##
    # Part 2
    ##

    print( f"Part 2 answer: {g.astar( 4, 10 )}" )


class Graph( object ):
    DIR_UP    = 0
    DIR_DOWN  = 1
    DIR_RIGHT = 2
    DIR_LEFT  = 3

    def __init__( self, graph ):
        self.height = len( graph )
        self.width = len( graph[ 0 ] )

        self.graph = graph
        self.dist = [ [float( 'Inf' )] * self.width for _ in range( self.height ) ]

    def heuristic( self, a, b ):
        # Manhattan distance on a square grid
        return abs( a[ 0 ] - b[ 0 ] ) + abs( a[ 1 ] - b[ 1 ] )

    def genNeighbors( self, pos, dir, minRun, maxRun ):
        neighbors = []

        for i in range( minRun, maxRun + 1 ):
            # Moving left/right - turn to up/down
            if dir == Graph.DIR_LEFT or dir == Graph.DIR_RIGHT: 
                if pos[ 1 ] - i >= 0:
                    neighbors.append( (pos[ 0 ], pos[ 1 ] - i, Graph.DIR_UP) )

                if pos[ 1 ] + i < self.height:
                    neighbors.append( (pos[ 0 ], pos[ 1 ] + i, Graph.DIR_DOWN) )
                
            # Moving up/down - turn to left/right
            else:
                if pos[ 0 ] - i >= 0:
                    neighbors.append( (pos[ 0 ] - i, pos[ 1 ], Graph.DIR_LEFT) )

                if pos[ 0 ] + i < self.width:
                    neighbors.append( (pos[ 0 ] + i, pos[ 1 ], Graph.DIR_RIGHT) )
                
        return neighbors

    def astar( self, minRun, maxRun ):
        start = (0, 0)
        goal = (self.width - 1, self.height - 1)
        frontier = queue.PriorityQueue()
        frontier.put( ( 0, (start, Graph.DIR_DOWN) ) )
        frontier.put( ( 0, (start, Graph.DIR_RIGHT) ) )

        costs = dict() 
        costs[ (start, Graph.DIR_DOWN) ] = 0
        costs[ (start, Graph.DIR_RIGHT) ] = 0

        while not frontier.empty():
            current, dir = frontier.get()[ 1 ]

            if current == goal:
                return costs[ (current, dir) ]

            for d in self.genNeighbors( current, dir, minRun, maxRun ):
                x, y, newDir = d

                if newDir == Graph.DIR_UP:
                    cost = sum( self.graph[ i ][ x ] for i in range( y, current[ 1 ] ) )
                elif newDir == Graph.DIR_DOWN:
                    cost = sum( self.graph[ i ][ x ] for i in range( current[ 1 ] + 1, y + 1 ) )
                elif newDir == Graph.DIR_LEFT:
                    cost = sum( self.graph[ y ][ i ] for i in range( x, current[ 0 ] ) )
                else:
                    cost = sum( self.graph[ y ][ i ] for i in range( current[ 0 ] + 1, x + 1 ) )

                newCost = costs[ (current, dir) ] + cost

                if ((x, y), newDir) not in costs or newCost < costs[ ((x, y), newDir) ]:
                    costs[ ((x, y), newDir) ] = newCost
                    priority = newCost + self.heuristic( goal, (x, y) )
                    frontier.put( ( priority, ( (x, y), newDir ) ) )

        return None


if __name__ == "__main__":
    main( argv=sys.argv )