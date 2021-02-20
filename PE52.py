# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:24:49 2019

@author: Taylor
"""

"""
 
                                    PE 52

"""


#it appears that to solve this problem, we may subtract these primes
#from one another, and check if this difference is an integer multiple
#of some common difference.

#the primes will be of the same length. so it appears we may generate all 
#primes of length 6, 7, 8, etc, and begin differencing. Once we have the list
# of differences, we sort the list into integer multiples.

#quick check: how many combinations are there, that is how many differencing
#operations will we have to perform on this list. its C(n,2), correct?
#answer: many combinations. damn. that sucks. guess I gotta figure out a new 
#method? well let's see if we can get my basic idea to work for the examples
#given in the question, then maybe I can optimize

#I also would like to learn how to call functions from other files, etc.


from PrimeNumberGenerator import sieve

primes = [p for p in sieve(100) if p > 9]

def differencing(liszt):
    
    output = []
    
    for i in range(len(liszt)):        
        for j in range(i+1,len(liszt)):
            
            diff = (-1)*(liszt[i]-liszt[j])
            
            output.append(diff)
        
    return(output)
    
    
        


























