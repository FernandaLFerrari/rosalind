#!/usr/bin/env Rscript
# Rscript --vanilla problem-1.R 10 25

#
# Problem 1
# Given: Two positive integers a and b, each less than 1000.
#
# Return: The integer corresponding to the square of the hypotenuse of the right 
#triangle whose legs have lengths a and b.
#
# 



args = commandArgs(trailingOnly=TRUE)



numberInt_1 = as.numeric(args[1])
numberInt_2 = as.numeric(args[2])

hypot = function(numberInt_1, numberInt_2) {

    hypotenuse = numberInt_1**2 + numberInt_2**2
    print(paste0("The hypotenuse is ", hypotenuse, "!"))
    
}

   
hypot(numberInt_1, numberInt_2)
