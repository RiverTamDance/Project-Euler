# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:14:14 2019

@author: Taylor


Prime Number Generator

"""
from math import *
import timeit

primes = [2]

def sieve(n):

    start = timeit.default_timer()
    
    primes = [2,3,5,7]
    
    for i in range(8,n):
        
        # initialise
        failed = False
        j = 0
        
        #use mod to check divisibility
        while (failed == False) and (j<len(primes)) and (primes[j] <= i ** (1/2)):
            
            p = primes[j]
            
            if i % p == 0:
                failed = True
            else:
                j = j + 1
            
    
        #append if not divisible by all other prior primes
        if (failed == False): 
            
            primes.append(i)
            
    stop = timeit.default_timer()
    print('Time: ', stop-start)
    
    return(primes)

