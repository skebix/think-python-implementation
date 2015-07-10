__author__ = 'skebix'

'''
Modify the previous program so that it prints the largest set of anagrams first, followed by the second largest set, and
so on.
'''

def anagrams_list():
    fin = open('words.txt', 'r')

    anagrams_dictionary = {}

    for line in fin:
        word = line.strip().lower()
        key = tuple(''.join(sorted(word)))
        anagrams_dictionary.setdefault(key, []).append(word)

    temporal = []
    for key, value in anagrams_dictionary.iteritems():
        decorated = len(value), value
        temporal.append(decorated)

    temporal.sort(reverse=True)

    for anagram in temporal:
        if len(anagram[1]) > 1:
            print anagram[1]

anagrams_list()