__author__ = 'skebix'

'''
In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter "e." Since
"e" is the most common letter in English, that's not easy to do.

In fact, it is difficult to construct a solitary thought without using that most common symbol. It is slow going at
first, but with caution and hours of training you can gradually gain facility. All right, I'll stop now.

Write a function called has_no_e that returns True if the given word doesn't have the letter "e" in it.

Modify your program from the previous section to print only the words that have no "e" and compute the percentage of the
words in the list have no "e."
'''

def has_no_e(word):
    return True if 'e' not in word else False

print has_no_e('wololo'), has_no_e('prehistoric')

def percentage_withouth_e():
    fin = open('words.txt', 'r')
    c, q, t = 0, 0, 0
    for line in fin:
        word = line.strip()
        t += 1
        if has_no_e(word):
            print word
            c += 1
    percentage = c * 100.0 / t
    return percentage

print percentage_withouth_e()