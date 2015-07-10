__author__ = 'skebix'

'''
Many of the built-in functions use variable-length argument tuples. For example, max and min can take any number of
arguments:

>>> max(1,2,3)
3

But sum does not.
>>> sum(1,2,3)
TypeError: sum expected at most 2 arguments, got 3

Write a function called sumall that takes any number of arguments and returns their sum.
'''

def sumall(*args):
    sum = 0
    for a in args:
        sum += a
    return sum

print sumall(1, 2, 4, 8, 16, 32, 64, 128)