# -*- coding: utf-8 -*-
"""
Created on Fri May  1 13:43:23 2020

@author: Rajas Joshi
"""

import random
import time

#Display the Board:
def printBoard(board):
    
    boardstr = []
    for x in range(len(board)):
        tstr = ""
        for y in range(len(board)):
            
            if board[y] == x:
                tstr += " Q "
            else:
                tstr += " X "
        boardstr.append(tstr)
        print(tstr)


def printBoardDetails(board):

    print(board)
    printBoard(board)   
    print("Clashes: " + str(checkClashes(board)) + "\n")
    
#Count the number of queen-pairs that can attack each other 

def checkClashes(board):
    
    clashes = 0
    
    #iterate over all the columns and rows:
    for x in range(len(board)):
        for y in range(x + 1, len(board)):
            
            #check rows:
            if board[x] == board[y]:
                clashes += 1
                
            #check diagonals:
            d = y - x
            if board[x] == board[y] + d:
                clashes += 1
            elif board[x] == board[y] - d:
                clashes += 1
    
    return clashes    

#find a single vertical movement of a Queen gives the maximum reduction in clashes:
#ignore count skips solutions that lead to dead-ends
def getSteepestMove(board):
    #save current clashes
    currClashes = checkClashes(board)
    #generate variable to hold clash count and new board after each single move
    bestClashes = currClashes
    bestBoard = list(board)  
    
    #iterate over each column:
    for x in range(len(board)):
        #iterate over moving the queen in that column over each row:
        for y in range(len(board)):
            if y != board[x]:
                tboard = list(board)
                tboard[x] = y
                tclashes = checkClashes(tboard)
                #check if this is the most clash-reducing move to date
                #if it is, save it:
                if tclashes < bestClashes:
                    bestBoard = list(tboard)
                    bestClashes = tclashes
                        
        #return true to indicate the algorithm should backtrack and continue looking
        return bestBoard

#if a local maxima is hit (ie a single step cannot reduce the clashes further and the
#number of clashes isnt 0):
def shuffleBoard(board):
    
    for x in range(20):
        board[random.randint(0, len(board) - 1)] = random.randint(0, len(board) - 1)
        
    return board
    
#main
#print intro and get user input for n:
print("N-Queens Problem - Solution using Steep Hill-Climbing Algorithm")
print("Enter a value for N:")
N = int(input())

#get user input for for initial state:
print("Enter 'C' to input the initial state or 'R' to randomly generate one")

choice = input().upper()

#generate board, take input:
#board index implies column, value at that index indicates row of Queen in that column
board = []
if choice == 'C':
    print("Note: uses a 0 offset (ie. 0 implies first row)")
    for x in range(N):
        print("Enter the row in which Column " + str(x) + " Queen is located:")
        qpos = int(input())
        board.append(qpos)
    
else:
    for x in range(N):
        board.append(random.randint(0, N - 1))
    

#copy board to preserve initial state:
board0 = list(board)

#print board description:
print("Reminder: uses a 0 offset (ie. 0 implies first row)\n")

#print initial state:
print("###Initial State###")
printBoardDetails(board0)

"""
tempBoard = getSteepestMove(board)
print("Steep Step " + str(stepCount) + ":")
print(tempBoard)
printBoard(tempBoard)
ccount = checkClashes(tempBoard)
print("Clashes: " + str(ccount))

"""
#perform steep steps until the problem is solved OR 10000 steps have been executed:
#loop vars:
print("Beginning Steep Hill-Climbing Algorithm")
trigger = False
shuffleCount = 0
stepCount = 0
shuffleLimit = len(board) * 1000
#loop:
#initial time:
time0 = time.time()
bestSolution = list(board)
bestClashes = checkClashes(board)
temp0 = list(board)

while trigger == False:
    stepCount += 1
    temp1 = list(temp0)
    temp0 = list(getSteepestMove(temp0))
    
    #if the step does not change the state, shuffle:
    if temp1 == temp0:
        temp0 = list(shuffleBoard(temp0))
        shuffleCount += 1
        continue
    
    
    ccount = checkClashes(temp0)
    #save if this state is the best state so far:
    if ccount < bestClashes:
        bestClashes = ccount
        bestSolution = list(temp0)
        
    #if no clashes, exit:
    if ccount == 0:
        time1 = time.time() - time0
        print("Solution Found:")
        printBoardDetails(bestSolution)
        print("Expended Time: " + str(time1) + " seconds")
        print("Number of Shuffles: " + str(shuffleCount))
        print("Number of Steps: " + str(stepCount))
        trigger = True
        continue
    
    #shuffle limit (5000 times) hit:
#    elif trigger == True: 
    elif ccount != 0 and shuffleCount > shuffleLimit:
        time1 = time.time() - time0
        print("No solution found after " + str(shuffleCount) + " shuffles")
        print("Best Solution Found:")
        printBoardDetails(bestSolution)
        print("Expended Time: " + str(time1) + " seconds")
        print("Number of Shuffles: " + str(shuffleCount))
        print("Number of Steps: " + str(stepCount))
        trigger = True
        continue