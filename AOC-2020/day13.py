# --- Day 13: Shuttle Search ---

# Your ferry can make it safely to a nearby port, but it won't get much further.
# When you call to book another ship, you discover that no ships embark from
# that port to your vacation island. You'll need to get from the port to the
# nearest airport.

# Fortunately, a shuttle bus service is available to bring you from the sea port
# to the airport! Each bus has an ID number that also indicates how often the
# bus leaves for the airport.

# Bus schedules are defined based on a timestamp that measures the number of
# minutes since some fixed reference point in the past. At timestamp 0, every
# bus simultaneously departed from the sea port. After that, each bus travels to
# the airport, then various other locations, and finally returns to the sea port
# to repeat its journey forever.

# The time this loop takes a particular bus is also its ID number: the bus with
# ID 5 departs from the sea port at timestamps 0, 5, 10, 15, and so on. The bus
# with ID 11 departs at 0, 11, 22, 33, and so on. If you are there when the bus
# departs, you can ride that bus to the airport!

# Your notes (your puzzle input) consist of two lines. The first line is your
# estimate of the earliest timestamp you could depart on a bus. The second line
# lists the bus IDs that are in service according to the shuttle company;
# entries that show x must be out of service, so you decide to ignore them.

# To save time once you arrive, your goal is to figure out the earliest bus you
# can take to the airport. (There will be exactly one such bus.)

# For example, suppose you have the following notes:

# 939
# 7,13,x,x,59,x,31,19

# Here, the earliest timestamp you could depart is 939, and the bus IDs in
# service are 7, 13, 59, 31, and 19. Near timestamp 939, these bus IDs depart at
# the times marked D:

# time   bus 7   bus 13  bus 59  bus 31  bus 19
# 929      .       .       .       .       .
# 930      .       .       .       D       .
# 931      D       .       .       .       D
# 932      .       .       .       .       .
# 933      .       .       .       .       .
# 934      .       .       .       .       .
# 935      .       .       .       .       .
# 936      .       D       .       .       .
# 937      .       .       .       .       .
# 938      D       .       .       .       .
# 939      .       .       .       .       .
# 940      .       .       .       .       .
# 941      .       .       .       .       .
# 942      .       .       .       .       .
# 943      .       .       .       .       .
# 944      .       .       D       .       .
# 945      D       .       .       .       .
# 946      .       .       .       .       .
# 947      .       .       .       .       .
# 948      .       .       .       .       .
# 949      .       D       .       .       .

# The earliest bus you could take is bus ID 59. It doesn't depart until
# timestamp 944, so you would need to wait 944 - 939 = 5 minutes before it
# departs. Multiplying the bus ID by the number of minutes you'd need to wait
# gives 295.

# What is the ID of the earliest bus you can take to the airport multiplied by
# the number of minutes you'll need to wait for that bus?

# --- Part Two ---

# The shuttle company is running a contest: one gold coin for anyone that can
# find the earliest timestamp such that the first bus ID departs at that time
# and each subsequent listed bus ID departs at that subsequent minute. (The
# first line in your input is no longer relevant.)

# For example, suppose you have the same list of bus IDs as above:

# 7,13,x,x,59,x,31,19

# An x in the schedule means there are no constraints on what bus IDs must
# depart at that time.

# This means you are looking for the earliest timestamp (called t) such that:

#     Bus ID 7 departs at timestamp t.

#     Bus ID 13 departs one minute after timestamp t.

#     There are no requirements or restrictions on departures at two or three
#     minutes after timestamp t.

#     Bus ID 59 departs four minutes after timestamp t.

#     There are no requirements or restrictions on departures at five minutes
#     after timestamp t.

#     Bus ID 31 departs six minutes after timestamp t.

#     Bus ID 19 departs seven minutes after timestamp t.

# The only bus departures that matter are the listed bus IDs at their specific
# offsets from t. Those bus IDs can depart at other times, and other bus IDs can
# depart at those times. For example, in the list above, because bus ID 19 must
# depart seven minutes after the timestamp at which bus ID 7 departs, bus ID 7
# will always also be departing with bus ID 19 at seven minutes after timestamp
# t.

# In this example, the earliest timestamp at which this occurs is 1068781:

# time     bus 7   bus 13  bus 59  bus 31  bus 19
# 1068773    .       .       .       .       .
# 1068774    D       .       .       .       .
# 1068775    .       .       .       .       .
# 1068776    .       .       .       .       .
# 1068777    .       .       .       .       .
# 1068778    .       .       .       .       .
# 1068779    .       .       .       .       .
# 1068780    .       .       .       .       .
# 1068781    D       .       .       .       .
# 1068782    .       D       .       .       .
# 1068783    .       .       .       .       .
# 1068784    .       .       .       .       .
# 1068785    .       .       D       .       .
# 1068786    .       .       .       .       .
# 1068787    .       .       .       D       .
# 1068788    D       .       .       .       D
# 1068789    .       .       .       .       .
# 1068790    .       .       .       .       .
# 1068791    .       .       .       .       .
# 1068792    .       .       .       .       .
# 1068793    .       .       .       .       .
# 1068794    .       .       .       .       .
# 1068795    D       D       .       .       .
# 1068796    .       .       .       .       .
# 1068797    .       .       .       .       .

# In the above example, bus ID 7 departs at timestamp 1068788 (seven minutes
# after t). This is fine; the only requirement on that minute is that bus ID 19
# departs then, and it does.

