__author__ = 'skebix'

'''
Write a function called remove_duplicates that takes a list and returns a new list with only the unique elements from
the original. Hint: they don't have to be in the same order.
'''

def remove_duplicates(l):
    return list(set(l))

print remove_duplicates([2, 4, 8, 4, 2])