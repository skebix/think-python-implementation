__author__ = 'skebix'

'''
Rewrite this function so that instead of traversing the string, it uses the three parameter version of find from the
previous section.
'''

from s8_6e8_4 import find

def count(word, letter):
    index = 0
    length = len(word)
    j = 0
    while index < length:
        i = find(word, letter, index)
        if i == -1:
            index = length
        else:
            j += 1
            index = i + 1
    return j

c = count('wololo', 'o')
print c