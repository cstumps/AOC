# --- Day 19: Not Enough Minerals ---

# Your scans show that the lava did indeed form obsidian!

# The wind has changed direction enough to stop sending lava droplets toward
# you, so you and the elephants exit the cave. As you do, you notice a
# collection of geodes around the pond. Perhaps you could use the obsidian to
# create some geode-cracking robots and break them open?

# To collect the obsidian from the bottom of the pond, you'll need waterproof
# obsidian-collecting robots. Fortunately, there is an abundant amount of clay
# nearby that you can use to make them waterproof.

# In order to harvest the clay, you'll need special-purpose clay-collecting
# robots. To make any type of robot, you'll need ore, which is also plentiful
# but in the opposite direction from the clay.

# Collecting ore requires ore-collecting robots with big drills. Fortunately,
# you have exactly one ore-collecting robot in your pack that you can use to
# kickstart the whole operation.

# Each robot can collect 1 of its resource type per minute. It also takes one
# minute for the robot factory (also conveniently from your pack) to construct
# any type of robot, although it consumes the necessary resources available when
# construction begins.

# The robot factory has many blueprints (your puzzle input) you can choose from,
# but once you've configured it with a blueprint, you can't change it. You'll
# need to work out which blueprint is best.

# For example:

# Blueprint 1:
#   Each ore robot costs 4 ore.
#   Each clay robot costs 2 ore.
#   Each obsidian robot costs 3 ore and 14 clay.
#   Each geode robot costs 2 ore and 7 obsidian.

# Blueprint 2:
#   Each ore robot costs 2 ore.
#   Each clay robot costs 3 ore.
#   Each obsidian robot costs 3 ore and 8 clay.
#   Each geode robot costs 3 ore and 12 obsidian.

# (Blueprints have been line-wrapped here for legibility. The robot factory's
# actual assortment of blueprints are provided one blueprint per line.)

# The elephants are starting to look hungry, so you shouldn't take too long; you
# need to figure out which blueprint would maximize the number of opened geodes
# after 24 minutes by figuring out which robots to build and when to build them.

# Using blueprint 1 in the example above, the largest number of geodes you could
# open in 24 minutes is 9. One way to achieve that is:

# == Minute 1 ==
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.

# == Minute 2 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.

# == Minute 3 ==
# Spend 2 ore to start building a clay-collecting robot.
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# The new clay-collecting robot is ready; you now have 1 of them.

# == Minute 4 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 1 clay-collecting robot collects 1 clay; you now have 1 clay.

# == Minute 5 ==
# Spend 2 ore to start building a clay-collecting robot.
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# 1 clay-collecting robot collects 1 clay; you now have 2 clay.
# The new clay-collecting robot is ready; you now have 2 of them.

# == Minute 6 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 2 clay-collecting robots collect 2 clay; you now have 4 clay.

# == Minute 7 ==
# Spend 2 ore to start building a clay-collecting robot.
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# 2 clay-collecting robots collect 2 clay; you now have 6 clay.
# The new clay-collecting robot is ready; you now have 3 of them.

# == Minute 8 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 3 clay-collecting robots collect 3 clay; you now have 9 clay.

# == Minute 9 ==
# 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# 3 clay-collecting robots collect 3 clay; you now have 12 clay.

# == Minute 10 ==
# 1 ore-collecting robot collects 1 ore; you now have 4 ore.
# 3 clay-collecting robots collect 3 clay; you now have 15 clay.

# == Minute 11 ==
# Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 3 clay-collecting robots collect 3 clay; you now have 4 clay.
# The new obsidian-collecting robot is ready; you now have 1 of them.

# == Minute 12 ==
# Spend 2 ore to start building a clay-collecting robot.
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# 3 clay-collecting robots collect 3 clay; you now have 7 clay.
# 1 obsidian-collecting robot collects 1 obsidian; you now have 1 obsidian.
# The new clay-collecting robot is ready; you now have 4 of them.

# == Minute 13 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 4 clay-collecting robots collect 4 clay; you now have 11 clay.
# 1 obsidian-collecting robot collects 1 obsidian; you now have 2 obsidian.

# == Minute 14 ==
# 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# 4 clay-collecting robots collect 4 clay; you now have 15 clay.
# 1 obsidian-collecting robot collects 1 obsidian; you now have 3 obsidian.

# == Minute 15 ==
# Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# 4 clay-collecting robots collect 4 clay; you now have 5 clay.
# 1 obsidian-collecting robot collects 1 obsidian; you now have 4 obsidian.
# The new obsidian-collecting robot is ready; you now have 2 of them.

# == Minute 16 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 4 clay-collecting robots collect 4 clay; you now have 9 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.

# == Minute 17 ==
# 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# 4 clay-collecting robots collect 4 clay; you now have 13 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.

# == Minute 18 ==
# Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 4 clay-collecting robots collect 4 clay; you now have 17 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 3 obsidian.
# The new geode-cracking robot is ready; you now have 1 of them.

# == Minute 19 ==
# 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# 4 clay-collecting robots collect 4 clay; you now have 21 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 5 obsidian.
# 1 geode-cracking robot cracks 1 geode; you now have 1 open geode.

