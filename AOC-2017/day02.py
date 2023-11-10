# --- Day 2: Corruption Checksum ---

# As you walk through the door, a glowing humanoid shape yells in your direction.
# "You there! Your state appears to be idle. Come help us repair the corruption in
# this spreadsheet - if we take another millisecond, we'll have to display an
# hourglass cursor!"

# The spreadsheet consists of rows of apparently-random numbers. To make sure the
# recovery process is on the right track, they need you to calculate the
# spreadsheet's checksum. For each row, determine the difference between the
# largest value and the smallest value; the checksum is the sum of all of these
# differences.

# For example, given the following spreadsheet:

# 5 1 9 5 
# 7 5 3
# 2 4 6 8

# The first row's largest and smallest values are 9 and 1, and their difference is
# 8.

# The second row's largest and smallest values are 7 and 3, and their difference
# is 4.

# The third row's difference is 6.

# In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

# What is the checksum for the spreadsheet in your puzzle input?

# Your puzzle answer was 45158.

# The first half of this puzzle is complete! It provides one gold star: *

# --- Part Two ---

# "Great work; looks like we're on the right track after all. Here's a star for
# "your effort. However, the program seems a little worried. Can programs be
# "worried?

# "Based on what we're seeing, it looks like all the User wanted is some
# "information about the evenly divisible values in the spreadsheet.
# "Unfortunately, none of us are equipped for that kind of calculation - most of
# "us specialize in bitwise operations.

# It sounds like the goal is to find the only two numbers in each row where one
# evenly divides the other - that is, where the result of the division operation
# is a whole number. They would like you to find those numbers on each line,
# divide them, and add up each line's result.

# For example, given the following spreadsheet:

# 5 9 2 8 
# 9 4 7 3 
# 3 8 6 5

# In the first row, the only two numbers that evenly divide are 8 and 2; the
# result of this division is 4.

# In the second row, the two numbers are 9 and 3; the result is 3.

# In the third row, the result is 2.

# In this example, the sum of the results would be 4 + 3 + 2 = 9.

# What is the sum of each row's result in your puzzle input?

import sys
import itertools

def main( argv ):

	with open( "input/day02-input.txt", "r" ) as f:
		data = f.readlines()

	p1 = part_1( data )
	p2 = part_2( data )

	print( "Part 1 checksum:  " + str( p1 ) )
	print( "Part 2 checksum:  " + str( p2 ) )


def part_1( input ):
	chk = 0

	for line in input:
		# Format and convert to integers
		line = line.strip().split( '\t' )
		line = list( map( int, line ) )

		mx = max( line )
		mn = min( line )

		chk += (mx - mn)

	return chk


def part_2( input ):
	chk = 0

	for line in input:
		# Format and convert to integers
		line = line.strip().split( '\t' )
		line = map( int, line )

		pairs = list( itertools.combinations( line, 2 ) )

		for p in pairs:
			if max( p ) % min( p ) == 0:
				chk += max( p ) / min( p )

	return chk

if __name__ == "__main__":
	main( argv = sys.argv )
