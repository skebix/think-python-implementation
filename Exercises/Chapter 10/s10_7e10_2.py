__author__ = 'skebix'

'''
Use capitalize_all to write a function named capitalize_nested that takes a nested list of strings and returns a new
nested list with all strings capitalized.
'''

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(nl):
    res = []
    for l in nl:
        res.append(capitalize_all(l))
    return res

print capitalize_nested([['wo', 'wol', 'wolo'], ['owl', 'wolol'], ['lol'], ['wololo'], ['lolo']])