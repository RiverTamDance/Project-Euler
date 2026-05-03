"""
Let me see if I can write a stupid version that at least corresponds to the example given in the problem statement.
 
 
3x2x1 corresponds to dimensions along x,y,z axes.
This means we have the following six unit cubes:
(1,1,1)
(2,1,1)
(3,1,1)
(1,2,1)
(2,2,1)
(3,2,1)
 
 
It may make calculations if I give "0" a width,
 
so the cubes instead look like
(0,0,0)
(1,0,0)
(2,0,0)
(0,1,0)
(1,1,0)
(2,1,0)
 
To be fully covered, each cube needs 6 more cubes:
 
(0,0,0)->(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)
clearly,  (1,0,0) and (0,1,0) already exist, so no need to consider them
That leaves 4 new cubes that need to be added to the covering, which is exactly the result in the example.
 
"""
 
""" it looks to me like I shouldn't try to use the starting cuboid as the initial condition.
I should use the first covering to fit the equation"""
 
"""Plan: use the first and second covering values to establish b & c for 4x**2 + bx + c.
I can also check that each equation is correct for the first 10 covering values for each initial cuboid. At that point, I'm sailing along."""
 
 
from math import prod
from collections import Counter
import time
import numpy as np
import itertools as it
from numba import njit
 
 
def starting_cubes(w,l,h):
    """generate all cubes corresponding to the starting cuboid dimensions"""
    cubes = set()
    for x in range(w):
        for y in range(h):
            for z in range(l):
                cubes.add((x,y,z))
   
    return cubes
 
 
def get_covering(cube):
    x,y,z = cube
    covering = set((
        (x-1,y,z),
        (x+1,y,z),
        (x,y-1,z),
        (x,y+1,z),
        (x,y,z-1),
        (x,y,z+1),
    ))
    return covering
 
def unique_starting_cuboids():
    i=0
    while True:
        i+=1
        for j in range(1,i+1):
            for k in range(1, j+1):
                yield((i,j,k))
 
def differences(seq):
   
    return [
        v-seq[i-1]
        for i,v in enumerate(seq)
        if i > 0
    ]
   
 
def naive_covering_lengths(cube, sample_size=10):
    internals = starting_cubes(*cube)
    i = 0
    covering_lengths = []
    while i < sample_size:
        i+=1
        covering = set()
        for cube in internals:
            covering |= get_covering(cube)
    
        covering -= internals
        internals |= covering
        covering_lengths.append(len(covering))
    return(covering_lengths)
   
 
def equation_fit(cube, sample):
    #let s be the sample of covering lengths for the given cube
    s = sample
    #for x = 1, 4+a+c = s[0]
    #for x = 2, 16+2a+c = s[1]
    #therefore, 12+a=s[1]-s[0] => a = s[1]-s[0]-12
    #and c = s[0]-4-s[1]+s[0]+12 = 2s[0]-s[1]+8
    return s[1]-s[0]-12, 2*s[0]-s[1]+8
 
def coefficients(w,l,h):
    first_layer = 2*w*l+2*w*h+2*l*h
    second_layer = first_layer + 4*(w+l+h)
    s = [first_layer, second_layer]
    b,c = equation_fit((w,l,h), s)
       
    return(b,c)

#-------------------------------
 
start_time = time.time()
 
 
 
 
cube_count = 100_000
n = 10_000
coeffs_gen = (coefficients(*cube) for cube in unique_starting_cuboids())
 
coeffs = np.fromiter(coeffs_gen, dtype=np.dtype((np.int64,2)), count=cube_count)
 
print("Getting coefficients took %s seconds" % (time.time() - start_time))
time_2 = time.time()
 
b,c = coeffs[:,0:1], coeffs[:,1:2]
x = np.arange(1,n+1, dtype = np.int64)
all_values = (4*x+b)*x+c
 
print("Evaluating functions took %s seconds" % (time.time() - time_2))
time_3 = time.time()
 
unique, counts = np.unique(all_values, return_counts=True)
 
# print("Sorting results took %s seconds" % (time.time() - time_3))
# time_4 = time.time()
 
# print(max(list(zip(unique, counts)),key=lambda x: x[1]))
# print("The final scan took %s seconds" % (time.time() - time_4))
 
# print("Total time: --- %s seconds ---" % (time.time() - start_time))

