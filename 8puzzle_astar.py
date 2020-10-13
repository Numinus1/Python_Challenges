import copy
import random

#print puzzle to output
def printPuzzle(puzzle, n):
    for x in range(0, n):
        stri = ""
        for y in range(0, n):
            if puzzle[x][y] != 0:
                stri += str(puzzle[x][y])
            else:
                stri += " "
            stri += " "
        print(stri)
    print("")

#create random puzzle:
def genNPuzzle(n):
    i = n
    puzzle = []
    
    #generate N x N array:
    for x in range(0, n):
        row0 = [-1] * n
        puzzle.append(row0)

    #assign blank:
    puzzle[random.randint(0, n-1)][random.randint(0, n-1)] = 0
    
    #assign remaining values pseudo-randomly:
    lim = n * n
    for i in range(1, lim):
        ind = random.randint(0, lim - 1)
        done = False
        while done == False:
            rowin = int(ind/n)
            colin = ind%n
            if puzzle[rowin][colin] == -1:
                puzzle[rowin][colin] = i
                done = True
            else:
                ind += 1
                if ind == lim:
                    ind = 0
    
                
    return puzzle

#check goal state reached:
def checkSolution(puzzle, goal, N = 3):
    
    for x in range(0, N - 1):
        for y in range(0, N - 1):
            if puzzle[x][y] != goal[x][y]:
                return False
    
    return True

#calculate h score
def getHScore(puzzle, goal, N = 3):
    h = 0
    for x in range(0, N):
        for y in range(0, N):
            if puzzle[x][y] != goal[x][y]:
                h += 1
    return h

#generate moves (ie open list)
def genMoves(puzzle, goal, d, N = 3):
    
    blanki = [-1, -1]
    
    #find location of blank
    for x in range(0, N):
        for y in range(0, N):
            if puzzle[x][y] == 0:
                blanki = [x, y]
    
    #return adjacent nodes along with their f-score
    moveList = []
    
    
    #move left:
    if blanki[0] != 0:
        tpuzzle = copy.deepcopy(puzzle)
        tval = tpuzzle[blanki[0] - 1][blanki[1]]
        tpuzzle[blanki[0] - 1][blanki[1]] = 0
        tpuzzle[blanki[0]][blanki[1]] = tval
        moveItem = [tpuzzle, d + getHScore(tpuzzle, goal)]
        moveList.append(moveItem)
    
    #move right:
    if blanki[0] != N - 1:
        tpuzzle = copy.deepcopy(puzzle)
        tval = tpuzzle[blanki[0] + 1][blanki[1]]
        tpuzzle[blanki[0] + 1][blanki[1]] = 0
        tpuzzle[blanki[0]][blanki[1]] = tval
        moveItem = [tpuzzle, d + getHScore(tpuzzle, goal)]
        moveList.append(moveItem)
    
    #move up
    if blanki[1] != 0:
        tpuzzle = copy.deepcopy(puzzle)
        tval = tpuzzle[blanki[0]][blanki[1] - 1]
        tpuzzle[blanki[0]][blanki[1] - 1] = 0
        tpuzzle[blanki[0]][blanki[1]] = tval
        moveItem = [tpuzzle, d + getHScore(tpuzzle, goal)]
        moveList.append(moveItem)
        
    #move down
    if blanki[1] != N-1:
        tpuzzle = copy.deepcopy(puzzle)
        tval = tpuzzle[blanki[0]][blanki[1] + 1]
        tpuzzle[blanki[0]][blanki[1] + 1] = 0
        tpuzzle[blanki[0]][blanki[1]] = tval
        moveItem = [tpuzzle, d + getHScore(tpuzzle, goal)]
        moveList.append(moveItem)
        
    return moveList
        
#iteratively solve
def solve(puzzle, goal, N = 3):
    #create closed list
    current = copy.deepcopy(puzzle)
    d = 0
    moveList = []
    moveItem = [current, d + getHScore(current, goal)]
    moveList.append(moveItem)
    print("Start State:")
    printPuzzle(current, N)
    trig = False
    while (checkSolution(current, goal, N)) == False:
    #while trig == False:
        #d += 1
        tMoveList = genMoves(current, goal, d)
        #add to closed list; get lowest fscore state:
        score = 99999999999
        newState = copy.deepcopy(current)
        
        for x in range(0, len(tMoveList)):
            moveList.append(tMoveList[x])
            print("Inner Step #" + str(x + 1))
            printPuzzle(tMoveList[x][0], N)
            print(str(tMoveList[x][1]))
            if tMoveList[x][1] < score:
                score = tMoveList[x][1]
                newState = copy.deepcopy(tMoveList[x][0])
                
        current = copy.deepcopy(newState)
        print("Step #" + str(d) + ":")
        printPuzzle(current, N)
        if d > 3:
            trig = True
    
    
    print("Solution found; terminating")
    
    
"""
print ("N-Puzzle Problem using A* Algorithm")
print ("Enter a value for N: ")
N = int(input())
print("Generated Random " + str(N) + "-Puzzle:")
"""
N = 3
puzzle = genNPuzzle(N)
goal = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
print("Goal State: ")
printPuzzle(goal, N)
printPuzzle(puzzle, N)
print(getHScore(puzzle, goal))
print(puzzle)
print(goal)
solve(puzzle, goal)