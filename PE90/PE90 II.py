"""
Created by Taylor Richards
taylordrichards@gmail.com
November 13, 2025
"""
import time
import itertools as it

def main():
    start_time = time.perf_counter()

    
    squaress = [[{0,1}, {0,4}, {2,5}, {8,1}], [{0,9}, {0,6}], [{1,6}, {1,9}], [{3,6}, {3,9}], [{4,9}, {4,6}]]
    squaress =[{frozenset(sq) for sq in squares} for squares in squaress]

    cubes = it.combinations({0,1,2,3,4,5,6,7,8,9}, 6)
    cube_pairs = it.combinations_with_replacement(cubes, 2)

    count = 0
    for left, right in cube_pairs:
        values = {frozenset({l,r}) for r in right for l in left if l != r} #cartesion product of both cubes values, except when both digits are the same
        #check that the first set of squares is a subset of our values, and make sure that all the other sets have at least one value in common with our cube-values.
        if squaress[0].issubset(values) and not any([squaress[i].isdisjoint(values) for i in range(1, len(squaress))]):
            count += 1


    valuess = [{frozenset({l,r}) for r in right for l in left if l != r} for left,right in cube_pairs]
    print(sum(map(lambda x: squaress[0].issubset(x) and not any([squaress[i].isdisjoint(x) for i in range(1, len(squaress))]), valuess)))

    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()