# == Minute 20 ==
# 1 ore-collecting robot collects 1 ore; you now have 4 ore.
# 4 clay-collecting robots collect 4 clay; you now have 25 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 7 obsidian.
# 1 geode-cracking robot cracks 1 geode; you now have 2 open geodes.

# == Minute 21 ==
# Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# 4 clay-collecting robots collect 4 clay; you now have 29 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 2 obsidian.
# 1 geode-cracking robot cracks 1 geode; you now have 3 open geodes.
# The new geode-cracking robot is ready; you now have 2 of them.

# == Minute 22 ==
# 1 ore-collecting robot collects 1 ore; you now have 4 ore.
# 4 clay-collecting robots collect 4 clay; you now have 33 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 4 obsidian.
# 2 geode-cracking robots crack 2 geodes; you now have 5 open geodes.

# == Minute 23 ==
# 1 ore-collecting robot collects 1 ore; you now have 5 ore.
# 4 clay-collecting robots collect 4 clay; you now have 37 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.
# 2 geode-cracking robots crack 2 geodes; you now have 7 open geodes.

# == Minute 24 ==
# 1 ore-collecting robot collects 1 ore; you now have 6 ore.
# 4 clay-collecting robots collect 4 clay; you now have 41 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.
# 2 geode-cracking robots crack 2 geodes; you now have 9 open geodes.

# However, by using blueprint 2 in the example above, you could do even better:
# the largest number of geodes you could open in 24 minutes is 12.

# Determine the quality level of each blueprint by multiplying that blueprint's
# ID number with the largest number of geodes that can be opened in 24 minutes
# using that blueprint. In this example, the first blueprint has ID 1 and can
# open 9 geodes, so its quality level is 9. The second blueprint has ID 2 and
# can open 12 geodes, so its quality level is 24. Finally, if you add up the
# quality levels of all of the blueprints in the list, you get 33.

# Determine the quality level of each blueprint using the largest number of
# geodes it could produce in 24 minutes. What do you get if you add up the
# quality level of all of the blueprints in your list?

import sys
import copy
import math
import queue

ORE   = 0
CLAY  = 1
OBS   = 2
GEODE = 3

TODO_NOTHING  = -1
TODO_ORE      = 0
TODO_CLAY     = 1
TODO_OBSIDIAN = 2
TODO_GEODE    = 3

def main( argv ):

    with open( "input/day19-input.txt" ) as f:
        data = f.readlines()

    data = "Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian."
    #data = "Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."

    ##
    # Part 1
    ##

    quality = 0

    for line in data:
    #for i in range( 1 ):
        number        = int( line.split()[ 1 ][ :-1 ] )
        ore           = int( line.split()[ 6 ] )
        clay          = int( line.split()[ 12 ] )
        obsidianOre   = int( line.split()[ 18 ] )
        obsidianClay  = int( line.split()[ 21 ] )
        geodeOre      = int( line.split()[ 27 ] )
        geodeObsidian = int( line.split()[ 30 ] )

        oreBot   = [ ore, 0, 0, 0 ]
        clayBot  = [ clay, 0, 0, 0 ]
        obsBot   = [ obsidianOre, obsidianClay, 0, 0 ]
        geodeBot = [ geodeOre, 0, geodeObsidian, 0 ]

        bp = [ number, ore, clay, obsidianOre, obsidianClay, geodeOre, geodeObsidian ]

        bp2 = [ number, oreBot, clayBot, obsBot, geodeBot ]

        #             O  C  OB G
        inventory = [ 0, 0, 0, 0 ]
        robots    = [ 1, 0, 0, 0 ]
        turn      = 1

        istate = [ inventory, robots, turn ]

    #geodes = dfs( bp, istate, 24 )
        geodes = maxGeodes( bp2, istate, 2 )
        print( f"BP: {bp2[ 0 ]} - {geodes}" )

        quality += (geodes * bp2[ 0 ])
    
    print( quality )


    #print( f"Part 1 answer: {faceCount}" )

    ## 
    # Part 2
    ##


    #print( f"Part 2 answer: {faceCount}" )

# Compute how soon we will have resources to satisfy cost
def timeToBuild( costs, inventory, rate ):
    bestTime = 0

    for c, i, r in zip( costs, inventory, rate ):
        if i >= c:
            continue
        elif c > 0 and not r:
            return 99 # Not buildable
        else:
            bestTime = max( [ bestTime, math.ceil( c - i / r ) ] )

    return bestTime

def runTurns( inventory, robots, turns ):
    newInventory = []

    for i, r in zip( inventory, robots ):
        newInventory.append( i + (r * turns) )

    return newInventory

