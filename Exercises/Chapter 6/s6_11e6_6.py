__author__ = 'skebix'

'''
Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False
otherwise. Remember that you can use the built-in function len to check the length of a string.
'''

from palindrome import first, last, middle

def is_palindrome(s):
    """Returns True if s is palindrome, False otherwise."""
    if len(s) <= 1:
        return True
    if first(s) != last(s):
        return False
    return is_palindrome(middle(s))

print is_palindrome('redivider')
print is_palindrome('wololo')