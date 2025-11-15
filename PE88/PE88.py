"""
Created by Taylor Richards
taylordrichards@gmail.com
May 24, 2025
"""
import time
from collections import defaultdict, Counter
import math
from sympy.ntheory import factorint
from math import prod
def main():
    start_time = time.perf_counter()

    def prime_factors(n):
        """finds all prime factors for all numbers less than n"""
        D = defaultdict(dict)
        for prime in range(2,n):
            if not D[prime]:
                s = prime
                counter = 1
                while s < n:
                    
                    if counter == prime:
                        D[s][prime] = D[s/prime][prime] + 1
                        counter = 0
                    else:
                        D[s][prime] = 1
                    s += prime #This is how many copies of 2 there are.
                    counter += 1

        return(D)

    def all_factorisations(n, prime_factors):
        """finds all (lists?) of factors for all numbers less than n"""
        
        #all factors will be a dictionary where keys are numbers, and items are lists of Counters,
        #where each Counter in the list corresponds to a factorisation of the number.
        #Ex: {12: [{2:2, 3:1}, {2:1, 6:1}, {3:1, 4:1}]}
        all_factors = defaultdict(set)

        for num in range(2,n):
            prime_factorisation = Counter(prime_factors[num])
            M = max(prime_factorisation) #Get the largest key, aka the largest factor
            prime_factorisation[M] -= 1
            root_num = prod([k**prime_factorisation[k] for k in prime_factorisation])
            if root_num == 1: #This is equivalent to num being prime
                all_factors[num].add(frozenset(Counter([num]).items())) #For prime numbers, we store a single element bag.
            else:
                for bag in all_factors[root_num]:
                    bag = Counter(dict(bag))
                    set_of_bags = set()
                    
                    #add M
                    add_bag = Counter(bag)
                    add_bag[M] += 1
                    set_of_bags.add(frozenset(add_bag.items()))

                    #multiply each unique factor in the bag by M
                    for root_factor in bag:
                        new_element = M*root_factor
                        if new_element != num:
                            mul_bag = Counter(bag)
                            mul_bag[root_factor] -= 1
                            mul_bag[new_element] += 1
                            mul_bag= +mul_bag #remove negatives or zeros
                            set_of_bags.add(frozenset(mul_bag.items()))

                    all_factors[num].update(set_of_bags)
            
                #create an unfactored bag:
                num_bag = Counter((root_num, M))      
                all_factors[num].add(frozenset(num_bag.items()))
    
        return(all_factors)

    def product_sum_sizes(n, factorisations):
        sizes = set()
        for fs in factorisations:
            fs = Counter(dict(fs))
            ones = n - sum([k*fs[k] for k in fs])
            size = fs.total() + ones
            sizes.add(size)

        return(sizes)
    

    factors = prime_factors(14_000)            
    all_factors = all_factorisations(14000, factors)

    p_s = {n:product_sum_sizes(n, all_factors[n]) for n in range(2,max(all_factors)+1)}

    optimal_product_sums = dict()
    for key, values in p_s.items():
        
        for value in values:
            if value not in optimal_product_sums:
                optimal_product_sums[value] = key
            elif optimal_product_sums[value] > key:
                optimal_product_sums[value] = key
    
    print(sum(set([optimal_product_sums[k] for k in range(2,12000+1)])))

    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()

    # The following code is underpinned by faulty assumptions.
    # optimal_prod_sums = defaultdict(int)

    # for N in range(4,32+1):
    #     factors_N = factors[N]
    #     total = 0
    #     length = 0
    #     for factor, count in factors_N.items():
    #         total += factor*count
    #         length += count
    #     ones = N - total
    #     k = ones + length
    #     if not optimal_prod_sums[k]:
    #         optimal_prod_sums[k] = N

    #         #Now we need to find all permutations of the factors...

    # print(optimal_prod_sums.items())