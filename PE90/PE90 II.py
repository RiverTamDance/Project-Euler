"""
Created by Taylor Richards
taylordrichards@gmail.com
November 13, 2025
"""
import time
import itertools as it

def main():
    start_time = time.perf_counter()

    
    squares = [{0,1}, {0,4}, {0,9}, {1,6}, {2,5}, {3,6}, {4,9}, {6,4}, {8,1}]
    squares = {frozenset(sq) for sq in squares}
    digits = {0,1,2,3,4,5,6,7,8,9}

    cubes = it.combinations(digits, 6)
    updated_cubes = set()
    for cube in cubes:
        if 6 in cube:
            updated_cubes.add(frozenset(cube) | {9})
        elif 9 in cube:
            updated_cubes.add(frozenset(cube) | {6})
        else:
            updated_cubes.add(frozenset(cube))
    print(len(updated_cubes) #I forgot that I am accidentally prematurely merging cubes here when I should be counting them separately)

    cube_pairs = it.combinations_with_replacement(updated_cubes, 2)

    count = 0
    for left, right in cube_pairs:
        values = {frozenset({l,r}) for r in right for l in left if l != r}
        if squares.issubset(values):
            count += 1

    print(count)

    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()