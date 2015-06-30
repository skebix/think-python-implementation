__author__ = 'skebix'

'''
If you did Exercise 10.8, you already have a function named has_duplicates that takes a list as a parameter and returns
True if there is any object that appears more than once in the list.

Use a dictionary to write a faster, simpler version of has_duplicates.
'''

from s11_1e11_2 import histogram

def has_duplicates(l):
    h = histogram(l)
    for k in h:
        if h[k] > 1:
            return True
    return False

print has_duplicates([1, 2, 3])