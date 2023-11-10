# --- Day 16: Proboscidea Volcanium ---

# The sensors have led you to the origin of the distress signal: yet another
# handheld device, just like the one the Elves gave you. However, you don't see
# any Elves around; instead, the device is surrounded by elephants! They must
# have gotten lost in these tunnels, and one of the elephants apparently figured
# out how to turn on the distress signal.

# The ground rumbles again, much stronger this time. What kind of cave is this,
# exactly? You scan the cave with your handheld device; it reports mostly
# igneous rock, some ash, pockets of pressurized gas, magma... this isn't just a
# cave, it's a volcano!

# You need to get the elephants out of here, quickly. Your device estimates that
# you have 30 minutes before the volcano erupts, so you don't have time to go
# back out the way you came in.

# You scan the cave for other options and discover a network of pipes and
# pressure-release valves. You aren't sure how such a system got into a volcano,
# but you don't have time to complain; your device produces a report (your
# puzzle input) of each valve's flow rate if it were opened (in pressure per
# minute) and the tunnels you could use to move between the valves.

# There's even a valve in the room you and the elephants are currently standing
# in labeled AA. You estimate it will take you one minute to open a single valve
# and one minute to follow any tunnel from one valve to another. What is the
# most pressure you could release?

# For example, suppose you had the following scan output:

# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II

# All of the valves begin closed. You start at valve AA, but it must be damaged
# or jammed or something: its flow rate is 0, so there's no point in opening it.
# However, you could spend one minute moving to valve BB and another minute
# opening it; doing so would release pressure during the remaining 28 minutes at
# a flow rate of 13, a total eventual pressure release of 28 * 13 = 364. Then,
# you could spend your third minute moving to valve CC and your fourth minute
# opening it, providing an additional 26 minutes of eventual pressure release at
# a flow rate of 2, or 52 total pressure released by valve CC.

# Making your way through the tunnels like this, you could probably open many or
# all of the valves by the time 30 minutes have elapsed. However, you need to
# release as much pressure as possible, so you'll need to be methodical.
# Instead, consider this approach:

# == Minute 1 ==
# No valves are open.
# You move to valve DD.

# == Minute 2 ==
# No valves are open.
# You open valve DD.

# == Minute 3 ==
# Valve DD is open, releasing 20 pressure.
# You move to valve CC.

# == Minute 4 ==
# Valve DD is open, releasing 20 pressure.
# You move to valve BB.

# == Minute 5 ==
# Valve DD is open, releasing 20 pressure.
# You open valve BB.

# == Minute 6 ==
# Valves BB and DD are open, releasing 33 pressure.
# You move to valve AA.

# == Minute 7 ==
# Valves BB and DD are open, releasing 33 pressure.
# You move to valve II.

# == Minute 8 ==
# Valves BB and DD are open, releasing 33 pressure.
# You move to valve JJ.

# == Minute 9 ==
# Valves BB and DD are open, releasing 33 pressure.
# You open valve JJ.

# == Minute 10 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve II.

# == Minute 11 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve AA.

# == Minute 12 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve DD.

# == Minute 13 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve EE.

# == Minute 14 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve FF.

# == Minute 15 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve GG.

# == Minute 16 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve HH.

# == Minute 17 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You open valve HH.

# == Minute 18 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve GG.

# == Minute 19 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve FF.

# == Minute 20 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve EE.

# == Minute 21 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You open valve EE.

# == Minute 22 ==
# Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
# You move to valve DD.

# == Minute 23 ==
# Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
# You move to valve CC.

# == Minute 24 ==
# Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
# You open valve CC.

# == Minute 25 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 26 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 27 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 28 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 29 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 30 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# This approach lets you release the most pressure possible in 30 minutes with
# this valve layout, 1651.

# Work out the steps to release the most pressure in 30 minutes. What is the
# most pressure you can release?

# You're worried that even with an optimal approach, the pressure released won't
# be enough. What if you got one of the elephants to help you?

# It would take you 4 minutes to teach an elephant how to open the right valves
# in the right order, leaving you with only 26 minutes to actually execute your
# plan. Would having two of you working together be better, even if it means
# having less time? (Assume that you teach the elephant before opening any
# valves yourself, giving you both the same full 26 minutes.)

# In the example above, you could teach the elephant to help you as follows:

# == Minute 1 ==
# No valves are open.
# You move to valve II.
# The elephant moves to valve DD.

# == Minute 2 ==
# No valves are open.
# You move to valve JJ.
# The elephant opens valve DD.