def maxGeodes( bp, istate, goal ):
    geodes = 0
    q = queue.Queue()

    q.put( copy.deepcopy( istate ) )

    maxOre  = max( [ bp[ 1 ][ 0 ], bp[ 2 ][ 0 ], bp[ 3 ][ 0 ], bp[ 4 ][ 0 ] ] )
    maxClay = max( [ bp[ 1 ][ 1 ], bp[ 2 ][ 1 ], bp[ 3 ][ 1 ], bp[ 4 ][ 1 ] ] )
    maxObs  = max( [ bp[ 1 ][ 2 ], bp[ 2 ][ 2 ], bp[ 3 ][ 2 ], bp[ 4 ][ 2 ] ] )

    maxBots = [ maxOre, maxClay, maxObs, 99 ]

    while not q.empty():
        inventory, robots, turn = q.get()

        #print()
        #print( f"Starting state: I:{inventory} R:{robots} T:{turn}" )

        #print( inventory )
        #print( robots )

        # We're done with this branch
        if turn >= goal:
            geodes = max( [ geodes, inventory[ GEODE ] ] )

        # Otherwise, figure out how long to build each robot type
        else:
            # For each robot type
            for i in range( 1, len( bp ) ):

                if robots[ i-1 ] >= maxBots[ i-1 ]:
                    continue

                # Get the cost of that robot
                cost = bp[ i ]

                # Determine how many turns until we can build one
                tb = timeToBuild( cost, inventory, robots )

                # If we have time to build this robot
                if tb <= (goal - turn): 
                    # Execute the number of harvest turns to get to the point where we can build it
                    i2 = runTurns( inventory, robots, tb )

                    # Decrease our inventory by the cost of the robot we're building
                    i3 = [ x - y for x, y in zip( i2, cost ) ]
                    
                    # Add our new robot
                    r2 = robots.copy()
                    r2[ i-1 ] += 1

                    #print( f"Adding state: {[i3, r2, turn+tb]}" )

                    # Queue up the next branch
                    #print( f"Pushing state: I:{i3} R:{r2} T:{turn+tb}" )
                    q.put( [ i3, r2, turn + tb ] )  
                
                # Not enought time to build this robot.  Just use up the remaining cycles and 
                # # update the inventory and send into the next state
                else:
                    # Dont' bother wih finishing out branch if we don't have geode robots
                    #if robots[ GEODE ] == 0:
                    #    continue

                    i2 = runTurns( inventory, robots, goal - turn )
                    r2 = robots.copy()

                    #print( f"Pushing state: I:{i2} R:{r2} T:{goal+1}" )
                    q.put( [ i2, r2, goal+1 ] )


    return geodes

def dfs( bp, state, goal ):
    geodes = 0
    q = queue.Queue()
    bestStates = [ 0 for i in range( goal + 1 ) ]

    maxOre = max( [ bp[ 1 ], bp[ 2 ], bp[ 3 ], bp[ 5 ] ] )
    maxClay = bp[ 4 ]
    maxObs = bp[ 6 ]

    q.put( copy.deepcopy( state ) )

    while not q.empty():
        inventory, robots, turn = q.get()

        # This branch had reached the goal state, save off the number of geodes
        if turn > goal:
            if inventory[ GEODE ] > geodes:
                geodes = inventory[ GEODE ]

        # Otherwise take a turn on this state
        else:

            if bestStates[ turn ] > (inventory[ GEODE ] * 2):
                continue # Prune this state

            todo = []

            # Always build a geode robot if we have the resources over all else
            if inventory[ ORE ] >= bp[ 5 ] and inventory[ OBS ] >= bp[ 6 ]:  # We have resources to build a geode robot
                todo.append( TODO_GEODE )
            
            else:
                todo.append( TODO_NOTHING )
                if inventory[ ORE ] >= bp[ 1 ] and robots[ ORE ] < maxOre:  # We have resources to build an ore robot
                    todo.append( TODO_ORE )

                if inventory[ ORE ] >= bp[ 2 ] and robots[ CLAY ] < maxClay:  # We have resources to build a clay robot
                    todo.append( TODO_CLAY )

                if inventory[ ORE ] >= bp[ 3 ] and inventory[ CLAY ] >= bp[ 4 ] and robots[ OBS ] < maxObs:  # We have resources to build an obsidian robot
                    todo.append( TODO_OBSIDIAN )

                

            for t in todo:
                r2 = robots.copy()
                i2 = [ x + y for x, y in zip( inventory, robots ) ]

                if t == TODO_ORE:
                    i2[ ORE ] -= bp[ 1 ]
                    r2[ ORE ] += 1

                elif t == TODO_CLAY:
                    i2[ ORE ] -= bp[ 2 ]
                    r2[ CLAY ] += 1

                elif t == TODO_OBSIDIAN:
                    i2[ ORE ]  -= bp[ 3 ]
                    i2[ CLAY ] -= bp[ 4 ]
                    r2[ OBS ] += 1

                elif t == TODO_GEODE:
                    i2[ ORE ] -= bp[ 5 ]
                    i2[ OBS ] -= bp[ 6 ]
                    r2[ GEODE ] += 1

                q.put( [ i2, r2, turn + 1 ] )

                if i2[ GEODE ] > bestStates[ turn ]:
                    bestStates[ turn ] = i2[ GEODE ]

    return geodes


if __name__ == "__main__":
    main( argv=sys.argv )