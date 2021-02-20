# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:48:24 2019

@author: Taylor

PE76

"""
memo = {0:1}

def partitions(n):
    
    if n < 0:
       
       memo[n] = 0 
    
    if not n in memo:
		
        result = 0
        k=1
        j=-1
        innersum1 = n-1
        innersum2 = n-2
		
        while (innersum1 >= 0) or (innersum2 >=0):
			
            result += ((-1)**(k+1)*partitions(innersum1)) + ((-1)**(j+1)*partitions(innersum2))
                        
            k += 1
            j -= 1
            innersum1 = n-k*(3*k-1)/2
            innersum2 = n-j*(3*j-1)/2
			
        memo[n] = result

    return memo[n]

testbool = False
n = 1

while testbool == False:
    if (partitions(n) % 1000000) == 0:
        testbool = True
        print(n)
    else:
        n = n + 1
        
#    if n % 1000 == 0:
#        print(n)

