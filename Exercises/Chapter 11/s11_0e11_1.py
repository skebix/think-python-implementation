__author__ = 'skebix'

'''
Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesn't matter what the
values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

If you did Exercise 10.11, you can compare the speed of this implementation with the list in operator and the bisection
search.
'''

c = 0

def word_list():
    word_list = dict()
    fin = open('words.txt')
    for line in fin:
        word_list[line.strip()] = 0
    return word_list

d = word_list()

a = 'wololo' in d
b = 'owl' in d

print a, b