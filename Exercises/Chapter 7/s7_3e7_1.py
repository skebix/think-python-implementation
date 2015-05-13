__author__ = 'skebix'

'''
Rewrite the function print_n from Section 5.8 using iteration instead of recursion.
'''

def print_n(s, n):
    for i in range(n):
        print s

print_n('wololo', 8)