# == Minute 3 ==
# Valve DD is open, releasing 20 pressure.
# You open valve JJ.
# The elephant moves to valve EE.

# == Minute 4 ==
# Valves DD and JJ are open, releasing 41 pressure.
# You move to valve II.
# The elephant moves to valve FF.

# == Minute 5 ==
# Valves DD and JJ are open, releasing 41 pressure.
# You move to valve AA.
# The elephant moves to valve GG.

# == Minute 6 ==
# Valves DD and JJ are open, releasing 41 pressure.
# You move to valve BB.
# The elephant moves to valve HH.

# == Minute 7 ==
# Valves DD and JJ are open, releasing 41 pressure.
# You open valve BB.
# The elephant opens valve HH.

# == Minute 8 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve CC.
# The elephant moves to valve GG.

# == Minute 9 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You open valve CC.
# The elephant moves to valve FF.

# == Minute 10 ==
# Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
# The elephant moves to valve EE.

# == Minute 11 ==
# Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
# The elephant opens valve EE.

# (At this point, all valves are open.)

# == Minute 12 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# ...

# == Minute 20 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# ...

# == Minute 26 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# With the elephant helping, after 26 minutes, the best you could do would
# release a total of 1707 pressure.

# With you and an elephant working together for 26 minutes, what is the most
# pressure you could release?

# So for part 1 we got a legit correct answer.  The annealing algorithm works fairly well
# though it is possible to occassionally get a wrong answer though I've widened the 
# parameters for it such that it shouldn't for these data sets.  Part 2 however relies
# on an observation that for our data set, if the elephant handles the valves remaining
# after our time runs out then we get the max value.  This will not work for all data sets.
# Notably the sample set fails here because we get through all the valves and there are none
# left for the elephant.  This is kinda cheesy but we're out of time for today and we got a 
# right answer.

# This annealing algorithm is worth remembering.

# This is probably what we would want to evolve to.  If I were to reduce the distance matrix to
# only those nodes with rates > 0 and put the movement into the edge weights then we could probably
# do a true depth or bredth first search of the space.  This is from teh solitions thread:

# My code went through a lot of iterations here. Initially started part 1 with a
# heap-based BFS search which initially worked out pretty well and executed in
# ~1s or so, and I tried to prune states, e.g. if we're partially through a
# state and even the most optimistic way of finishing won't get to our current
# max, just drop it entirely.

# Then the state space exploded for part 2 and I switched to doing a DFS-based
# solution. Also found out that using fancy immutable classes to represent state
# makes it way slower so it ended up being kind of dirty and using non-local
# variables.

# I then realized that we could probably just compress the graph to valves with
# positive flow rates (using Floyd-Warshall to get edge weights) like people
# have described here, so after initial submission I went and did a BFS approach
# based on that, and also used the observation that you/elephant operate on
# disjoint sets of valves, so you just need to perform BFS to find all of the
# best states for a 1-player scenario, then just match against all pairs of
# states with disjoint open valves.

# This got my part 2 down to a runtime of ~0.4s in Python which I'm pretty happy
# with.

import sys
import numpy as np
import random
import math
import copy
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

def main( argv ):

    with open( "input/day16-input.txt" ) as f:
        data = f.readlines()

    #data = [ 'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB',
    #         'Valve BB has flow rate=13; tunnels lead to valves CC, AA',
    #         'Valve CC has flow rate=2; tunnels lead to valves DD, BB',
    #         'Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE',
    #         'Valve EE has flow rate=3; tunnels lead to valves FF, DD',
    #         'Valve FF has flow rate=0; tunnels lead to valves EE, GG',
    #         'Valve GG has flow rate=0; tunnels lead to valves FF, HH',
    #         'Valve HH has flow rate=22; tunnel leads to valve GG',
    #         'Valve II has flow rate=0; tunnels lead to valves AA, JJ',
    #         'Valve JJ has flow rate=21; tunnel leads to valve II' ]

    # Convert the text into nodes with numbers, a rate value, and a list of destinations
    letterMap = []
    graph = []
    maxRoom = 0

    # Create a mapping of nodes to numbers
    for line in data:
        line = line.split()
        letterMap.append( line[ 1 ] )

    # Populate our graph
    for line in data:
        line = line.split()

        source = letterMap.index( line[ 1 ] )
        rate = int( line[ 4 ].split( '=' )[ 1 ].strip( ';' ) )
        dest = [ letterMap.index( l[ 0:2 ] ) for l in line[ 9: ] ]

        graph.append( [ source, rate, dest ] )

        if source > maxRoom:
            maxRoom = source

    ##
    # Part 1
    ##

    # Create an adjacency matrix

    adj = np.zeros( shape=(maxRoom + 1,maxRoom + 1) )

    for node in graph:
        for dest in node[ 2 ]:
            adj[ node[ 0 ] ][ dest ] = 1

    g = csr_matrix( adj )

    dist_matrix, predecessors = floyd_warshall( csgraph=g, directed=False, return_predecessors=True )

    # We only care about rooms that have a rate > 0.  Ditch the dest rooms too and AA node.
    validNodes = [ [ node[ 0 ], node[ 1 ] ] for node in graph if node[ 1 ] > 0 ]
    value, _ = runAnneal( validNodes, letterMap.index( 'AA' ), dist_matrix, 30 )

    print( f"Part 1 answer: {value}" )

    ## 
    # Part 2
    #

    val1, remainder = runAnneal( validNodes, letterMap.index( 'AA' ), dist_matrix, 26 )

    if not len( remainder ):
        print( "Unable to solve part 2 with this data set" )

    else:
        val2, _ = runAnneal( remainder, letterMap.index( 'AA' ), dist_matrix, 26 )

        print( f"Part 2 answer: {val1 + val2}" )

