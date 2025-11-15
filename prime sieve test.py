"""
Created by Taylor Richards
taylordrichards@gmail.com
October 03, 2023
"""
import time

import itertools as it
def erat2( ):
    D = {  }
    yield 2
    for q in it.islice(it.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

def main():
    start_time = time.perf_counter()

    ## main code goes here

    primes = erat2()

    # it.dropwhile(lambda x: x < 1000000, primes)

    # print(primes.__next__)

    primes = list(it.takewhile(lambda x: x < 100000000, primes))

    print(primes[-1])

    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()