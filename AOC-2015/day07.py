# --- Day 7: Some Assembly Required ---

# This year, Santa brought little Bobby Tables a set of wires and bitwise logic
# gates! Unfortunately, little Bobby is a little under the recommended age
# range, and he needs help assembling the circuit.

# Each wire has an identifier (some lowercase letters) and can carry a 16-bit
# signal (a number from 0 to 65535). A signal is provided to each wire by a
# gate, another wire, or some specific value. Each wire can only get a signal
# from one source, but can provide its signal to multiple destinations. A gate
# provides no signal until all of its inputs have a signal.

# The included instructions booklet describes how to connect the parts together:
# x AND y -> z means to connect wires x and y to an AND gate, and then connect
# its output to wire z.

# For example:

#     123 -> x means that the signal 123 is provided to wire x.

#     x AND y -> z means that the bitwise AND of wire x and wire y is provided
#     to wire z.

#     p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and
#     then provided to wire q.

#     NOT e -> f means that the bitwise complement of the value from wire e is
#     provided to wire f.

# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for
# some reason, you'd like to emulate the circuit instead, almost all programming
# languages (for example, C, JavaScript, or Python) provide operators for these
# gates.

# For example, here is a simple circuit:

# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i

# After it is run, these are the signals on the wires:

# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456

# In little Bobby's kit's instructions booklet (provided as your puzzle input),
# what signal is ultimately provided to wire a?

# --- Part Two ---

# Now, take the signal you got on wire a, override wire b to that signal, and
# reset the other wires (including wire a). What new signal is ultimately
# provided to wire a?

import sys
import numpy as np

# This is kind of a clunky implementation but it works.

def main( argv ):

    data = []

    # Read in input file and add up the sums
    with open( "input/day07-input.txt", "r" ) as f:
        data = f.readlines()

    #data = [ '123 -> x',
    #         '456 -> y',
    #         'x AND y -> d',
    #         'x OR y -> e',
    #         'x LSHIFT 2 -> f',
    #         'y RSHIFT 2 -> g',
    #         'NOT x -> h',
    #         'NOT y -> i' ]


    ##
    # Part 1
    ##

    circuit = Circuit( data )
    wires = circuit.solve()

    print( f"Part 1 answer: {wires[ 'a' ]}" )

    ##
    # Part 2
    ##

    # Take part 1 answer and inject it in data for part 2
    circuit = Circuit( data )
    circuit.addWire( 'b', wires[ 'a' ] )

    wires = circuit.solve()

    print( f"Part 2 answer: {wires[ 'a' ]}" )

class Circuit:
    def __init__( self, data ):
        self.wires = {}   # Dictionary of wires and their values
        self.devices = [] # List of lists ([ [device, wire, op1, op2] ])

        for line in data:
            line = line.split( '->' )

            wire = line[ 1 ].strip()
            lhs  = line[ 0 ].strip()

            if lhs.isdigit():
                self.addWire( wire, int( lhs ) )
            else:
                lhs = lhs.split()

                if len( lhs ) == 2: # NOT
                    self.addDevice( lhs[ 0 ].strip(), wire, lhs[ 1 ].strip() )
                elif len( lhs ) == 1: # xx -> a
                    self.addDevice( 'WIRE', wire, lhs[ 0 ].strip() )
                else: # x DEV y
                    if lhs[ 2 ].strip().isdigit():
                        op2 = int( lhs[ 2 ].strip() )
                    else:
                        op2 = lhs[ 2 ].strip()

                    if lhs[ 0 ].strip().isdigit():
                        op1 = int( lhs[ 0 ].strip() )
                    else:
                        op1 = lhs[ 0 ].strip()

                    self.addDevice( lhs[ 1 ].strip(), wire, op1, op2 )

    def addWire( self, wire, value ):
        self.wires[ wire ] = value

    def addDevice( self, device, wire, op1, op2=None ):
        self.devices.append( [device, wire, op1, op2] )

    def reduceDevices( self ):
        removeList = []

        for device in self.devices:
            if device[ 0 ] == 'AND':
                if device[ 3 ] in self.wires.keys():
                    if device[ 2 ] in self.wires.keys():
                        self.wires[ device[ 1 ] ] = self.wires[ device[ 2 ] ] & self.wires[ device[ 3 ] ]
                        removeList.append( device )
                    elif isinstance( device[ 2 ], int ):
                        self.wires[ device[ 1 ] ] = device[ 2 ] & self.wires[ device[ 3 ] ]
                        removeList.append( device )

            elif device[ 0 ] == 'OR':
                if device[ 2 ] in self.wires.keys() and device[ 3 ] in self.wires.keys():
                    self.wires[ device[ 1 ] ] = self.wires[ device[ 2 ] ] | self.wires[ device[ 3 ] ]
                    removeList.append( device )

            elif device[ 0 ] == 'LSHIFT':
                if device[ 2 ] in self.wires.keys():
                    self.wires[ device[ 1 ] ] = self.wires[ device[ 2 ] ] << device[ 3 ]
                    removeList.append( device )

            elif device[ 0 ] == 'RSHIFT':
                if device[ 2 ] in self.wires.keys():
                    self.wires[ device[ 1 ] ] = self.wires[ device[ 2 ] ] >> device[ 3 ]
                    removeList.append( device )

            elif device[ 0 ] == 'NOT':
                if device[ 2 ] in self.wires.keys():
                    self.wires[ device[ 1 ] ] = ~self.wires[ device[ 2 ] ]
                    removeList.append( device )
            elif device[ 0 ] == 'WIRE':
                if device[ 2 ] in self.wires.keys():
                    self.wires[ device[ 1 ] ] = self.wires[ device[ 2 ] ]
                    removeList.append( device )
            else:
                raise MyError( "Error: Unknown device" )
            
        # Now process the removal list
        for item in removeList:
            self.devices.remove( item )

    def solve( self ):
        while len( self.devices ):
            self.reduceDevices()

        return self.wires


class MyError( Exception ):
    def __init__( self, value ):
        self.value = value

    def __str__( self ):
        return repr( self.value )

if __name__ == "__main__":
    main( argv=sys.argv )
