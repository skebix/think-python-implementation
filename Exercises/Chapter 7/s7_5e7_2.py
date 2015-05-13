__author__ = 'skebix'

'''
Encapsulate this loop in a function called square_root that takes a as a parameter, chooses a reasonable value of x, and
returns an estimate of the square root of a.
'''

def square_root(a):
    epsilon = 0.00000001
    x = float(a / 2)
    while True:
        print x
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return x

root = square_root(175)