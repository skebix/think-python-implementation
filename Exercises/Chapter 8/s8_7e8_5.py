__author__ = 'skebix'

'''
Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as
arguments.
'''

def count(word, l):
    count = 0
    for letter in word:
        if letter == l:
            count = count + 1
    return count

print count('wololo', 'l')