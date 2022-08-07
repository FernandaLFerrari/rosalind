#!/usr/bin/env python3


# Problem
#
# Given: A string s of length at most 200 letters and four integers a, b, c and d.
#
# Return: The slice of this string from indices a through b and c through d
#(with space in between), inclusively. In other words, we should include elements 
#s[b] and s[d] in our slice.
#
#

from collections import Counter


import sys

#str(open(str(sys.argv[1]), "r"))

inputPath = open(str(sys.argv[1]),'r')
inputStr = inputPath.read()
inputInt1 = int(sys.argv[2])
inputInt2 = int(sys.argv[3])
inputInt3= int(sys.argv[4])
inputInt4 = int(sys.argv[5])

def dictionary(inputPath: str, inputInt1: int, inputInt2: int,
               inputInt3: int, inputInt4: int):
    
        objStr1 = inputStr[inputInt1:inputInt2]
        objStr2 = inputStr[inputInt3:inputInt4]
        print(objStr1 + " " + objStr2)
        
        
dictionary(inputPath=inputPath, inputInt1=inputInt1, inputInt2=inputInt2, 
           inputInt3=inputInt3, inputInt4=inputInt4)


