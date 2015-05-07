__author__ = 'skebix'

'''Add another parameter, named length, to square. Modify the body so length of the sides is length, and then modify the
function call to provide a second argument. Run the program again. Test your program with a range of values for length.
'''

from swampy.TurtleWorld import *

w = TurtleWorld()
bob = Turtle()

def square(t, length):
    """
    Draws a square of the given length with a Turtle t.
    The turtle returns to its original position.
    """
    for i in range(4):
        fd(t, length)
        lt(t)

square(bob, 21)