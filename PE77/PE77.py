"""
Created by Taylor Richards
taylordrichards@gmail.com
August 03, 2024

Something tells me I will need generating functions for this one.

"""
import time
from functools import lru_cache
import math

def main():
    start_time = time.perf_counter()

    p = 4

    def primeList(n):
        # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
        """ Returns  a list of primes < n """
        sieve = [True] * n
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if sieve[i]:
                # i*i is the square of the number we are working with, duh. 
                sieve[i*i::2*i]=[False]*int(((n-i*i-1)//(2*i)+1))
        return [2] + [i for i in range(3,n,2) if sieve[i]]

    primes = primeList(10**p)

    def odd(n):
        if 1 == (n&1):
            return(True)
        else:
            return(False)
    @lru_cache
    def prime_partitions(n, m):
        # print(n,m)
        if n < 0:
            # print(f'n < 0 {n,m}')
            return(0)
        elif n == 0:
            # print(f'n == 0 {n,m} +1')
            return(1)
        elif m == 2: #need this line to prevent next_prime erroring out of bounds.
            if odd(n):
                # print(f'm==2 and n is odd {n,m}')
                return(0)
            else:
                # print(f'm==2 and n is even {n,m} +1')
                return(1)
        
        else:
            # print(f'n > m {n,m}')
            next_prime = primes[primes.index(m)-1]
            return(prime_partitions(n-m,m) + prime_partitions(n, next_prime))
        # else:
        #     print(f'weird exit {n,m}')
        #     return(0)
        
    for i in range(4,100):
        print(i, prime_partitions(i, max(filter(lambda x: x<=i, primes))))
        







    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()