# Here are some other examples:

#     The earliest timestamp that matches the list 17,x,13,19 is 3417.
#     67,7,59,61 first occurs at timestamp 754018.
#     67,x,7,59,61 first occurs at timestamp 779210.
#     67,7,x,59,61 first occurs at timestamp 1261476.
#     1789,37,47,1889 first occurs at timestamp 1202161486.

# However, with so many bus IDs in your list, surely the actual earliest
# timestamp will be larger than 100000000000000!

# What is the earliest timestamp such that all of the listed bus IDs depart at
# offsets matching their positions in the list?

import sys 
import math

def main( argv ):

    # Read in input file
    with open( "input/day13-input.txt", "r" ) as f:
        data = [ line.rstrip() for line in f ]

    #data = [ "939", "7,13,x,x,59,x,31,19" ]

    # Part 1

    myId = int( data[ 0 ] )
    busList = []

    for bus in data[ 1 ].split( ',' ):
        # Skip x's for now
        if bus == 'x':
            continue

        # For each bus, see how close it is to coming and add the arrival time
        # to the list along with the bus number
        b = int( bus )
        busList.append( [ b * math.floor( myId / float( b ) ) + b, b ] )

    busList.sort( key=lambda b: b[ 0 ] )

    print( "Part 1 answer: %s" % (busList[ 0 ][ 1 ] * (busList[ 0 ][ 0 ]-myId)) )

    # Part 2

    x = []
    m = []

    # We need bus numbers (modulo) and their offset i the array subtracted from the 
    # bus number (we want the offset AFTER the last whole number, not before).
    for i, bus in enumerate( data[ 1 ].split( ',' ) ):
        if bus == 'x':
            continue

        m.append( int( bus ) )
        x.append( int( bus ) - i )

    print( "Part 2 answer: %s" % crt( m, x ) ) 

# Functions below are for implementing the Chinese Remainder Theorm.  Note that this 
# is not my own code.  Taken from: 
#   https://www.geeksforgeeks.org/using-chinese-remainder-theorem-combine-modular-equations/
#
# Part 2 essentially works out to a system of crongruences ('=' is congruence, not equals):
#
#    7: t
#    13: t+1
#    x: t+2
#    x: t+3
#   59: t+4
#    x: t+5
#   31: t+6
#   19: t+7
#
# Find t such that:
#
#     (t    % 7) = 0 
#   ((t+1) % 13 = 0)
#   ((t+4) % 59 = 0)
#   ((t+6) % 31 = 0)
#   ((t+7) % 19 = 0)
#
#   t =  0 (mod 7)
#   t = 12 (mod 13) -> (13-1)
#   t = 55 (mod 59) -> (59-4)
#   t = 25 (mod 31) -> (31-6)
#   t = 12 (mod 19) -> (19-7)
#
# 1, 4, 6, 7 are the offsets in time of each bus after the first.  We subtract that from the 
# module as we want the time after the first whole division of t=0 rather than before. Note 
# this all works because the modulo/bus numbers are all co-prime with each other.
#
# A little bit of searching the adventofcode reddit seems to indicate that coming up with
# an algoritm that is more or less the CRT is fairly simple if you start thining about it
# in terms of the remainders and combining all the equations, a pair at a time:
#
#   "I just figured you could combine two routes into one meta-route, and the
#   "solution" for combining them is going to repeat every N minutes... So you
#   find the first two instances where the "solution" occurs -- the first will be
#   the offset (from 0) and the second minus the first gives you the cycle time
#   (the route number) and you can keep combining more routes into the meta-route."
#
# ---------------
#
# function that implements Extended euclidean 
# algorithm 
def extended_euclidean(a, b): 
    if a == 0: 
        return (b, 0, 1) 
    else: 
        g, y, x = extended_euclidean(b % a, a) 
        return (g, x - (b // a) * y, y) 
  
# modular inverse driver function 
def modinv(a, m): 
    g, x, y = extended_euclidean(a, m) 
    return x % m 

# function implementing Chinese remainder theorem 
def crt(m, x): 
  
    # We run this loop while the list of 
    # remainders has length greater than 1 
    while True: 
          
        # temp1 will contain the new value  
        # of A. which is calculated according  
        # to the equation m1' * m1 * x0 + m0' 
        # * m0 * x1 
        temp1 = modinv(m[1],m[0]) * x[0] * m[1] + modinv(m[0],m[1]) * x[1] * m[0] 
  
        # temp2 contains the value of the modulus 
        # in the new equation, which will be the  
        # product of the modulii of the two 
        # equations that we are combining 
        temp2 = m[0] * m[1] 
  
        # we then remove the first two elements 
        # from the list of remainders, and replace 
        # it with the remainder value, which will 
        # be temp1 % temp2 
        x.remove(x[0]) 
        x.remove(x[0]) 
        x = [temp1 % temp2] + x  
  
        # we then remove the first two values from 
        # the list of modulii as we no longer require 
        # them and simply replace them with the new  
        # modulii that  we calculated 
        m.remove(m[0]) 
        m.remove(m[0]) 
        m = [temp2] + m 
  
        # once the list has only one element left, 
        # we can break as it will only  contain  
        # the value of our final remainder 
        if len(x) == 1: 
            break
  
    # returns the remainder of the final equation 
    return x[0] 

if __name__ == "__main__":
    main( argv=sys.argv )