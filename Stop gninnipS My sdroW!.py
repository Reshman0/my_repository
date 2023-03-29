# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 11:47:37 2022

@author: Bekir Berk YILDIRIM
"""

def spin_words(sentence):
    # Your code goes here
    splited_sentence=sentence.split(' ')
    new_sentence=''
    for a in splited_sentence:
        if len(a)>=5:
            a=a[::-1]
            new_sentence=new_sentence+a+' '
        else:
            new_sentence=new_sentence+a+' '
    new_sentence=new_sentence.rstrip()
        
        
    return new_sentence
print(spin_words("This sentence is a sentence"))



def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])