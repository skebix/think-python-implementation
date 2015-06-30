__author__ = 'skebix'

'''
Dictionaries have a method called keys that returns the keys of the dictionary, in no particular order, as a list.
Modify print_hist to print the keys and their values in alphabetical order.
'''

from s11_1e11_2 import histogram

def print_hist(h):
    l = sorted(h.keys())
    for e in l:
        print e, h[e]

print_hist(histogram('brontosaurus'))


