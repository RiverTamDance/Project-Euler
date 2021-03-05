"""
PE 63
Created by Taylor Richards
taylordrichards@gmail.com
March 4, 2021 
"""

""" ---------------- PROBLEM STATEMENT ----------------
The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, 
is a ninth power.

How many n-digit positive integers exist which are also an nth power?

"""
""" ---------------- Discussion ----------------

don't forget that 1**1 = 1, 2**1 = 2, for all i in range(10).

I basically just need to come up with the theoretical upper limit to this question, and then
compute guilt-free.

I am proposing that there is a relationship. Understanding this is probably more difficult than the question
in itself, but worth it for the practice, i imagine. 

so we have a function f(n,pow) = len(n**pow). We want where pow == len(n**pow). If we hold n fixed, then
f_n(pow) = len(n**pow) is monotonic and unbounded. meaning that for any M, exists pow s.t. 
M < len(n**pow). So i supposed i have to figure out where that bound is for any n. 

because 2 is the most extreme case, i.e. the slowest increase, we have that 2**4 brings us to 2 digit numbers
2**8 3 digits, and so on. so once this catches up, we are good. okay so we will find the upperbound using
powers of 2.


okay so now I will have n such that len(2**n) > n, and this means i will never have to exponentiate higher
than this n. it may be too wide of a net tho. whatever computers are fast. 

"""
""" ---------------- Approach ----------------
"""

import time
import math
start_time = time.time()

solsum = 0

for i in range(1,10):

    n=1

    while (n-1)/n <= math.log(i,10):
        
        print((i, n, len(str(i**n))))

        n += 1
    
    print((i, n, len(str(i**n))))
    solsum = solsum + n-1

print(solsum)


print("--- %s seconds ---" % (time.time() - start_time))