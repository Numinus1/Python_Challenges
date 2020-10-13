# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:49:22 2020

@author: Rajas Joshi
"""

try:
    print(int("b"))
except ValueError:
    print("error!")

def newfunction():
    lister = [1, 2 , 4, 5]
    number = 5
    letter = 'a'
    return lister, number, letter

a, b, c = newfunction()
d = list(a)
print(d)
print(a)
print(b)
print(c)

a = [-1, 123]
print(a[0])
print(a[1])
print (4 % 2)
print(5 % 2)

print("modulo trials: " )
print (int(10/4))
print(10%3)

print("comparing graphs/matrices:")
begin = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]
end0 = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]
end1 = [[1, 2, 3], [6, 5, 4], [7, 9, 8]]
print ("begin vs end0: " + str(end0 == begin))
print ("begin vs end1: " + str(end1 == begin))

print("/ vs %:")
N = 3
for x in range(0, N*N):
    print(str(x) + "/" + str(N) + " = " + str(int(x/N)))
    print(str(x) + "%" + str(N) + " = " + str(x%N))
    
def solvable(puzzle, goal):
    
    global n
    N = n
    
    #create linear array of elements
    invcount = 0
    linarr = []
    goalarr = []
    
    lim = N*N
    for i in range(0, lim):
        linarr.append(puzzle[int(i/N)][i%N])
        goalarr.append(goal[int(i/N)][i%N])

    print("Encoded Linarr:")
    print(linarr)
    
    #create positional array
    semarr = []
    for i in range(0, lim):
        x0 = -1
        y0 = -1
        for x in range(0, N):
            for y in range(0, N):
                if goal[x][y] == i:
                    x0 = x
                    y0 = y
        pos = x0
        pos *= 3
        pos += y0
        
        for j in range(0, lim):
            if linarr[j] == i:
                linarr[j] = pos

    print("Decoded Linarr:")
    print(linarr)
    print(goalarr)
    
    #parity:
    ip = -1
    ig = -1
    #find zero parity:
    zeroEvenParity = True
    
    for x in range(0, lim):
        if linarr[x] == 0:
            ip = x
        if goalarr[x] == 0:
            ig = x
    
    if ((ip - ig) % 2) == 0:
        zeroEvenParity = True
    else:
        zeroEvenParity = False
    
    print(zeroEvenParity)
    
    #find permutation parity
    
    

puzzle = [[1, 3, 5], [2, 8, 4], [0, 6, 7]]
goal = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
solvable(puzzle, goal)

"""

        print("i: " + str(i))
        print("puzzle[" + str(int(i/N)) + ", " + str(i%N) + "]: ")
        print(puzzle[int(i/N)][i%N])
        """