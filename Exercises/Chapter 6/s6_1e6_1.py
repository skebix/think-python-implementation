__author__ = 'skebix'

'''
Write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y.
'''

def compare(x, y):
    """Compare x and y. If x > y, returns 1, 0 if they are equal and -1 yf x < y"""
    return 1 if x > y else (0 if x == y else -1)

print compare(8, 4)