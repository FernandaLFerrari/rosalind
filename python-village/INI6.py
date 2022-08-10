#!/usr/bin/env python3

#
# Problem 5
#
# Given: A string s of length at most 10000 letters.
#
# Return:  The number of occurrences of each word in s, where words are 
# separated by spaces. Words are case-sensitive, and the lines in the output 
# can be in any order.
#
#

# Library for get parameters

import sys
from collections import Counter

inputPath = str(sys.argv[1])

def get_occurrences_world(inputPath: str):
    
    with open(inputPath) as f:
        ocorrencias = Counter(f.read().split())
        counter = Counter(ocorrencias)
    
    for key, value in ocorrencias.items():
        print (key, value)
        
        
get_occurrences_world(inputPath)