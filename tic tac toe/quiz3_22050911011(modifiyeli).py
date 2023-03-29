# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 15:39:02 2022

@author: DARK
"""


from sys import exit


global theBoard
theBoard=[["7","8","9"],
          ["4","5","6"],
          ["1","2","3"]]



def game():
    global theBoard
    while True:
        
        print_board()
        
        
        inp=int(input("Player 1(X) - Select number that what to fill "))
        if inp==7:
            row1=0
            column1=0
        if inp==8:
            row1=0
            column1=1
        if inp==9:
            row1=0
            column1=2
        if inp==4:
            row1=1
            column1=0
        if inp==5:
            row1=1
            column1=1
        if inp==6:
            row1=1
            column1=2
        if inp==1:
            row1=2
            column1=0
        if inp==2:
            row1=2
            column1=1
        if inp==3:
            row1=2
            column1=2
            
        
            
        
        if theBoard[row1][column1] in"123456789":
            theBoard[row1][column1]="X"
            is_win("X")
        print_board()
        inp=int(input("Player 2(O) - Select number that what to fill "))
        if inp==7:
            row2=0
            column2=0
        if inp==8:
            row2=0
            column2=1
        if inp==9:
            row2=0
            column2=2
        if inp==4:
            row2=1
            column2=0
        if inp==5:
            row2=1
            column2=1
        if inp==6:
            row2=1
            column2=2
        if inp==1:
            row2=2
            column2=0
        if inp==2:
            row2=2
            column2=1
        if inp==3:
            row2=2
            column2=2
        if theBoard[row2][column2] in "123456789":
            theBoard[row2][column2]="O"
            is_win("O")


def is_win(who):
    global theBoard   
    if (theBoard[0][0]==theBoard[0][1]==theBoard[0][2]==who or
       theBoard[1][0]==theBoard[1][1]==theBoard[1][2]==who or
       theBoard[2][0]==theBoard[2][1]==theBoard[2][2]==who or
       theBoard[0][0]==theBoard[1][0]==theBoard[2][0]==who or
       theBoard[0][1]==theBoard[1][1]==theBoard[2][1]==who or
       theBoard[0][2]==theBoard[1][2]==theBoard[2][2]==who or 
       theBoard[0][2]==theBoard[1][2]==theBoard[2][2]==who or
       theBoard[0][0]==theBoard[1][1]==theBoard[2][2]==who or
       theBoard[0][2]==theBoard[1][1]==theBoard[2][0]==who):
        print_board()
        print("Player",who,"wins") 
        exit()
        
    
    
def print_board():
    global theBoard
    print("(0)(1)(2)")
    print("------")
    print(theBoard[0][0]+" | "+theBoard[0][1]+" | "+theBoard[0][2]+" |(0)")
    print('--+---+---')
    print(theBoard[1][0]+" | "+theBoard[1][1]+" | "+theBoard[1][2]+" |(1)")
    print('--+---+---')
    print(theBoard[2][0]+" | "+theBoard[2][1]+" | "+theBoard[2][2]+" |(2)")
    


game()

        
            
        
        
            
    