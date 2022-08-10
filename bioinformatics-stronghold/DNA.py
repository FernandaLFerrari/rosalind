#!/usr/bin/env python3

#
# Problem
# 
# A string is simply an ordered collection of symbols selected from some alphabet 
#and formed into a word; the length of a string is the number of symbols that it
#contains.
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 
#'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
#
# Given: A DNA string s of length at most 1000 nt.
#
# Return: Four integers (separated by spaces) counting the respective number of 
#times that the symbols 'A', 'C', 'G', and 'T' occur in s.
#
#


import sys


inputPath = open(str(sys.argv[1]), 'r').read()


def count_DNA_letters(inputPath: str):
    
    nA = inputPath.count("A")
    nC = inputPath.count("C")
    nT = inputPath.count("T")
    nG = inputPath.count("G")
    
    print(nA, nC, nG, nT)
    
    
    
count_DNA_letters(inputPath=inputPath)