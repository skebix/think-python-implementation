__author__ = 'skebix'

'''
Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns None.
'''

def chop(x):
    del x[:1]
    del x[-1:]

l = [1, 2, 3, 4]

print l, chop(l), l