__author__ = 'skebix'

'''
Write a function called do_n that takes a function object and a number, n, as arguments, and that calls the given
function n times.
'''

def do_n(f, n):
    """
    Execute the function given in the parameter f, n times.
    """
    if(n > 0):
        f()
        do_n(f, n - 1)
