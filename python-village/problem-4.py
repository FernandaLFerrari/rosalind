#!/usr/bin/env python3

#
# Problem 4
#
# Given:  A file containing at most 1000 lines.
#
# Return:  A file containing all the even-numbered lines from the original file. 
# Assume 1-based numbering of lines.
#
#

# Library for get parameters
import sys

inputPath = str(sys.argv[1])

def get_even_numbered(inputPath: str):
    
    i = 1
    f = open(inputPath, 'r')
    
    for line in f.readlines():
        if i % 2 == 0 :
            print(line)
        i += 1


get_even_numbered(inputPath)
