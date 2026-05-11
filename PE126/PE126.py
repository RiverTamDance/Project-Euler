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
from math import prod
 
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

#-------------------------------
dimensions = (11,1,1)
internals = starting_cubes(*dimensions)
i = 0
covering_lengths = [prod(dimensions)]
while i <= 10:
    i+=1
    covering = set()
    for cube in internals:
        covering |= get_covering(cube)
 
    covering -= internals
    internals |= covering
    covering_lengths.append(len(covering))

first_differences = []
for i, v in enumerate(covering_lengths):
    if i > 0:
        first_differences.append(v - covering_lengths[i-1])

print(first_differences)

second_differences = []
for i, v in enumerate(first_differences):
    if i > 0:
        second_differences.append(v - first_differences[i-1])

print(second_differences)