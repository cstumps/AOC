# --- Day 19: Monster Messages ---

# You land in an airport surrounded by dense forest. As you walk to your
# high-speed train, the Elves at the Mythical Information Bureau contact you
# again. They think their satellite has collected an image of a sea monster!
# Unfortunately, the connection to the satellite is having problems, and many of
# the messages sent back from the satellite have been corrupted.

# They sent you a list of the rules valid messages should obey and a list of
# received messages they've collected so far (your puzzle input).

# The rules for valid messages (the top part of your puzzle input) are numbered
# and build upon each other. For example:

# 0: 1 2
# 1: "a"
# 2: 1 3 | 3 1
# 3: "b"

# Some rules, like 3: "b", simply match a single character (in this case, b).

# The remaining rules list the sub-rules that must be followed; for example, the
# rule 0: 1 2 means that to match rule 0, the text being checked must match rule
# 1, and the text after the part that matched rule 1 must then match rule 2.

# Some of the rules have multiple lists of sub-rules separated by a pipe (|).
# This means that at least one list of sub-rules must match. (The ones that
# match might be different each time the rule is encountered.) For example, the
# rule 2: 1 3 | 3 1 means that to match rule 2, the text being checked must
# match rule 1 followed by rule 3 or it must match rule 3 followed by rule 1.

# Fortunately, there are no loops in the rules, so the list of possible matches
# will be finite. Since rule 1 matches a and rule 3 matches b, rule 2 matches
# either ab or ba. Therefore, rule 0 matches aab or aba.

# Here's a more interesting example:

# 0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"

# Here, because rule 4 matches a and rule 5 matches b, rule 2 matches two
# letters that are the same (aa or bb), and rule 3 matches two letters that are
# different (ab or ba).

# Since rule 1 matches rules 2 and 3 once each in either order, it must match
# two pairs of letters, one pair with matching letters and one pair with
# different letters. This leaves eight possibilities: aaab, aaba, bbab, bbba,
# abaa, abbb, baaa, or babb.

# Rule 0, therefore, matches a (rule 4), then any of the eight options from rule
# 1, then b (rule 5): aaaabb, aaabab, abbabb, abbbab, aabaab, aabbbb, abaaab, or
# ababbb.

# The received messages (the bottom part of your puzzle input) need to be
# checked against the rules so you can determine which are valid and which are
# corrupted. Including the rules and the messages together, this might look
# like:

# 0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"

# ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb

# Your goal is to determine the number of messages that completely match rule 0.
# In the above example, ababbb and abbbab match, but bababa, aaabbb, and aaaabbb
# do not, producing the answer 2. The whole message must match all of rule 0;
# there can't be extra unmatched characters in the message. (For example,
# aaaabbb might appear to match rule 0 above, but it has an extra unmatched b on
# the end.)

# How many messages completely match rule 0?

# --- Part Two ---

# As you look over the list of messages, you realize your matching rules aren't
# quite right. To fix them, completely replace rules 8: 42 and 11: 42 31 with
# the following:

# 8: 42 | 42 8
# 11: 42 31 | 42 11 31

# This small change has a big impact: now, the rules do contain loops, and the
# list of messages they could hypothetically match is infinite. You'll need to
# determine how these changes affect which messages are valid.

# Fortunately, many of the rules are unaffected by this change; it might help to
# start by looking at which rules always match the same set of values and how
# those rules (especially rules 42 and 31) are used by the new versions of rules
# 8 and 11.

# (Remember, you only need to handle the rules you have; building a solution
# that could handle any hypothetical combination of rules would be significantly
# more difficult.)

# For example:

# 42: 9 14 | 10 1
# 9: 14 27 | 1 26
# 10: 23 14 | 28 1
# 1: "a"
# 11: 42 31
# 5: 1 14 | 15 1
# 19: 14 1 | 14 14
# 12: 24 14 | 19 1
# 16: 15 1 | 14 14
# 31: 14 17 | 1 13
# 6: 14 14 | 1 14
# 2: 1 24 | 14 4
# 0: 8 11
# 13: 14 3 | 1 12
# 15: 1 | 14
# 17: 14 2 | 1 7
# 23: 25 1 | 22 14
# 28: 16 1
# 4: 1 1
# 20: 14 14 | 1 15
# 3: 5 14 | 16 1
# 27: 1 6 | 14 18
# 14: "b"
# 21: 14 1 | 1 14
# 25: 1 1 | 1 14
# 22: 14 14
# 8: 42
# 26: 14 22 | 1 20
# 18: 15 15
# 7: 14 5 | 1 21
# 24: 14 1

# abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
# bbabbbbaabaabba
# babbbbaabbbbbabbbbbbaabaaabaaa
# aaabbbbbbaaaabaababaabababbabaaabbababababaaa
# bbbbbbbaaaabbbbaaabbabaaa
# bbbababbbbaaaaaaaabbababaaababaabab
# ababaaaaaabaaab
# ababaaaaabbbaba
# baabbaaaabbaaaababbaababb
# abbbbabbbbaaaababbbbbbaaaababb
# aaaaabbaabaaaaababaa
# aaaabbaaaabbaaa
# aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
# babaaabbbaaabaababbaabababaaab
# aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba

# Without updating rules 8 and 11, these rules only match three messages:
# bbabbbbaabaabba, ababaaaaaabaaab, and ababaaaaabbbaba.

# However, after updating rules 8 and 11, a total of 12 messages match:

#     bbabbbbaabaabba
#     babbbbaabbbbbabbbbbbaabaaabaaa
#     aaabbbbbbaaaabaababaabababbabaaabbababababaaa
#     bbbbbbbaaaabbbbaaabbabaaa
#     bbbababbbbaaaaaaaabbababaaababaabab
#     ababaaaaaabaaab
#     ababaaaaabbbaba
#     baabbaaaabbaaaababbaababb
#     abbbbabbbbaaaababbbbbbaaaababb
#     aaaaabbaabaaaaababaa
#     aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
#     aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba

# After updating rules 8 and 11, how many messages completely match rule 0?

# I can't take full credit for this solution.  I started off looking at writing my own parser
# handle this but thought better of it.  Originally wanted to use python's built in regex in
# some fashion but couldn't figure out how to format it.  A look at the reddit showed it was 
# possible.  A little experimenting with it got it giving me an answer but a wrong one.  
# Further reading showed that I had a rule that wasn't parsing right because I was replacing
# all occurance rather than one at a time.  Changing to max replace of 1 fixed this.  We 
# replace left to right.  In part 2 I started by getting the updated replacement from rule 8
# correct but struggled with rule 11.  Reddit gave enough hints to use {x} and iterate thru
# the possible values of x.  
#
# Clearly there are some insights that could have been made from looking closer at the rules
# and the possible strings.  Unfortunately I was a little burned out and couldn't spend the 
# time to make these relevations.  I also had soem trouble wrapping my head around how the
# regex pattern comparisson actually works.
#
# As a furture project it might be interesting to implement a parser for regex soemtime. 
# See:
#   https://deniskyashif.com/2020/08/17/parsing-regex-with-recursive-descent/
#   https://deniskyashif.com/2019/02/17/implementing-a-regular-expression-engine/

import sys 
import re

def main( argv ):

    # Read in input file
    with open( "input/day19-input.txt", "r" ) as f:
        data = [ line.rstrip() for line in f ]

    # Read in rules into dictionary
    rules = { l.split(':')[ 0 ]: l.split(':')[ 1 ].strip() for l in data[ :data.index( '' ) ] if l != '' }

    # Starting location of strings to match
    dataStart = data.index( '' ) + 1

    # Part 1
    redEx = buildRegex( rules, rules[ '0' ] )

    reg = re.compile( '^' + redEx + '$' )
    count = 0

    for line in data[ dataStart: ]:
        if reg.match( line ):
            count += 1

    print( "Part 1 answer: %s " % count )

    # Part 2

    rules[ '8' ] = '42 +'
    rules[ '11' ] = '42 {x} 31 {x}'

    redEx = buildRegex( rules, rules[ '0' ] )
    count = 0

    # Here we know that for rule 11 the number of 42's and 31's has to be equal.  The only
    # way to do this is regex is to iterate over the number x until we stop matching.  In 
    # theory there could be a gap between valid numbers for x but it's unlikely since the 
    # strings we're comparing against aren't particularily long.  10 iterations was more 
    # than enough (really the max was 4).
    for x in range( 1, 10 ):
        reg = re.compile( '^' + redEx.replace( 'x', str( x ) ) + '$' )

        for line in data[ dataStart: ]:
            if reg.match( line ):
                count += 1
        
    print( "Part 2 answer: %s " % count )

def buildRegex( rules, redEx ):
    # Note that the replacement count of 1 is important here.  We are proceeding left to right
    # and if that's not present we could replace a '11' with the value for a '1' twice.

    subMade = True

    # Build a regex from rule set
    while subMade:
        for i, r in enumerate( redEx.split() ):
            if r.isdigit():
                if rules[ r ][ 0 ] == '\"':
                    redEx = redEx.replace( r, rules[ r ][ 1 ], 1 )
                else:
                    redEx = redEx.replace( r, ' ( ' + rules[ r ] + ' ) ', 1 )
                
                subMade = True
                break
        else:
            subMade = False

    # Strip out the spaces
    redEx = redEx.replace( ' ', '' )

    return redEx

if __name__ == "__main__":
    main( argv=sys.argv )