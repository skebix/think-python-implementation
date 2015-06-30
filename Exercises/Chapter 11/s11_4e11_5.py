__author__ = 'skebix'

'''
Read the documentation of the dictionary method setdefault and use it to write a more concise version of invert_dict.
'''

from s11_1e11_2 import histogram

def invert_dict(d):
    inverse = dict()
    for k in d:
        inverse.setdefault(d[k], []).append(k)
    return inverse


hist = histogram('parrot')
print hist
inverse = invert_dict(hist)
print inverse