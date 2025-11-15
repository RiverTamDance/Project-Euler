"""
Created by Taylor Richards
taylordrichards@gmail.com
July 18, 2025
"""
import time
from functools import cache
import math

@cache
def square_triangular(n):
    if n==0:
        return(0)
    elif n==1: 
        return(1)
    else:
        return(34*square_triangular(n-1) - square_triangular(n-2) + 2)
    
def blue_balls(R):
    
    radicand = 8*R**2+16*R+9
    summand_1 = 3+2*R
    summand_2 = math.sqrt(radicand)
    
    B1 = summand_1-summand_2
    B2 = summand_1+summand_2
    
    return(B1/2, B2/2)

def main():
    start_time = time.perf_counter()


    square_triangular_numbers = [square_triangular(n) for n in range(1,10)]
    Rs = [math.sqrt(st) for st in square_triangular_numbers]
    Bs = [blue_balls(R) for R in Rs]

    return(Bs)

    # i = 0
    # found = False
    # while not found:
    #     i += 1
    #     R = square_triangular(i)






    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    print(main())