import numba 
import numpy as np
import time


def pe108_2(threshold):
    n=2
    while True:
        val = count_reciprocals_2(n)+1
        if val > 1000:
            return(n, val)
        n+=1


@numba.njit(parallel = True)
def count_reciprocals_1(n):
    n = np.uint64(n)
    i = np.arange(1,n, dtype = np.uint64)
    nni = n*(n+i)
    return (nni % i ==0).sum()


@numba.njit(parallel = True)
def count_reciprocals_2(n):
    n = np.int64(n)
    acc=0
    for i in numba.prange(1,n):
        acc += (n*(n+i)) % i == 0

    return acc


if __name__ == "__main__":
    n = 1000000
    t1 = time.perf_counter()
    print(pe108_2(n))
    print(time.perf_counter() - t1)

# def pe108(threshold):

#     n = 1
#     highest_count = 0
#     biggest_n = 2

#     while highest_count < threshold:
#         n += 1

#         current_count = 1
#         for i in range(1,n):
#             d = math.gcd(i, n*(n+i))
#             r = i//d
#             if r == 1:
#                 current_count += 1

#         if current_count > highest_count:
#             highest_count = current_count
#             biggest_n = n
    
#     return biggest_n, highest_count