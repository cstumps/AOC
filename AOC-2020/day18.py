# --- Day 18: Operation Order ---

# As you look out the window and notice a heavily-forested continent slowly
# appear over the horizon, you are interrupted by the child sitting next to you.
# They're curious if you could help them with their math homework.

# Unfortunately, it seems like this "math" follows different rules than you
# remember.

# The homework (your puzzle input) consists of a series of expressions that
# consist of addition (+), multiplication (*), and parentheses ((...)). Just
# like normal math, parentheses indicate that the expression inside must be
# evaluated before it can be used by the surrounding expression. Addition still
# finds the sum of the numbers on both sides of the operator, and multiplication
# still finds the product.

# However, the rules of operator precedence have changed. Rather than evaluating
# multiplication before addition, the operators have the same precedence, and
# are evaluated left-to-right regardless of the order in which they appear.

# For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as
# follows:

# 1 + 2 * 3 + 4 * 5 + 6
#   3   * 3 + 4 * 5 + 6
#       9   + 4 * 5 + 6
#          13   * 5 + 6
#              65   + 6
#                  71

# Parentheses can override this order; for example, here is what happens if
# parentheses are added to form 1 + (2 * 3) + (4 * (5 + 6)):

# 1 + (2 * 3) + (4 * (5 + 6))
# 1 +    6    + (4 * (5 + 6))
#      7      + (4 * (5 + 6))
#      7      + (4 *   11   )
#      7      +     44
#             51

# Here are a few more examples:

#     2 * 3 + (4 * 5) becomes 26.
#     5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
#     5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
#     ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.

# Before you can help with the homework, you need to understand it yourself.
# Evaluate the expression on each line of the homework; what is the sum of the
# resulting values?

# --- Part Two ---

# You manage to answer the child's questions and they finish part 1 of their
# homework, but get stuck when they reach the next section: advanced math.

# Now, addition and multiplication have different precedence levels, but they're
# not the ones you're familiar with. Instead, addition is evaluated before
# multiplication.

# For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are
# now as follows:

# 1 + 2 * 3 + 4 * 5 + 6
#   3   * 3 + 4 * 5 + 6
#   3   *   7   * 5 + 6
#   3   *   7   *  11
#      21       *  11
#          231

# Here are the other examples from above:

#     1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
#     2 * 3 + (4 * 5) becomes 46.
#     5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
#     5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
#     ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.

# What do you get if you add up the results of evaluating the homework problems
# using these new rules?

# I'll admit that I knew going into implementation that I wanted to convert to postfix
# notation to evaluate the equations.  Rather than re-invent the wheel I implemented a
# known algorithm to do the work.  Even found some code to base mine on.

import sys 
import re

def main( argv ):

    # Read in input file
    with open( "input/day18-input.txt", "r" ) as f:
        data = [ line.rstrip() for line in f ]

    #data = "1 + (2 * 3) + (4 * (5 + 6))"
    #data = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"

    ans = 0
    conv = PostfixStack()

    for line in data:
        eq = line.replace( '(', '( ' ).replace( ')', ' )' )
        ans += conv.evaluate( eq.split() )

    print( "Part 1 answer: %s" % ans )

class PostfixStack( object ):
    def __init__( self ):
        self.array = []   # Stack
        self.output = []  # Output stream

        self.priority = { '+': 2, '*':1 }

    def isEmpty( self ):
        return not len( self.array )
    
    def clear( self ):
        self.array.clear()
        self.output.clear()

    def push( self, val ):
        self.array.append( val )

    def pop( self ):
        if self.isEmpty():
            return None
        else:
            return self.array.pop()

    def peek( self ):
        if self.isEmpty():
            return None
        else:
            return self.array[ len( self.array ) - 1 ]

    def isOperand( self, val ):
        try:
            int( val )
        except ValueError:
            return False

        return True

    # Is the passed in value higher priority than the top of the stack
    def hasPriority( self, val ):
        return self.priority[ self.peek() ] < self.priority[ val ]

    def evaluate( self, lst ):
        self.clear()
        self.infixToPostfix( lst )
        self.array.clear() # Reuse self.array

        for c in self.output:
            if self.isOperand( c ):
                self.push( c )
            else:
                self.push( str( eval( self.pop() + c + self.pop() ) ) )

        return int( self.pop() )

    def infixToPostfix( self, lst ):
        for token in lst:
            if self.isOperand( token ):
                self.output.append( token )
            elif token == '(':
                self.push( token )
            elif token == ')':
                val = self.pop()
                
                while val != '(':
                    self.output.append( val )
                    val = self.pop()
            else:
                while not self.isEmpty() and self.peek() != '(' and not self.hasPriority( token ):
                    self.output.append( self.pop() )

                self.push( token )

        while not self.isEmpty():
            self.output.append( self.pop() )
        
        return self.output.copy()

if __name__ == "__main__":
    main( argv=sys.argv )