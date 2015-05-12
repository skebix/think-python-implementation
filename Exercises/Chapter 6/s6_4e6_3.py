__author__ = 'skebix'

'''
Write a function is_between(x, y, z) that returns True if x <= y <= z or False otherwise.
'''

def is_between(x, y, z):
    """Returns True if x <= y <= z, False otherwise"""
    return x <= y <= z

print is_between(2, 4, 8)
print is_between(2, 8, 4)