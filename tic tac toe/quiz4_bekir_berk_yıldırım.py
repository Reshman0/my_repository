# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 19:13:12 2022

@author: DARK
"""

from sys import exit
global word
global hang_count
global pword
global ggword
global point
global roundc


point=0
words_to_guess=["bent","man"]
word=list(words_to_guess[0])
hang_count=0
roundc=len(words_to_guess)
ggword=[]
for i in range(len(word)):
    ggword.append("-")
def hangman():
    global word
    global ggword
    global hang_count
    global ggword
    if hang_count==0:
        print(ggword,"\n")
        print("| - - - -\n")
        print("|        \n")
        print("|        \n")
        print("|        \n")
        print("|        \n")
        print("|        \n")
        print("|        \n")
        print("|        \n")
    elif hang_count==1:
        print(ggword,"\n")
        print("| - - - -\n")
        print("|       |\n")
        print("|        \n")
        print("|        \n")
        print("|        \n")
        print("|        \n")
        print("|        \n")
        print("|        \n")
    elif hang_count==2:
        print(ggword,"\n")
        print("| - - - -\n")
        print("|       |\n")
        print("|       |\n")
        print("|        \n")
        print("|        \n")
        print("|        \n")
        print("|        \n")
        print("|        \n")
    elif hang_count==3:
        print(ggword,"\n")
        print("| - - - -\n")
        print("|       |\n")
        print("|       |\n")
        print("|       O\n")
        print("|        \n")
        print("|        \n")
        print("|        \n")
        print("|        \n")
    elif hang_count==4:
        print(ggword,"\n")
        print("| - - - -\n")
        print("|       |\n")
        print("|       |\n")
        print("|       O\n")
        print("|       |\n")
        print("|        \n")
        print("|        \n")
        print("|        \n")
    elif hang_count==5:
        print(ggword,"\n")
        print("| - - - -\n")
        print("|       |\n")
        print("|       |\n")
        print("|       O\n")
        print("|       |\n")
        print("|       |\n")
        print("|        \n")
        print("|        \n")
    elif hang_count==6:
        print(ggword,"\n")
        print("| - - - -\n")
        print("|       |\n")
        print("|       |\n")
        print("|       O\n")
        print("|     / |\n")
        print("|       |\n")
        print("|        \n")
        print("|        \n")
    elif hang_count==7:
        print(ggword,"\n")
        print("| - - - -\n")
        print("|       |\n")
        print("|       |\n")
        print("|       O\n")
        print("|     / | \\\n")
        print("|       |\n")
        print("|        \n")
        print("|        \n")
    elif hang_count==8:
        print(ggword,"\n")
        print("| - - - -\n")
        print("|       |\n")
        print("|       |\n")
        print("|       O\n")
        print("|     / | \\\n")
        print("|       |\n")
        print("|     /  \n")
        print("|        \n")
    elif hang_count==9:
        print(ggword,"\n")
        print("| - - - -\n")
        print("|       |\n")
        print("|       |\n")
        print("|       O\n")
        print("|     / | \\\n")
        print("|       |\n")
        print("|     /   \\\n")
        print("|        \n")


def game():
    global word
    global hang_count
    global pword
    global ggword
    global point
    global roundc
    
    
    while True:
        hangman()
        if "-" not in ggword:
            point += 1
            print("You Won. Total points are ",point)
            roundc -= 1
            if roundc==0:
                exit()
            else:
                hang_count=0
                word=words_to_guess[1]
                ggword.clear()
                for i in range(len(word)):
                    ggword.append("-")
                continue
                
            
        if hang_count==9:
            point -= 1
            print("You Lost.Total points are ",point)
            roundc -= 1
            if roundc==0:
                exit()
            
        
        inp=input("please enter a character: ")
        if inp in word:
            ggword[word.index(inp)]=inp
        else:
            hang_count += 1
            print("Your guess is wrong")
        
            
game()

        
    