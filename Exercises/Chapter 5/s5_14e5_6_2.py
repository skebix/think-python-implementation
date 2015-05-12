__author__ = 'skebix'

'''
2. Write a function called snowflake that draws three Koch curves to make the outline of a snowflake.
'''

from swampy.TurtleWorld import *
from s5_14e5_6_1 import koch

w = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def snowflake(t, l):
    """Uses a turtle to draw a snowflake, with each side of length l"""
    for i in range(3):
        koch(t, l)
        rt(t, 120)

snowflake(bob, 150)