#!/usr/bin/env Rscript
# Rscript --vanilla problem-3.R 10 25
#
# Problem 1
# Given: Two positive integers a and b (a<b<10000).
#
# Return: The sum of all odd integers from a through b, inclusively.
#
#


args = commandArgs(trailingOnly=TRUE)


numberInt_1 = as.numeric(args[1])
numberInt_2 = as.numeric(args[2])


sum_integers = function(numberInt_1, numberInt_2){
    
    soma = 0
    count = numberInt_1

    while(count <= numberInt_2){
        if(count %% 2 == 1){
            soma = soma + count
        } 
      count = count+1         
    } 

    print(paste0(' A soma é ', soma, "."))

}
    
    


sum_integers(numberInt_1,numberInt_2)