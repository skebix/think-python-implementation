__author__ = 'skebix'

'''
In this example, ties are broken by comparing words, so words with the same length appear in reverse alphabetical order.
For other applications you might want to break ties at random. Modify this example so that words with the same length
appear in random order. Hint: see the random function in the random module.
'''

from random import random

def sort_by_length_random(words):
    t = []
    for word in words:
        t.append((len(word), random(), word))

    t.sort(reverse=True)

    res = []
    for length, random_float, word in t:
        res.append(word)
    return res

word_list = list()
fin = open('words.txt')
for line in fin:
    word_list.append(line.strip())

r = sort_by_length_random(word_list)

print r