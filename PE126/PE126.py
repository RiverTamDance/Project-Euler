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
 
internals = starting_cubes(5,1,1)
i = 0
while i <= 1000:
    i+=1
    covering = set()
    for cube in internals:
        covering |= get_covering(cube)
 
    covering -= internals
    internals |= covering
    print(len(covering))   

