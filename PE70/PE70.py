# """
# PE 70
# Created by Taylor Richards
# taylordrichards@gmail.com
# February 12, 2023
# """

# import time
# import sys
# import itertools as it

# useful_functions_path = ("C:\\Users\\Taylo\\OneDrive\\Documents"
#     "\\Project Euler\\Useful Functions\\")

# sys.path.insert(1, useful_functions_path)
# import prime as p

# def main():
#     start_time = time.perf_counter()

#     ## main code goes here

#     # test1 = it.takewhile(lambda x : x<100, p.erat2()))

#     # print(test1)



#     end_time = time.perf_counter()
#     print("--- %s seconds ---" % (end_time - start_time))

# if __name__ == "__main__":
#     main()

"""
Created by Taylor Richards
taylordrichards@gmail.com
July 25, 2023

#--------------------------

(1) My assumption is that primes minimize n/tot(n), because tot(p) = p-1, p prime. 
so I need to start looking at the largest primes and work my way back down.

#This probably won't work, as p-1 and p are too close together to produce anagramic effects.
#I will give it a try, but my hope is low.

#well, (1) didn't work so lets try something new. say n = p1*p1. then tot(n) = (p1-1)*(p2-1)
(2) So I think I need to check all numbers with two prime factors, then numbers with three prime factors, and so on. and the first result should be the smallest, I think.

(3) Okay, (2) didn't work either. New idea: find all prime factors of all numbers less than 1 million. 
Then I will basically have the totients for free. then I can get all anagrams really quickly.
And take the smallest n/tot from the lot.



"""

#----------imports----------
import time
import sys
import itertools as it
import functools as ft
from collections import Counter
from math import prod
from operator import itemgetter

# useful_functions_path = ("C:\\Users\\Taylo\\OneDrive\\Documents"
#     "\\Project Euler\\Project-Euler\\Useful Functions\\")

# sys.path.insert(1, useful_functions_path)
# import prime as p

#---------definitions-------------
from collections import defaultdict
def prime_factors(n):
    """finds all prime factors for all numbers less than n"""
    D = defaultdict(set)
    for i in range(2,n):
        if not D[i]:
            s = i
            while s < n:
                D[s].add(i)
                s += i 
    return(D)

def anagram(x1, x2):

    s1, s2 = sorted(str(x1)), sorted(str(x2))
    return(s1 == s2)

def totient(n, unique_primes):
    term1 = n/prod(unique_primes)
    term2 = prod(map(lambda x: x-1, unique_primes))
    return(int(term1 * term2))


def main():
    start_time = time.perf_counter()

    ## main code goes here

    ub=10**7

    p_f = prime_factors(ub)

    tot = {k: totient(k, v) for k, v in p_f.items()}

    anas = dict()
    for n, tot_n in tot.items():
        if anagram(n, tot_n):
            anas[n] = n/tot_n

    best = [0, float('inf')]
    for n, ratio in anas.items():
        if ratio < best[1]:
            best = [n, ratio]

    print(best)

    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()
