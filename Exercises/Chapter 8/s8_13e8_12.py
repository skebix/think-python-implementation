__author__ = 'skebix'

'''
ROT13 is a weak form of encryption that involves "rotating" each letter in a word by 13 places. To rotate a letter means
to shift it through the alphabet, wrapping around to the beginning if necessary, so 'A' shifted by 3 is 'D' and 'Z'
shifted by 1 is 'A'.

Write a function called rotate_word that takes a string and an integer as parameters, and that returns a new string that
contains the letters from the original string "rotated" by the given amount. For example, "cheer" rotated by 7 is
"jolly" and "melon" rotated by -10 is "cubed".

You might want to use the built-in functions ord, which converts a character to a numeric code, and chr, which converts
numeric codes to characters.

Potentially offensive jokes on the Internet are sometimes encoded in ROT13. If you are not easily offended, find and
decode some of them.
'''

def rotate_letter(letter, n):
    """Rotates letter n places. letter is a string of length 1 and n is the number of places"""
    start_upper = ord('A')
    start_lower = ord('a')

    if letter.islower():
        i = swap(letter, start_lower, n)
    else:
        i = swap(letter, start_upper, n)
    return chr(i)

def swap(letter, start, n):
    c = ord(letter) - start
    return (c + n) % 26 + start

def rotate_word(word, n):
    """Rotates a word n places."""
    r = ''
    for letter in word:
        r += rotate_letter(letter, n)
    return r

print rotate_word('cheer', 7)
print rotate_word('melon', -10)