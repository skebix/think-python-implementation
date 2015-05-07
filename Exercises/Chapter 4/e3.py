__author__ = 'skebix'

'''
The functions lt and rt make 90-degree turns by default, but you can provide a second argument that specifies the number
of degrees. For example, lt(bob, 45) turns bob 45 degrees to the left.

Make a copy of square and change the name to polygon. Add another parameter named n and modify the body so it draws an
n-sided regular polygon. Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.
'''

from swampy.TurtleWorld import *

#w = TurtleWorld()
bob = Turtle()

def polygon(t, sides, length):
    """
    Draws a n-sided polygon of given length. t is a Turtle.
    """
    angle = 360.0 / sides
    for i in range(sides):
        fd(t, length)
        lt(t, angle)

#polygon(bob, 8, 21)