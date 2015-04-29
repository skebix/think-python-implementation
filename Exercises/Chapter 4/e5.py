__author__ = 'skebix'

'''
Make a more general version of circle called arc that takes an additional parameter angle, which determines what
fraction of a circle to draw. angle is in units of degrees, so when angle=360, arc should draw a complete circle.
'''

from swampy.TurtleWorld import *
from math import pi
from e3 import polygon

world = TurtleWorld()
turtle = Turtle()
turtle.delay = 0.01

def arc(t, r, angle):
    arc_size = 2 * pi * r * angle / 360
    sides = 80
    length = arc_size / sides
    angle = float(angle) / sides

    for i in range(sides):
        fd(t, length)
        lt(t, angle)

arc(turtle, 80, 180)