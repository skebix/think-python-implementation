__author__ = 'skebix'

'''
In Scrabble a "bingo" is when you play all seven tiles in your rack, along with a letter on the board, to form an
eight-letter word. What set of 8 letters forms the most possible bingos? Hint: there are seven.
'''

def most_bingos():
    fin = open('words.txt', 'r')

    anagrams_dictionary = {}

    for line in fin:
        word = line.strip().lower()
        key = tuple(''.join(sorted(word)))
        if(len(key) == 8):
            anagrams_dictionary.setdefault(key, []).append(word)

    temporal = []
    for key, value in anagrams_dictionary.iteritems():
        decorated = len(value), value
        temporal.append(decorated)

    temporal.sort(reverse=True)

    print temporal[0][1]

most_bingos()