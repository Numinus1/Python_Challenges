# -*- coding: utf-8 -*-
"""
Created on Sat 2 May 12:39:42 2020

@author: Rajas Joshi
"""
import copy
import random

clet = ' '

def printBoard(board):
    #print board as a grid
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |\n')

def selectFirstPlayer():
    #choose whether X or O goes first
    #define vars
    ine = ' '
    trigger = False
    global clet
    
    #loop til valid input
    while trigger == False:
        print ("Should X (Player) or O (AI) go first?")
        ine = input().upper()
        if ine == 'X' or ine == 'O':
            clet = ine 
            trigger = True
        else:
            trigger = False
    

#get player move
def inputMove(board):
    #get the next move to be played:
    num = -1
    global clet
    while num == -1:
        
        print("Enter next move (#1 to #9): ")
        num = int(input())
        if num < 1:
            num = -1
            print("invalid input; try again")
        if num > 9:
            num = -1
            print("invalid input; try again")
        if board[num] != ' ':
            num = -1
            print("That slot is already occupied; try again")
        else:
            board[num] = 'X'
            

#check if the board is in final state
def checkWin(board):
    
    if board[1] == board[2] and board[2] == board[3]:
        if board[1] == ' ':
            return ' '
        else:
            return board[1]
        
    if board[4] == board[5] and board[5] == board[6]:
        if board[4] == ' ':
            return ' '
        else:
            return board[4]
        
    if board[7] == board[8] and board[8] == board[9]:
        if board[7] == ' ':
            return ' '
        else:
            return board[7]
        
    if board[1] == board[4] and board[4] == board[7]:
        if board[1] == ' ':
            return ' '
        else:
            return board[1]
        
    if board[2] == board[5] and board[5] == board[8]:
        if board[2] == ' ':
            return ' '
        else:
            return board[2]
        
    if board[3] == board[6] and board[6] == board[9]:
        if board[3] == ' ':
            return ' '
        else:
            return board[3]
        
    if board[1] == board[5] and board[5] == board[9]:
        if board[1] == ' ':
            return ' '
        else:
            return board[1]
        
    if board[3] == board[5] and board[5] == board[7]:
        if board[3] == ' ':
            return ' '
        else:
            return board[3]
    else:
        return ' '

def checkDraw(board):
    for x in range(1, 10):
        if board[x] == ' ':
            return False
    
    return True


def checkPlayer(board):
    flipper = 0
    global clet
    for x in range(1, 10):
        if board[x] != ' ':
            flipper += 1
            
    if (flipper % 2) == 0:
        return clet
    else:
        if clet == 'X':
            return 'O'
        else:
            return 'X'

def findOptimalMove(board):
    
    depth = 0
    for x in range(1, 10):
        if board[x] == ' ':
            depth += 1
            
    if depth == 9:
        board[random.randint(1, 9)] = 'O'
    else:
        pos = minimax(board, depth)
        board[pos[0]] = 'O'
    
               
def gameOver(board):
    return (checkDraw(board)) or (checkWin(board)) != ' '

def heuristic_checkBoard(board):
    
    if (checkWin(board)) == 'X':
        return -1
    elif (checkWin(board)) == 'O':
        return 1
    else:
        return 0    
    
def minimax(board, depth):
    
    letter = checkPlayer(board)
    newBoard = copy.deepcopy(board)
    
    if letter == 'X':
        best = [-1, 999999]
    else:
        best = [-1, -999999]
    
    if depth == 0 or checkWin(newBoard) != ' ':
        value = heuristic_checkBoard(newBoard)
        return [-1, value]
        
    
    
    for x in range(1, 10):
        if newBoard[x] == ' ':
            newBoard[x] = letter
            score = [0, 0]
            tscore = minimax(newBoard, depth - 1)
            score[0] = x
            score[1] += tscore[1]
            newBoard[x] = ' '
            if letter == 'X':
                if score[1] < best[1]:
                    best = score
            else:
                if score[1] > best[1]:
                    best = score
            
                    
    return best

print("Tic Tac Toe")
boarder = [' '] * 10
printBoard(boarder)
selectFirstPlayer()
trig = False

while trig == False:
   letter = checkPlayer(boarder)
   if (checkPlayer(boarder) == 'X'):
       inputMove(boarder)
   else:
       findOptimalMove(boarder)

       
   printBoard(boarder)
   
   chkw = checkWin(boarder)
   
   if chkw != ' ':
       print("Game Over: " + chkw + " wins!")
       trig = False
       break
   
   if checkDraw(boarder):
        print("Draw!")
        trig = False
        break
        