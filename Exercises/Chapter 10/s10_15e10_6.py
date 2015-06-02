__author__ = 'skebix'

'''
Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending
order and False otherwise. You can assume (as a precondition) that the elements of the list can be compared with the
relational operators <, >, etc.

For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return False.
'''


def is_sorted(l):
    length = len(l)
    if length < 2:
        return False
    for i in range(length - 1):
        if l[i] > l[i + 1]:
            return False
    return True

print is_sorted([2, 4, 8, 32, 16, 64, 128]), is_sorted([2, 4, 8])