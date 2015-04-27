__author__ = 'skebix'

'''
This exercise can be done using only the statements and other features we have learned so far.

1. Write a function that draws a grid like the following:

+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

Hint: to print more than one value on a line, you can print a comma-separated sequence: print '+', '-'
If the sequence ends with a comma, Python leaves the line unfinished, so the value printed next appears on the same line
print '+',
print '-'
The output of these statements is '+ -'.
A print statement all by itself ends the current line and goes to the next line.

2. Write a function that draws a similar grid with four rows and four columns.
'''

from e3_4 import do_twice, do_four

def print_wall():
    print '+ - - - -',

def print_post():
    print '|        ',

def print_row_two():
    do_twice(print_wall)
    print '+'

def print_posts_two():
    do_twice(print_post)
    print '|'

def print_block_two():
    print_row_two()
    do_four(print_posts_two)

def print_grid_two():
    do_twice(print_block_two)
    print_row_two()

def print_row_four():
    do_four(print_wall)
    print '+'

def print_posts_four():
    do_four(print_post)
    print '|'

def print_block_four():
    print_row_four()
    do_four(print_posts_four)

def print_grid_four():
    do_four(print_block_four)
    print_row_four()

print_grid_two()
print
print_grid_four()