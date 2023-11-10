# --- Day 3: Spiral Memory ---

# You come across an experimental new kind of memory stored on an infinite two-
# dimensional grid.

# Each square on the grid is allocated in a spiral pattern starting at a
# location marked 1 and then counting up while spiraling outward. For example,
# the first few squares are allocated like this:

# 17  16  15  14  13 
# 18   5   4   3  12 
# 19   6   1   2  11 
# 20   7   8   9  10 
# 21  22  23  24  25  26

# While this is very space-efficient (no squares are skipped), requested data
# must be carried back to square 1 (the location of the only access port for
# this memory system) by programs that can only move up, down, left, or right.
# They always take the shortest path: the Manhattan Distance between the
# location of the data and square 1.

# For example:

# Data from square 1 is carried 0 steps, since it's at the access port.

# Data from square 12 is carried 3 steps, such as: down, left, left.

# Data from square 23 is carried only 2 steps: up twice.

# Data from square 1024 must be carried 31 steps.

# How many steps are required to carry the data from the square identified in
# your puzzle input all the way to the access port?

# Your puzzle input is 368078.

# --- Part Two ---

# As a stress test on the system, the programs here clear the grid and then
# store the value 1 in square 1. Then, in the same allocation order as shown
# above, they store the sum of the values in all adjacent squares, including
# diagonals.

# So, the first few squares' values are chosen as follows:

# Square 1 starts with the value 1.

# Square 2 has only one adjacent filled square (with value 1), so it also stores
# 1.

# Square 3 has both of the above squares as neighbors and stores the sum of
# their values, 2.

# Square 4 has all three of the aforementioned squares as neighbors and stores
# the sum of their values, 4.

# Square 5 only has the first and fourth squares as neighbors, so it gets the
# value 5.

# Once a square is written, its value does not change. Therefore, the first few
# squares would receive the following values:

# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...

# What is the first value written that is larger than your puzzle input?

import sys
import math

def main( argv ):

	d = part_1( 277678 )
	v = part_2( 277678 )

	print( "Distance: %s" % d )
	print( "First val: %s" % v )

	# Part 2 is ugly, not the best way to do it to be sure.

def part_1( target ):
	ind = 1
	cur = 1
	prev = 1
	total = 1 # Start out with the first step in place

	while (total + 1) <= target:
		prev = cur

		cur += (1 - (ind % 2))
		ind += 1

		total += cur

	# At this point we know the length of the side that the target is on (cur)
	total += 1

	if prev % 2:
		s1 = math.floor( (prev + 1) / 2 )
	else:
		s1 = math.floor( prev / 2 )

	s2 = math.fabs( math.floor( (cur + 1) / 2 ) - (total - target) )

	return s1 + s2

def part_2( target ):

	w = 20
	h = 20

	val = 1
	dir = 'r'

	grid = [ [ 0 for x in range( w ) ] for y in range( h ) ] 

	x = 9
	y = 9

	grid[ x ][ y ] = 1
	x += 1

	while val <= target:

		if dir == 'r':
			val = sum_adj( grid, x, y )
			grid[ x ][ y ] = val

			if grid[ x ][ y-1 ] != 0:
				x += 1
			else:
				y -= 1
				dir = 'u'

		elif dir == 'u':
			val = sum_adj( grid, x, y )
			grid[ x ][ y ] = val

			if grid[ x-1 ][ y ] != 0:
				y -= 1
			else:
				x -= 1
				dir = 'l'

		elif dir == 'l':
			val = sum_adj( grid, x, y )
			grid[ x ][ y ] = val

			if grid[ x ][ y + 1 ] != 0:
				x -= 1
			else:
				y += 1
				dir = 'd'

		else:
			val = sum_adj( grid, x, y )
			grid[ x ][ y ] = val

			if grid[ x+1 ][ y ] != 0:
				y += 1
			else:
				x += 1
				dir = 'r'

	#print('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in grid]))

	return val

def sum_adj( g, x, y ):
	return g[ x-1 ][ y-1 ] + g[ x ][ y-1 ] + g[ x-1 ][ y ] + g[ x+1 ][ y+1 ] + g[ x ][ y+1 ] + g[ x+1 ][ y ] + g[ x+1 ][ y-1 ] + g[ x-1 ][ y+1 ]

if __name__ == "__main__":
	main( argv = sys.argv )
