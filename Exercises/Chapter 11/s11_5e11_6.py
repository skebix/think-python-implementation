__author__ = 'skebix'

'''
Run this version of fibonacci and the original with a range of parameters and compare their run times.
'''

import time

known = {0:0, 1:1}

def fibonacci_memo(n):
    if n in known:
        return known[n]

    res = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    known[n] = res
    return res

def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

start_time = time.time()
r = fibonacci(21)
elapsed_time = time.time() - start_time

print 'Fibonacci of 21 calculated with fibonacci in ' + str(elapsed_time) + ' seconds. Result: ' + str(r)

start_time = time.time()
r = fibonacci_memo(999)
elapsed_time = time.time() - start_time

print 'Fibonacci of 999 calculated with fibonacci_memo in ' + str(elapsed_time) + ' seconds. Result: ' + str(r)

print known