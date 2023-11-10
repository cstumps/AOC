# --- Day 4: High-Entropy Passphrases ---

# A new system policy has been put in place that requires all accounts to use a
# passphrase instead of simply a password. A passphrase consists of a series of
# words (lowercase letters) separated by spaces.

# To ensure security, a valid passphrase must contain no duplicate words.

# For example:

# aa bb cc dd ee is valid.

# aa bb cc dd aa is not valid - the word aa appears more than once.

# aa bb cc dd aaa is valid - aa and aaa count as different words.

# The system's full passphrase list is available as your puzzle input. How many
# passphrases are valid?

# --- Part Two ---

# For added security, yet another system policy has been put in place. Now, a
# valid passphrase must contain no two words that are anagrams of each other -
# that is, a passphrase is invalid if any word's letters can be rearranged to
# form any other word in the passphrase.

# For example:

# abcde fghij is a valid passphrase.

# abcde xyz ecdab is not valid - the letters from the third word can be
# rearranged to form the first word.

# a ab abc abd abf abj is a valid passphrase, because all letters need to be
# used when forming another word. iiii oiii ooii oooi oooo is valid.

# oiii ioii iioi iiio is not valid - any of these words can be rearranged to
# form any other word.

# Under this new system policy, how many passphrases are valid?

import sys
import math

def main( argv ):

	with open( "input/day04-input.txt", "r" ) as f:
		data = f.readlines()

	v1 = part_1( data )
	v2 = part_2( data )

	print( "Part 1 valid phrases: %s" % v1 )
	print("Part 2 valid phrases: %s" % v2 )
	

def part_1( data ):
	valid = 0

	for line in data:
		line = line.split()

		if len( set( line ) ) == len( line ):
			valid += 1

	return valid
	

def part_2( data ):
	valid = 0

	for line in data:
		line = line.split()
		s = set()

		# Split each item in the list, sort, and rejoin
		for word in line:
			w = list( word )
			w.sort()
			s.add( "".join( w ) )

		if len( s ) == len( line ):
			valid += 1

	return valid


if __name__ == "__main__":
	main( argv = sys.argv )
