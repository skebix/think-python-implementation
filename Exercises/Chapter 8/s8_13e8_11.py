__author__ = 'skebix'

'''
The following functions are all intended to check whether a string contains any lowercase letters, but at least some of
them are wrong. For each function, describe what the function actually does (assuming that the parameter is a string).
'''

#This one doesn't work, it will return in the first letter, if it's lowercase, True, if it's uppercase, False, without
#seeing the rest of the string
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

#This is even worse, it doesn't actually check for the characters in the strings, always the letter 'c', always True.
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

#This one seems right, but if the last character is uppercase, it doesn't matter if the others are all lowercase, it
#returns False
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

#This one is fine
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

#This one is bad, if any is uppercase, returns False
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
