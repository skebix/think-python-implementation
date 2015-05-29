__author__ = 'skebix'

'''
This question is based on a Puzzler that was broadcast on the radio program Car Talk
(http://www.cartalk.com/content/puzzlers):

Give me a word with three consecutive double letters. I'll give you a couple of words that almost qualify, but don't.
For  example, the word committee, c-o-m-m-i-t-t-e-e. It would be great except for the 'i' that sneaks in there. Or
Mississippi: M-i-s-s-i-s-s-ip-p-i. If you could take out those i's it would work. But there is a word that has three
consecutive pairs of letters and to the best of my knowledge this may be the only word.

Of course there are probably 500 more but I can only think of one. What is the word? Write a program to find it.
'''

def triple_double(word):
    i, j = 0, 0
    length = len(word)

    while i < length - 1:
        if word[i] == word[i + 1]:
            j += 1
            if j == 3: return True
            i += 2
        else:
            j = 0
            i += 1
    return False

def print_triple_double():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if triple_double(word):
            print word

print_triple_double()