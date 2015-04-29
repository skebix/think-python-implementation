__author__ = 'skebix'

'''
Write a function called square that takes a parameter named t, which is a turtle. It should use the turtle to draw a
square.
Write a function call that passes bob as an argument to square, and then run the program again.
'''

from swampy.TurtleWorld import *

w = TurtleWorld()
bob = Turtle()

def square(t):
    for i in range(4):
        fd(t, 100)
        lt(t)

square(bob)