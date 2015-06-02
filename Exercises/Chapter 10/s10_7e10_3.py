__author__ = 'skebix'

'''
Write a function that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element
is the sum of the first i + 1 elements from the original list. For example, the cumulative sum of [1, 2, 3] is [1, 3, 6]
'''

def cumulative_sum(l):
    cl = []
    if len(l) > 0: cl.append(l[0])
    for i in range(1, len(l)):
        cl.append(cl[i - 1] + l[i])
    return cl

print cumulative_sum([1, 2, 3, 4, 5, 6, 7, 8])
