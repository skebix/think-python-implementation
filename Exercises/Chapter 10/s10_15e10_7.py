__author__ = 'skebix'

'''
Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called is_anagram
that takes two strings and returns True if they are anagrams.
'''

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print is_anagram('wololo', 'looowl'), is_anagram('puts', 'spud')