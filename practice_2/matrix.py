#!/usr/bin/python

import sys
from pyfiglet import figlet_format

N = 8

def genMatrix(digit):
    if(digit.isdigit() and int(digit) >= 0 and int(digit) <= 9):
        Matrix = [[0 for x in xrange(N)] for x in xrange(N)] 
        arr = figlet_format(str(digit), font='clr8x8')
        new_arr = arr.split('\n')
       
        for i in xrange(N):
            for j in xrange(N):
                Matrix[i][j] = '*' if new_arr[i][j] == '#' else ' '
        return Matrix
    else:
        print "Not a number"
        return ""


def printMatrix(matrix):
    for i in xrange(N):
        for j in xrange(N):
            sys.stdout.write(str(matrix[i][j]))
        print     

#test Matrix
Matrix = []
for i in xrange(10):
    Matrix.append(genMatrix(str(i)))

for item in Matrix:
    printMatrix(item)

