"""
Created by Taylor Richards
taylordrichards@gmail.com
June 14, 2024


I think that for this problem I will do what I was planning on doing for uhh PE72. So that means gcd,
and build a dictionary of all coprimes less than the key value. lets go. also, I will probably add some multithreading,
just for funsies.

"""
import time
from math import gcd
import multiprocessing
# from collections import ChainMap
# from itertools import chain

def coprime(n,d):
    if gcd(n,d) == 1:
        return(True)
    else:
        return(False)
    
def reduced_fractions(d):

    return({n/d for n in range(1,d+1) if coprime(n,d)})

def main():
    start_time = time.perf_counter()
    
    target = 12000

    pool = multiprocessing.Pool()
    result = pool.map(reduced_fractions, range(2,target+1))

    total = 0
    for s in result:
        for e in s:
            if e > 1/3 and e < 1/2:
                total += 1

    print(total)

    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()