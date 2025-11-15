"""
Created by Taylor Richards
taylordrichards@gmail.com
July 14, 2024

------------------------------

Project Euler 75:

Singular Integer Right Triangles

Given that L is the length of the wire, for how many values of L <= 1,500,000 can exactly 
one integer sided right angle triangle be formed?

------------------------------

My immediate feeling is that this must have to do with diophantine equations, just like any whole 
numbered solution to pythagoras' equation



"""
import time
from math import gcd
import itertools as it
from collections import defaultdict

def main():
    start_time = time.perf_counter()

    # def doubles(n):
    #     """generator for all doubles (a,b) such that
    #     b <= a and 2a+b+1 <= n"""
    #     for a in range(1, (n-2//2)):
    #         for b in range(1,a+1):
    #             yield (a,b)

    # d = doubles(10)

    # def pythagorean_triples(n):
    #     """returns """

    # doubles = ((a,b) for a in range(1,(n-2//2)) for b in range(1,min(n-a, a+1)))
    # triples = ((a,b) for (a,b) in doubles if (c2 := a**2+b**2) == isqrt(c2)**2)
    # for triple in triples:
    #     pass
    #     # print(triple)

    L = 1500000

    def euclids_formula(m,n):
        s_m = m**2
        s_n = n**2

        a = s_m-s_n
        b = 2*m*n
        c = s_m+s_n

        return(a,b,c)
    
    def odd(n):
        if 1 == (n&1):
            return(True)
        else:
            return(False)

    doubles = ((m,n) for m in it.count(2) for n in range(1,m) if gcd(m,n) == 1 and odd(m) != odd(n))

    def f(x):
        m,n = x
        t1 = (sum(euclids_formula(m,n)) <= L)
        t2 = (n >= 2)
        return(any((t1,t2)))
        
    valid_doubles = it.takewhile(f,doubles)

    D = defaultdict(set)
    for double in valid_doubles:
        a,b,c = euclids_formula(*double)
        triples = it.takewhile(lambda x: x[0] <= L, ((sum((k*a, k*b, k*c)), (k*a, k*b, k*c)) for k in it.count(1)))
        for triple in triples:
            D[triple[0]].add(triple[1])

    result = 0
    for s in D.values():
        if len(s) == 1:
            result += 1

    print(result)

    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()