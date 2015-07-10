__author__ = 'skebix'

'''
Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Find
text samples from several different languages and see how letter frequency varies between languages. Compare your
results with the tables at http://en.wikipedia.org/wiki/Letter_frequencies.
'''

import random

def most_frequent(s):
    histogram = make_histogram(s)

    temporal = []
    for letter, frequency in histogram.iteritems():
        temporal.append((frequency, letter))

    temporal.sort(reverse=True)

    result = []
    for frequency, letter in temporal:
        result.append(letter)

    return result


def make_histogram(s):
    histogram = {}
    for letter in s:
        histogram[letter] = histogram.get(letter, 0) + 1
    return histogram


s = open('words.txt').read()
result = most_frequent(s)
print result
