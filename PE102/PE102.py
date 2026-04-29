# Triangle containment
""" Calculate the area of the three triangles formed by the origin and the three given points. if that area is equal to the area of the original triangle, success.
Shoelace formula works because two triangle forms a parallelogram, and the area of a parallelogram is given by a determinant. I think.
"""
import itertools as it
 
def area(a,b,c=(0,0)):
    xa, ya = a
    xb, yb = b
    xc, yc = c
    
    T = abs(xa*yb - xa*yc + xb*yc - xb*ya + xc*ya - xc*yb)
    return T
 
def contains_origin(coordinates):
    initial_area = area(*coordinates)
    areas_with_origin = [area(*coords) for coords in it.combinations(coordinates, 2)]
    return initial_area == sum(areas_with_origin)
 
if __name__ == "__main__":
    with open("0102_triangles.txt", 'r') as f:
        coordinates = f.readlines()
    coordinates = [map(int,c.strip().split(',')) for c in coordinates]
    coordinates = [list(it.batched(c, 2)) for c in coordinates]
    results = [contains_origin(c) for c in coordinates]
    total = sum(results)
    print(total)



