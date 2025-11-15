"""
Created by Taylor Richards
taylordrichards@gmail.com
November 09, 2025

Square numbers: 01, 04, 09, 16, 25, 36, 49, 64, 81

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

def main():
    start_time = time.perf_counter()

    pairs = [(0,1), (0,4), (0,6), (2,5), (1,6), (3,6), (4,6), (8,1)]

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
        cubes.add((frozenset(cube_L), frozenset(cube_R)))

    print(max)
    
    count = 0
    for cube in cubes:
        cube_L, cube_R = cube
        count += math.comb(10-len(cube_L), 6-len(cube_L)) * math.comb(10-len(cube_R), 6-len(cube_R))

    print(f"Total arrangements: {len(cubes)}")
    print(f"Number of distinct cube pairs: {count}")


    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()