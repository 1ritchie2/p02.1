"""
Problem:

    The function biggest takes in three variables: a, b and c.
    It should print out the biggest of the three.

Tests:

    >>> biggest(10, 12, 7)
    12
    >>> biggest(27, 16, 22)
    27
    >>> biggest(15, 11, 19)
    19
    >>> biggest(11, 6, 11)
    11

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)

#   Putting this here as i need to re add the code to git bash
# Edit this code
def biggest(a, b, c):

    if a > b > c:
        print(a)

    elif a < b < c:
        print(c)

    elif a < b > c:
        print(b)

    elif a == b > c:
        print(a)

    elif a < b == c:
        print(b)

    elif a >b < c == a:
        print(c) 

    
