__author__ = 'skebix'

'''
Starting with this diagram, execute the program on paper, changing the values of i and j during each iteration. Find and
fix the second error in this function.
'''

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) - 1

    while j >= 0:
        #print i, j
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    return True

b = is_reverse('stop', 'pots')
print b