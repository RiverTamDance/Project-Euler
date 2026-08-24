import sympy
import functools
import math
import time
 
 
#My goal is to build the most primely-dense composite number.
@functools.cache
def prime(n):
    return sympy.prime(n)
   
@functools.cache
def partitions(n, max_size = None) -> list[list[int]]:
    """ partitions returns a list of lists of ints """
    if max_size is None:
        max_size = n
   
    if n < 1:
        return []
    elif n == 1:
        return [[1]]
    elif max_size == 1:
        return [[1]*n]
       
    ps = partitions(n-max_size, min(n-max_size,max_size))
    if ps:
        left = [[max_size]+p for p in ps]
    else:
        left = [[max_size]]
       
    right = [p for p in partitions(n, max_size-1) if p[0] != 0]
    return left+right
   
        
if __name__ == "__main__":
    start_time = time.perf_counter()
    best_answer = float('inf')
    for n in range(20):
        ps = partitions(n)
        for p in ps:
            divisor_count = int((math.prod([2*c+1 for c in p])+1)/2)
            if divisor_count > 4_000_000:
                best_answer = min(math.prod([prime(i+1)**c for i,c in enumerate(p)]), best_answer)
                print(n, p, best_answer)
    print(time.perf_counter()-start_time)
    # largest_divisor_count = 0
    # for n in range(5_000_000):
        # factors = sympy.ntheory.factor_.factorint(n)
        # divisor_count = int((math.prod([2*v+1 for k,v in factors.items()])+1)/2)
        # if divisor_count > largest_divisor_count:
            # largest_divisor_count = divisor_count
            # print(n, largest_divisor_count, factors)
# I have found that 22 primes to the first power would put us over the 4 million solutions threshold.
#Which tells me that the answer is likely much lower, probably 15-17 primes

