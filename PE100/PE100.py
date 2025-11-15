"""
Created by Taylor Richards
taylordrichards@gmail.com
August 09, 2024
"""
import time
from math import isqrt

def main():
    start_time = time.perf_counter()

    [n for n in range(100000000) if (x := 1+8*(n**2+n)) == isqrt(x) **2]
    #let's see how long it takes to fill up a dictionary with squares:

    n=10

    S = set(x**2 for x in range(10**n))

    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":

    main()