def runAnneal( nodes, startNode, dist, time ):
    initialTemp = 500
    finalTemp = 0.0002
    alpha = 0.0002

    curTemp = initialTemp

    curState = copy.deepcopy( nodes )
    solution = curState

    while curTemp > finalTemp:
        i = random.randint( 0, len( curState ) - 1 )
        j = random.randint( 0, len( curState ) - 1 )

        while j == i:
            i = random.randint( 0, len( curState ) - 1 )

        newState = swapPositions( copy.deepcopy( curState ), i, j )
        newPressure, _ = calcPressure( newState, dist, startNode, time )
        oldPressure, _ = calcPressure( curState, dist, startNode, time )

        diff = newPressure - oldPressure

        if diff > 0:
            solution = newState
            curState = newState

        elif random.uniform( 0, 1 ) < math.exp( diff / curTemp ):
            solution = newState 
            curState = newState  

        curTemp -= alpha 

    value, remainder = calcPressure( solution, dist, startNode, time )

    return value, remainder

def swapPositions( l, pos1, pos2 ):
    l[ pos1 ], l[ pos2 ] =  l[ pos2 ], l[ pos1 ]
    return l

def calcPressure( nodes, dist, start, time ):
    value = 0
    timeLeft = time
    curNode = start
    remainder = []

    for i in range( len( nodes ) ):
        timeLeft -= (dist[ curNode ][ nodes[ i ][ 0 ] ] + 1) # Time to get there
        # The +1 is the time it takes to open a valve

        if timeLeft <= 0:
            if i < len( nodes ):
                remainder = nodes[ i+1: ]

            break

        value += (timeLeft * nodes[ i ][ 1 ]) # Value of this valve in our total
        curNode = nodes[ i ][ 0 ]

    return value, remainder


# https://medium.com/swlh/how-to-implement-simulated-annealing-algorithm-in-python-ab196c2f56a0

# This is actually not the worst idea, but you need some additional stuff to
# make it work efficiently:

# Write a function that returns the total amount of pressure released for a
# given order of valve openings.

#     Start with a random ordered list of opening valves, calculate how much
#     pressure is released for that order. Make a variable Temperature=100

#     Randomly choose two indices i and j of your list and swap them. Calculate
#     how much pressure is released for this changed order.

#     If the pressure released is bigger, then obviously keep that swap and go
#     to 5

#     If the pressure released is higher, still do the swap if exp((new_pressure
#     - old_pressure)/Temperature) is bigger than a random number between 0 and
#     1 you generate on the fly. If that's not true nothing happens

#     reduce temperature by a small amount (say 0.002) and restart at 2

# break the loop if the Temperature reached a very small value (Temperature <
# 0.002).

# If the temperature reduction is small enough this is guaranteed to give you
# the correct path in the end (but obviously the small the change in temperature
# in each cycle the longer will this method take).

# This is called simulated annealing. Works like a charm on a problem like this
# (and one of its main advantages over many other optimization algorithms lies
# in how general it is - as long as you can define a "small change" in your
# system (like a single swap of two items in the list here) it's possible to use
# this heuristic.

# Why it works is a bit more complicated and has to do with statistical physics
# so I won't go into that here but in general it's a useful algorithm to know if
# you ever need to do non-convex optimization.

if __name__ == "__main__":
    main( argv=sys.argv )