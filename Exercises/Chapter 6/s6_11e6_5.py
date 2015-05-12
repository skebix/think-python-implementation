__author__ = 'skebix'

'''
See http://en.wikipedia.org/wiki/Ackermann_function. Write a function named ack that evaluates Ackermann's function. Use
your function to evaluate ack(3, 4), which should be 125. What happens for larger values of m and n?
'''

def ack(m, n):
    """Evaluates Ackerman's function of given m and n, non-negative integers."""
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))

print ack(3, 4)