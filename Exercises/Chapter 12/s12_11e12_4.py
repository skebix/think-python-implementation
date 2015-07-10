__author__ = 'skebix'

'''
More anagrams!
1. Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of words that are
anagrams.

Here is an example of what the output might look like:
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']

Hint: you might want to build a dictionary that maps from a set of letters to a list of words that can be spelled with
those letters. The question is, how can you represent the set of letters in a way that can be used as a key?
'''

def anagrams_list():
    fin = open('words.txt', 'r')

    anagrams_dictionary = {}

    for line in fin:
        word = line.strip().lower()
        key = tuple(''.join(sorted(word)))
        anagrams_dictionary.setdefault(key, []).append(word)

    for key, value in anagrams_dictionary.iteritems():
        if len(value) > 1:
            print value

anagrams_list()