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

def main( argv ):

    #with open( "input/day19-input.txt" ) as f:
    #    data = f.readlines()

    data = "Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian."

    ##
    # Part 1
    ##

    number = int( data.split()[ 1 ][ :-1 ] )
    ore = int( data.split()[ 6 ] )
    clay = int( data.split()[ 12 ] )
    obsidianOre = int( data.split()[ 18 ] )
    obsidianClay = int( data.split()[ 21 ] )
    geodeOre = int( data.split()[ 27 ] )
    geodeObsidian = int( data.split()[ 30 ] )

    bp = Blueprint( number )
    bp.setCost( Blueprint.ROBOT_ORE, ore, 0, 0 )
    bp.setCost( Blueprint.ROBOT_CLAY, clay, 0, 0 )
    bp.setCost( Blueprint.ROBOT_OBSIDIAN, obsidianOre, obsidianClay, 0 )
    bp.setCost( Blueprint.ROBOT_GEODE, geodeOre, 0, geodeObsidian )

    #print( bp.robots )

    f = Factory( bp )

    for i in range( 24 ):
        #print( f.resources )
        f.takeTurn()
        print()


    #print( f"Part 1 answer: {faceCount}" )

    ## 
    # Part 2
    ##


    #print( f"Part 2 answer: {faceCount}" )

class Blueprint:
    ROBOT_ORE      = 0 
    ROBOT_CLAY     = 1
    ROBOT_OBSIDIAN = 2
    ROBOT_GEODE    = 3

    ROBOT_STR = [ "ore-collecting", "clay-collecting", "obsidian-collecting", "geode-cracking" ]
    MIN_STR = [ "ore", "clay", "obsidian", "geode" ]

    MIN_ORE  = 0
    MIN_CLAY = 1
    MIN_OBS  = 2

    def __init__( self, number ):
        # [ ORE, CLAY, OBSIDIAN ]
        self.robots = [ [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0 ] ]
        self.number = number

    def setCost( self, robot, ore, clay, obsidian ):
        self.robots[ robot ][ Blueprint.MIN_ORE ] += ore
        self.robots[ robot ][ Blueprint.MIN_CLAY ] += clay
        self.robots[ robot ][ Blueprint.MIN_OBS ] += obsidian

    def getCost( self, robot ):
        return self.robots[ robot ]

class Factory:
    ROBOT_TYPES = [ Blueprint.ROBOT_ORE, Blueprint.ROBOT_CLAY, Blueprint.ROBOT_GEODE, Blueprint.ROBOT_OBSIDIAN, ]

    def __init__( self, blueprint ):
        self.blueprint = blueprint

        self.robots = [ 1, 0, 0, 0 ]
        self.buildQueue = [ 0, 0, 0, 0 ]
        self.resources = [ 0, 0, 0, 0 ]

        self.turn = 1

    def takeTurn( self ):
        print( f"== Minute {self.turn} ==" )

        # First see what we can build, prioritizing higher quality robots first
        for robot in sorted( Factory.ROBOT_TYPES, reverse=True ):
            cost = self.blueprint.getCost( robot )

            if self.resources[ Blueprint.MIN_ORE  ]  >= cost[ Blueprint.MIN_ORE  ] and \
               self.resources[ Blueprint.MIN_CLAY ] >= cost[ Blueprint.MIN_CLAY  ] and \
               self.resources[ Blueprint.MIN_OBS  ] >= cost[ Blueprint.MIN_OBS   ]:

                print( f"Spend {self.buildStr( cost )} to start building a {Blueprint.ROBOT_STR[ robot ]} robot" )

                # Deduct the cost from our resources
                self.resources[ Blueprint.MIN_ORE  ] -= cost[ Blueprint.MIN_ORE  ]
                self.resources[ Blueprint.MIN_CLAY ] -= cost[ Blueprint.MIN_CLAY ]
                self.resources[ Blueprint.MIN_OBS  ] -= cost[ Blueprint.MIN_OBS  ]
                
                # Add our new robot
                self.buildQueue[ robot ] += 1

        # Now collect new resources
        for robot in Factory.ROBOT_TYPES:
            if not self.robots[ robot ]:
                continue

            self.resources[ robot ] += self.robots[ robot ]

            str = f"{self.robots[ robot ]} {Blueprint.ROBOT_STR[ robot ]} robot(s) collect {self.robots[ robot ]} {Blueprint.MIN_STR[ robot ]}"
            str += f"; you now have {self.resources[ robot ]} {Blueprint.MIN_STR[ robot ]}"
            print( str )

        # Bring new robots in the queue online
        for robot in self.buildQueue:
            if not self.buildQueue[ robot ]:
                continue

            self.robots[ robot ] += self.buildQueue[ robot ]
            print( f"The new {Blueprint.ROBOT_STR[ robot ]} is ready; you now have {self.robots[ robot ]} of them" )

        # Update build queue for next turn
        #self.buildQueue = newRobots
        self.buildQueue = [ 0, 0, 0, 0 ]

        self.turn += 1
                

    def buildStr( self, cost ):
        str = ""

        if cost[ Blueprint.MIN_ORE ]:
            str += f"{cost[ Blueprint.MIN_ORE ]} ore"

        if cost[ Blueprint.MIN_CLAY ]:
            if len( str ):
                str += " and "

            str += f"{cost[ Blueprint.MIN_CLAY ]} clay"

        if cost[ Blueprint.MIN_OBS ]:
            if len( str ):
                str += " and "

            str += f"{cost[ Blueprint.MIN_OBS ]} obsidian"

        return str




if __name__ == "__main__":
    main( argv=sys.argv )