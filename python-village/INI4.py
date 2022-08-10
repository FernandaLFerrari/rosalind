#!/usr/bin/env python3

#
# Problem 1
# Given: Two positive integers a and b (a<b<10000).
#
# Return: The sum of all odd integers from a through b, inclusively.
#
#


# Library for get parameters
import sys

numberInt_1 = int(sys.argv[1])
numberInt_2 = int(sys.argv[2])


def sum_integers(numberInt_1: int, numberInt_2: int):
    
    soma = 0
    
    for c in range(numberInt_1, numberInt_2):
        if c % 2 == 1:
            soma = soma + c

    print(f' A soma é {soma}')


sum_integers(numberInt_1, numberInt_2)