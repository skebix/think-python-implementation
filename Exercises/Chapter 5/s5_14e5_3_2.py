__author__ = 'skebix'

'''
Write a function that prompts the user to input values for a, b, c and n, converts them to integers, and uses
check_fermat to check whether they violate Fermat's theorem.
'''

from s5_14e5_3_1 import check_fermat

def input_check():
    print "We will try to se if some numbers a, b, c and n > 2 can violate Fermat's theorem"
    a = int(input('Enter a..\n'))
    b = int(input('Enter b..\n'))
    c = int(input('Enter c..\n'))
    n = int(input('Enter n..\n'))

    check_fermat(a, b, c, n)

input_check()