__author__ = 'skebix'

'''
Write a function that reads the file words.txt and builds a list with one element per word. Write two versions of this
function, one using the append method and the other using the idiom t = t + [x]. Which one takes longer to run? Why?

Hint: use the time module to measure elapsed time.
'''

import time

def word_list1():
    l = []
    fin = open('words.txt')
    for line in fin:
        l.append(line.strip())
    return l


def make_word_list2():
    l = []
    fin = open('words.txt')
    for line in fin:
        l = l + [line.strip()]
    return l


start_time = time.time()
l = word_list1()
elapsed_time = time.time() - start_time

print len(l), elapsed_time, 'seconds'

start_time = time.time()
l = make_word_list2()
elapsed_time = time.time() - start_time

print len(l), elapsed_time, 'seconds'