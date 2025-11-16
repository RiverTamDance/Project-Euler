#PE90

"""
0 & 1,4,9
2 & 5
3 & 6
4 & 9
6 & 4
8 & 1

So long as I anchor things by having the left cube be the "2" cube and having the right cube be the "5" cube, we should be god to go. I can assign everything else any which way and all the cubes arrangements will be distinct.

Which means I really only have to solve a sub problem. can i use this reasoning again?
Because the rest of the numbers have a potential to "chain-together", I don't think I can cleanly use the same 2,5 logic. Or else I have to think harder.

Let's see...


"""

"""
Created by Taylor Richards
taylordrichards@gmail.com
November 09, 2025

Square numbers: 01, 04, 09, 16, 25, 36, 49, 64, 81

{0,6,5,4,8}
{1,4,2,3}

What's the best way to approach this? Like I could start cooking up rules for each digit.
- 0 must be in one, and then the other must have 1, 4, and {6,9}
- In general, we get the "opposite combos"
- 0 & 1,4,6
- 1 & 6
- 2 & 5
- 3 & 6
- 4 & 9, same as 4 & 6
- 6 & 4, same as 4 & 9
- 8 & 1

"""
import time
import math
import itertools as it

def nine_cubes(cube_pair):
    cube_L, cube_R = cube_pair
    
    new_pairs = set()
    if 6 in cube_L:
        cube_L_new = {x for x in cube_L if x != 6}
        cube_L_new.add(9) 
        new_pairs.add((frozenset(cube_L_new), frozenset(cube_R)))
    
    if 6 in cube_R:
        cube_R_new = {x for x in cube_R if x != 6}
        cube_R_new.add(9) 
        new_pairs.add((frozenset(cube_L), frozenset(cube_R_new)))
        
    if 6 in cube_L and 6 in cube_R:
        cube_L_new = {x for x in cube_L if x != 6}
        cube_L_new.add(9)        
        cube_R_new = {x for x in cube_R if x != 6}
        cube_R_new.add(9) 
        new_pairs.add((frozenset(cube_L_new), frozenset(cube_R_new)))
    
    return(new_pairs)
    
def filled_in_cubes(cube_pair):
    cube_L, cube_R = cube_pair
    digits = set(range(10))
    
    new_pairs = set()
    
    empty_L_slots = 6 - len(cube_L)
    potential_left_numbers = digits.difference(cube_L)
    left_combinations = it.combinations(potential_left_numbers, empty_L_slots)
    left_cubes = {cube_L.union(lc) for lc in left_combinations}
        
    empty_R_slots = 6 - len(cube_R)
    potential_right_numbers = digits.difference(cube_R)
    right_combinations = it.combinations(potential_right_numbers, empty_R_slots)
    right_cubes = {cube_R.union(rc) for rc in right_combinations}
    
    for L in left_cubes:
        for R in right_cubes:
            new_pairs.add((frozenset(L), frozenset(R)))
    
    return(new_pairs)
    
    

def main():
    start_time = time.perf_counter()

    pairs = [(0,1), (0,4), (0,6), (1,6), (2,5), (3,6), (4,6), (8,1)]

    selectors = [format(x, '0'+str(len(pairs)) +'b') for x in range(2**len(pairs))]

    cubes = set()
    for selector in selectors:
        cube_L = set()
        cube_R = set()
        for i, b in enumerate(selector):
            if b == '0':
                cube_L.add(pairs[i][0])
                cube_R.add(pairs[i][1])
            else:
                cube_L.add(pairs[i][1])
                cube_R.add(pairs[i][0])
        if len(cube_L) <= 6 and len(cube_R) <= 6:
            cubes.add((frozenset(cube_L), frozenset(cube_R)))
            
    #Here we deal with the issue of '9'.
    #testcases
    # print(nine_cubes((frozenset({0, 1, 3, 4, 5}), frozenset({0, 1, 2, 6, 8}))))
    # print(nine_cubes((frozenset({1, 3, 4, 5, 6}), frozenset({0, 2, 4, 6, 8}))))
    
    new_pairs = set()
    for cube in cubes:
        new_pairs = new_pairs.union(nine_cubes(cube))
    
    cubes = cubes.union(new_pairs)
        

    print(f"Total arrangements: {len(cubes)}")

    #fill in the empty space in each cube.
    pairs = set()
    for cube in cubes:
        pairs = pairs.union(filled_in_cubes(cube))

    
    
    #Check all the cubes for sizes and duplicates
    print(max([len(cube) for pair in pairs for cube in pair]))
    print(min([len(cube) for pair in pairs for cube in pair]))
    
    #check that all entries have exactly 2 elements
    pair_lengths = [len(pair) for pair in pairs]
    print(max(pair_lengths))
    print(min(pair_lengths))
    
    #check for pairs with identical entries
    #first convert everthing to sorted tuples
    pairs = {tuple(sorted((tuple(sorted(pair[0])), tuple(sorted(pair[1]))))) for pair in pairs}
    
    print(f"Number of distinct cube pairs: {len(pairs)}")

    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()