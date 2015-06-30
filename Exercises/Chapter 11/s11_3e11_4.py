__author__ = 'skebix'

'''
Modify reverse_lookup so that it builds and returns a list of all keys that map to v, or an empty list if there are none
'''

from s11_1e11_2 import histogram

def reverse_lookup(d, v):
    l = []
    for k in d:
        if d[k] == v:
            l.append(k)

    return l

print reverse_lookup(histogram('brontosaurus'), 2)
