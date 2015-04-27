__author__ = 'skebix'

'''
1. Type this example into a script and test it.

2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing
the value as an argument.

3. Write a more general version of print_spam, called print_twice, that takes a string as a parameter and prints it
twice.

4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.

5. Define a new function called do_four that takes a function object and a value and calls the function four times,
passing the value as a parameter. There should be only two statements in the body of this function, not four.
'''

def print_twice(s):
    print s
    print s

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def do_twice_value(f, v):
    f(v)
    f(v)

def do_four_value(f, v):
    do_twice(f, v)
    do_twice(f, v)
