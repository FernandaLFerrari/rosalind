#!/usr/bin/env python3
 
#
# Problem 1
# Given: Two positive integers a and b, each less than 1000.
#
# Return: The integer corresponding to the square of the hypotenuse of the right 
#triangle whose legs have lengths a and b.
#
# 


## Library for get parameters 
import sys

numberInt_1 = int(sys.argv[1])
numberInt_2 = int(sys.argv[2])

def hypot(numberInt_1: int, numberInt_2: int):

    hypotenuse = numberInt_1**2 + numberInt_2**2
    print(f"The hypotenuse is {hypotenuse}!")
    
    
hypot(numberInt_1=numberInt_1, numberInt_2=numberInt_2)
