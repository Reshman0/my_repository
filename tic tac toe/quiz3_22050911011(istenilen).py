# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:28:56 2022

@author: DARK
"""

from sys import exit



theBoard=[["0","0","0"],
          ["0","0","0"],
          ["0","0","0"]]

       


while True:
    
    print("(0)(1)(2)")
    print("------")
    print(theBoard[0][0]+" | "+theBoard[0][1]+" | "+theBoard[0][2]+" |(0)")
    print('--+---+---')
    print(theBoard[1][0]+" | "+theBoard[1][1]+" | "+theBoard[1][2]+" |(1)")
    print('--+---+---')
    print(theBoard[2][0]+" | "+theBoard[2][1]+" | "+theBoard[2][2]+" |(2)")
    row1=int(input('Player 1(X) - Please enter row number:'))
    column1=int(input('Player 1(X) - Please enter column number:'))
    if theBoard[row1][column1]=="0":
        theBoard[row1][column1]="X"
        if (theBoard[0][0]==theBoard[0][1]==theBoard[0][2]=="X" or
           theBoard[1][0]==theBoard[1][1]==theBoard[1][2]=="X" or
           theBoard[2][0]==theBoard[2][1]==theBoard[2][2]=="X" or
           theBoard[0][0]==theBoard[1][0]==theBoard[2][0]=="X" or
           theBoard[0][1]==theBoard[1][1]==theBoard[2][1]=="X" or
           theBoard[0][2]==theBoard[1][2]==theBoard[2][2]=="X" or 
           theBoard[0][2]==theBoard[1][2]==theBoard[2][2]=="X" or
           theBoard[0][0]==theBoard[1][1]==theBoard[2][2]=="X" or
           theBoard[0][2]==theBoard[1][1]==theBoard[2][0]=="X"):
            print("Player","X","wins") 
            exit()
            
    print("(0)(1)(2)")
    print("------")
    print(theBoard[0][0]+" | "+theBoard[0][1]+" | "+theBoard[0][2]+" |(0)")
    print('--+---+---')
    print(theBoard[1][0]+" | "+theBoard[1][1]+" | "+theBoard[1][2]+" |(1)")
    print('--+---+---')
    print(theBoard[2][0]+" | "+theBoard[2][1]+" | "+theBoard[2][2]+" |(2)")
    row2=int(input('Player 2(O) - Please enter row number:'))
    column2=int(input('Player 2(O) - Please enter column number:'))
    if theBoard[row2][column2]=="0":
        theBoard[row2][column2]="O"
        if (theBoard[0][0]==theBoard[0][1]==theBoard[0][2]=="O" or
           theBoard[1][0]==theBoard[1][1]==theBoard[1][2]=="O" or
           theBoard[2][0]==theBoard[2][1]==theBoard[2][2]=="O" or
           theBoard[0][0]==theBoard[1][0]==theBoard[2][0]=="O" or
           theBoard[0][1]==theBoard[1][1]==theBoard[2][1]=="O" or
           theBoard[0][2]==theBoard[1][2]==theBoard[2][2]=="O" or 
           theBoard[0][2]==theBoard[1][2]==theBoard[2][2]=="O" or
           theBoard[0][0]==theBoard[1][1]==theBoard[2][2]=="O" or
           theBoard[0][2]==theBoard[1][1]==theBoard[2][0]=="O"):
            print("Player","O","wins") 
            exit()
            



    
    

    
    


