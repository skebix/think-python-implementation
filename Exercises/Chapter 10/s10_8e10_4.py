__author__ = 'skebix'

'''
Write a function called middle that takes a list and returns a new list that contains all but the first and last
elements. So middle([1,2,3,4]) should return [2,3].
'''

def middle(l):
    if len(l) <= 2: return []
    del l[0]
    del l[len(l) - 1]
    return l

print middle([1, 2, 3, 4, 5])