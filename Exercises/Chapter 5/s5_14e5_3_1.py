__author__ = 'skebix'

'''
Write a function named check_fermat that takes four parameters -a, b, c and n- and that checks to see if Fermat's
theorem holds. If n is greater than 2 and it turns out to be true that an + bn = cn the program should print,
'Holy smokes, Fermat was wrong!' Otherwise the program should print, 'No, that doesn't work.'
'''

def check_fermat(a, b, c, n):
    """
    This function checks if Fermat's theorem holds for integers a, b and c. And n > 2.
    """
    if((pow(a, n) + pow(b, n) == pow(c, n)) and n > 2):
        print 'Holy smokes, Fermat was wrong!'
    else:
        print "No, that doesn't work."