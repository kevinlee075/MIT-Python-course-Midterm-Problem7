# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 18:06:50 2021

@author: Lenovo
"""

#Write a function called score that meets the specifications below.

def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    eng_char_num = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 
                    'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 
                        'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 
                            'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    score_word = []
    word = word.lower()
    for letter_place in range(len(word)):
        scores = letter_place * eng_char_num[word[letter_place]]
        score_word.append(scores)
    highest = max(score_word)
    while True:
        if highest in score_word:
            score_word.remove(highest)
        else:
            break
    second_highest = max(score_word)
    return f(highest, second_highest)
def f(a, b):
    return a+b
    
        