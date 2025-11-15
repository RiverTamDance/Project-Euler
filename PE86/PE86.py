"""
Created by Taylor Richards
taylordrichards@gmail.com
February 16, 2025

The solution I sketched out to the example problem involved finding the roots of a 5th degree polynomial. Which I don't think is tenable, especially because I think it was actually an 8th degree polynomial where the higher-order terms cancelled. That was the straight-forward approach, which I think is always worth trying for these problems, but almost always the question is constructed such that I need to find an alternative solution, like bottom up, or looking at the problem from another perspective.

Integer dimensions seems key to this problem, of course. 

I have returned a couple of days later and I think I have found a solution approach.

For each cuboid, we have to check three possibilities:

- w**2 + (h+l)**2
- h**2 + (w+l)**2
- l**2 + (h+w)**2

"""
import time
from math import sqrt
import itertools as it
from multiprocessing import Pool
import os

def integer_route(triple):
    i,j,k = triple

    distance_1 = sqrt(i**2 + (j+k)**2)
    distance_2 = sqrt(j**2 + (i+k)**2)
    distance_3 = sqrt(k**2 + (i+j)**2)

    distance = min(distance_1, distance_2, distance_3)

    if int(distance) == distance:
        result = 1
    else:
        result = 0
    
    return(result)

def main():
    start_time = time.perf_counter()

    routes = 0
    triples = it.combinations_with_replacement(range(1, 2000), 3)
    p = Pool(os.cpu_count())

    routes = p.map(integer_route,triples)

    print(sum(routes))

    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()