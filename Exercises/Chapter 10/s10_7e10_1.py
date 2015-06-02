__author__ = 'skebix'

'''
Write a function called nested_sum that takes a nested list of integers and add up the elements from all of the nested
lists.
'''

def nested_sum(l):
    total = 0
    for i in l: total += sum(i)
    return total

print nested_sum([[1, 2, 3], [4, 5], [6, 7], [8]])