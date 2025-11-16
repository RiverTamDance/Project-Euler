
"""
Created by Taylor Richards
taylordrichards@gmail.com
November 16, 2025
"""
import time
import math as mt
import itertools as it

def distance(x,y):
    return((x[0]-y[0])**2+(x[1]-y[1])**2)

def side_squares(triangle):
    #triangle: [(x1,y1), (x2, y2)]
    triangle.append((0,0))
    lengths = [distance(*points) for points in it.combinations(triangle,2)]

    return(sorted(lengths))    

def main():
    start_time = time.perf_counter()

    grid_size = 100
    points = it.product((x for x in range(grid_size+1)), repeat = 2)
    points = set(points)
    points.remove((0,0))

    triangles = it.combinations(points,2)
    lengths = [side_squares(list(triangle)) for triangle in triangles]

    pythagoreans = [l for l in lengths if l[0] + l[1] == l[2]]

    print(len(pythagoreans))


    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()





# test_1 = [(1,1), (0,2)]
# print(list(side_squares(test_1)))

