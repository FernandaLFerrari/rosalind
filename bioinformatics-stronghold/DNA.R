#!/usr/bin/env Rscript
# Rscript --vanilla problem-1.R "ATCTTTTCC"
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

library(tidyverse)
args = commandArgs(trailingOnly=TRUE)



stringDNA = args[1]


count_DNA_letters = function(stringDNA) {

    nA = str_count(stringDNA, "A")
    nC = str_count(stringDNA, "C")
    nT = str_count(stringDNA, "T")
    nG = str_count(stringDNA, "G")
    
    print(c(nA, nC, nG, nT))
    
}

   
count_DNA_letters(stringDNA)
