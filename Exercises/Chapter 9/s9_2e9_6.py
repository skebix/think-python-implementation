__author__ = 'skebix'

'''
Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double
letters are ok). How many abecedarian words are there?
'''

def is_abecedarian(word):
    return word == ''.join(sorted(word))

print is_abecedarian('access')