__author__ = 'skebix'

'''
Write a function that prompts the user to input three stick lengths, converts them to integers, and uses is_triangle to
check whether sticks with the given lengths can form a triangle.
'''

from s5_14e5_4_1 import is_triangle

def check_sticks():
    print "We will try to se if some numbers a, b, c can form a triangle"
    a = int(input('Enter a..\n'))
    b = int(input('Enter b..\n'))
    c = int(input('Enter c..\n'))

    is_triangle(a, b, c)

check_sticks()