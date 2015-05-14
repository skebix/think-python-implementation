__author__ = 'skebix'

'''
Write a function that takes a string as an argument and displays the letters backward, one per line.
'''

def backwards(s):
    l = len(s) - 1
    while l >= 0:
        print s[l]
        l = l - 1

backwards('wololo')