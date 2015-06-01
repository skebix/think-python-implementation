__author__ = 'skebix'

'''
Here's another Car Talk Puzzler (http://www.cartalk.com/content/puzzlers):

"I was driving on the highway the other day and I happened to notice my odometer. Like most odometers, it shows six
digits, in whole miles only. So, if my car had 300,000 miles, for example, I'd see 3-0-0-0-0-0. "Now, what I saw that
day was very interesting. I noticed that the last 4 digits were palindromic; that is, they read the same forward as
backward. For example, 5-4-4-5 is a palindrome, so my odometer could have read 3-1-5-4-4-5.

"One mile later, the last 5 numbers were palindromic. For example, it could have read 3-6-5-4-5-6. One mile after that,
the middle 4 out of 6 numbers were palindromic. And you ready for this? One mile later, all 6 were palindromic!

"The question is, what was on the odometer when I first looked?"

Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy these requirements.
'''

def is_palindrome(i, start, length):
    s = str(i)[start : start + length]
    return s[::-1] == s

def has_properties(i):
    return is_palindrome(i, 2, 4) and is_palindrome(i + 1, 1, 5) and is_palindrome(i + 2, 1, 4) and is_palindrome(i + 3, 0, 6)

def puzzler():
    for i in range(100000, 999997):
        if has_properties(i): print i

puzzler()