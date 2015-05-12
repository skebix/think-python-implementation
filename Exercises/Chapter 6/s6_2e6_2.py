__author__ = 'skebix'

'''
Use incremental development to write a function called hypotenuse that returns the length of the hypotenuse of a right
triangle given the lengths of the two legs as arguments. Record each stage of the development process as you go.
'''

from math import sqrt

def hypotenuse(leg1, leg2):
    """"Gets the hypotenuse of a right triangle given the lengths of the two legs"""
    #return 0.0

    #leg1_squared = leg1 ** 2
    #leg2_squared = leg2 ** 2
    #print leg1_squared, leg2_squared
    #return 0.0

    #sum_legs_squared = leg1 ** 2 + leg2 ** 2
    #print sum_legs_squared
    #return 0.0

    return sqrt(leg1 ** 2 + leg2 ** 2)

print hypotenuse(3, 4)