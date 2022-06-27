#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Eliezer Romero
# @Date:   2022/6/23 17:49
# output:_ 22 function calls in 0.000 seconds
from dataclasses import replace
import string
'''
Given an input text, code a program (in python) that will
that displays the number of repetitions of each word.
'''

def repeatWord(words):
    #build a new dict
    get_dict= dict()
    #split all word from our phrase. 
    #we remove possible extra spaces
    strip_word = words.strip()
    #we convert text to lower case to avoid complications
    lower_word = strip_word.lower()
    # remove Character from String
    replace_w = lower_word.translate(str.maketrans('', '', string.punctuation))
    #separte word 
    split_word = replace_w.split()
    
    for i in split_word:
        ''' 
            So here we use the dictionary declared before as get_dict 
            and we start interacting with each word[i] and 
            with the get method we say that each word consindence 
            starts from 0 if it conside a word is worth 1 and if there 
            is another word equal it will do a sum of 1.
        '''
        get_dict[i] = get_dict.get(i, 0) + 1

    return get_dict
    
phrase = "Hi how are things? How are you? Are you a developer? I am also a developer"

print(repeatWord(phrase))