"""
PE57
Created by Taylor Richards
January 16, 2021 
"""

""" ---------------- PROBLEM STATEMENT ----------------

In the first one-thousand expansions, how many fractions contain a numerator with more
digits than the denominator?

"""

""" ---------------- Discussion ----------------

There probably is some sneaky-breaky way to do this, like by actually thinking about it
but why do that when I could smash out some more mindless code?

The only tricky bit here is figuring out how to do continued fractions. and its a bit
of a headache. but once I get that I should be good to go.

"""

""" ---------------- Approach ----------------

I don't have a good mind for it yet, but I want to build a recursive function that
computes the ith iteration of this continued fraction.

I have discovered a decorator that caches the results.
https://realpython.com/python-thinking-recursively/#naive-recursion-is-naive

Now the challenge is to use fractional form and not decimal.

What I really want to do is keep track of the numerator and denominator. I never actually
want to divide. That makes me think. Do I need to keep track of two values or of
just one? Yeah if I want them to stay integers I need to keep track of two values... or no?

1. write the recursive function.
2. don't forget to add 1 to the result!
3. 

"""

import time

#This is what does the hashing!!
from functools import lru_cache

#This decorator hashes the results of cf(n)
@lru_cache(maxsize=None)
def cf(n):

    if n <= 1:
        return (1,2)
    else:
        return (cf(n-1)[1], 2*cf(n-1)[1]+cf(n-1)[0])

#This guy just adds that extra 1 to the whole ordeal. 
def stilicho(n):

    return (cf(n)[0] + cf(n)[1], cf(n)[1])

# main loop where we get 'er done.
start_time = time.time()

coont = 0
for n in range(1,1001):
    
    if len(str(stilicho(n)[0])) > len(str(stilicho(n)[1])):
        coont += 1

print(coont)
print("--- %s seconds ---" % (time.time() - start_time))