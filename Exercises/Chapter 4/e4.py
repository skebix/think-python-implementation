__author__ = 'skebix'

'''
Write a function called circle that takes a turtle, t, and radius, r, as parameters and that draws an approximate circle
by invoking polygon with an appropriate length and number of sides. Test your function with a range of values of r.

Hint: figure out the circumference of the circle and make sure that length * n = circumference.

Another hint: if bob is too slow for you, you can speed him up by changing bob.delay, which is the time between moves,
in seconds. bob.delay = 0.01 ought to get him moving.
'''

from swampy.TurtleWorld import *
from e3 import polygon
from math import pi

world = TurtleWorld()
turtle = Turtle()
turtle.delay = 0.01

def circle(t, r):
    circumference = 2 * pi * r
    sides = 80
    length = circumference / sides
    polygon(t, sides, length)

circle(turtle, 80)