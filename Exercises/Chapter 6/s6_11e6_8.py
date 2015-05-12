__author__ = 'skebix'

'''
The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder.

One way to find the GCD of two numbers is based on the observation that if r is the remainder when a is divided by b,
then gcd(a, b) = gcd(b, r). As a base case, we can use gcd(a, 0) = a.

Write a function called gcd that takes parameters a and b and returns their greatest common divisor.

Credit: The exercise is based on an example from Abelson and Sussman's Structure and Interpretation of Computer Programs
'''

def gcd(a, b):
    ''''Calculates the gcd of a and b using Euclid's algorithm'''
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print gcd(42, 56), gcd(54, 24)