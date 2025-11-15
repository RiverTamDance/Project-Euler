#Project Euler 94

from math import sqrt
from multiprocessing import Pool
import time
import decimal as dec

def triangle_area_big_b(a):
    """Heron's formula to calculate area of triangle, b = a+1"""
    
    b = a+1

    radicand = (a-1)*(3*a+1)
    radicand = dec.Decimal(radicand)
    area = (b*radicand.sqrt())/4

    return(area)

def triangle_area_small_b(a):
    """Heron's formula to calculate area of triangle, b = a+1"""
    
    b = a-1

    radicand = (a+1)*(3*a-1)
    radicand = dec.Decimal(radicand)
    area = (b*radicand.sqrt())/4
    
    return(area)
    
def is_whole_area(a):

    perimeter_total = 0
    
    A1 = triangle_area_big_b(a)
    A2 = triangle_area_small_b(a)

    if int(A1) == A1:
       perimeter_total += 3*a + 1
    
    if int(A2) == A2:
       perimeter_total += 3*a - 1
    return(perimeter_total)

def main():
    dec.getcontext().prec = 3
    
    result = 0
    #ranges = [(3,1000), (1000-1,2000)]
    # ranges = [(3,10**8-1),(10**8-1, 2*10**8-1), (2*10**8-1, 333_333_333+1)]
    # for r in ranges:

    inputs = [a for a in range(3,333333333+1,2)]

    with Pool(20) as pool:
        suitable_perims = pool.map(is_whole_area, inputs)
    
    result += sum(suitable_perims)
    print(result)

if __name__ == "__main__":
    start_time = time.time()
    
    main()
    
    print("--- %s seconds ---" % (time.time() - start_time))
