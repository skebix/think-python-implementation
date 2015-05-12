__author__ = 'skebix'

'''
The Koch curve is a fractal that looks something like Figure 5.2. To draw a Koch curve with length x, all you have to do
is:

1. Draw a Koch curve with length x/3.
2. Turn left 60 degrees.
3. Draw a Koch curve with length x/3.
4. Turn right 120 degrees.
5. Draw a Koch curve with length x/3.
6. Turn left 60 degrees.
7. Draw a Koch curve with length x/3.

The exception is if x is less than 3: in that case, you can just draw a straight line with length x.

1. Write a function called koch that takes a turtle and a length as parameters, and that uses the turtle to draw a Koch
curve with the given length.
'''

from swampy.TurtleWorld import *

#w = TurtleWorld()
#bob = Turtle()
#bob.delay = 0.01

def koch(t, l):
    """Uses turtle t to draw a Koch fractal of length l."""
    if l < 3:
        fd(t, l)
    else:
        third = l / 3.0
        koch(t, third)
        lt(t, 60)
        koch(t, third)
        rt(t, 120)
        koch(t, third)
        lt(t, 60)
        koch(t, third)

#koch(bob, 150)