# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 20:43:24 2022

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
        row1=int(input('Player 1(X) - Please enter row number:'))
        column1=int(input('Player 1(X) - Please enter column number:'))
        if theBoard[row1][column1]=="-":
            theBoard[row1][column1]="X"
            is_win("X")
        print_board()
        row2=int(input('Player 2(O) - Please enter row number:'))
        column2=int(input('Player 2(O) - Please enter column number:'))
        if theBoard[row2][column2]=="-":
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

        
            
        
        
            
    