"""
Created by Taylor Richards
taylordrichards@gmail.com
November 16, 2025

Gonna look into sympy for the fastest way to get proper divisors.

1. start with a set of all the numbers in our search space
2. (a) get a number from the search space, then
   (b) add the number to a new cycle-set, then
   (c) sum the number's proper divisors, then
   (d) if the sum is not in the search space, discard the cycle and go to (a) 
       else, if the sum is already in the cycle-set, we have a cycle; go to (a)
       otherwise, add the sum to the current cycle-set, and repeat from (c)
"""

from sympy.ntheory.factor_ import proper_divisors
import time
from collections import defaultdict

def main():
    start_time = time.perf_counter()

    SEARCH_SIZE = 10**6

    search_space = set(range(1,SEARCH_SIZE+1))

    chains = []
    bad_nums = {0,1,2}
    while search_space:
        bad_chain = False
        n = search_space.pop()
        chain = set()
        while n not in chain:
            if n > SEARCH_SIZE:
                bad_chain = True 
                break
            elif n in bad_nums:
                bad_chain = True 
                break
            else:
                chain.add(n)
                search_space.discard(n)
                n = sum(proper_divisors(n))

        if bad_chain:
            bad_nums.update(chain)
        else:
            chains.append(chain)

    walk = {}
    real_chains = []
    for chain in chains:
        cycle_found = False
        walk = {n:[sum(proper_divisors(n)),0] for n in chain}
        starting_point = min(chain)
        walk[starting_point][1] += 1
        n = walk[starting_point][0]
        while not cycle_found:
            walk[n][1] += 1
            if walk[n][1] >= 3:
                cycle_found = True
            else:
                n = walk[n][0]
        new_chain = {k for k,v in walk.items() if v[1] >= 2}
        real_chains.append(new_chain)


    longest_chain = max(real_chains, key=len)
    print(longest_chain)
    print(min(longest_chain))

    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()