__author__ = 'skebix'

'''
Type these functions into a file named palindrome.py and test them out. What happens if you call middle with a string
with two letters? One letter? What about the empty string, which is written '' and contains no letters?
'''

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]