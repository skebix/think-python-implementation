__author__ = 'skebix'

'''
Write a function named avoids that takes a word and a string of forbidden letters, and that returns True if the word
doesn't use any of the forbidden letters.

Modify your program to prompt the user to enter a string of forbidden letters and then print the number of words that
don't contain any of them.

Can you find a combination of 5 forbidden letters that excludes the smallest number of words?
'''

import string, operator

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

def avoids_modified():
    forbidden = raw_input('Enter a string of letters to be forbidden: ')
    fin = open('words.txt', 'r')
    q = 0
    for line in fin:
        word = line.strip()
        if avoids(word, forbidden): q += 1
    print q

avoids_modified()

def minimal_subset():
    d = dict.fromkeys(string.ascii_lowercase, 0) #Creates a dict with the letters of the alphabet as keys and 0 as value
    fin = open('words.txt', 'r')
    for line in fin:
        op = line.strip()
        full_letters_set = set(line.strip()) #Creates a set with the letters of the word
        for letter in full_letters_set:
            d[letter] += 1 #Increment the number of words that have the letter
    sorted_dict = sorted(d.items(), key=operator.itemgetter(1)) #Sort the dict ascending
    minimal_letters_subset = [x[0] for x in sorted_dict] #Create a list of letters according to it's number of appearances
    minimal_subset = set()
    for i in range(5):
        minimal_subset.add(minimal_letters_subset[i]) #Take the first 5 letters
    return minimal_subset

print minimal_subset()