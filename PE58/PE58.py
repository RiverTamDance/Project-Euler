"""
PE58
Created by Taylor Richards
January 17, 2021 
"""

""" ---------------- PROBLEM STATEMENT ----------------

If one complete new layer is wrapped around the spiral above, a square spiral with side 
length 9 will be formed. If this process is continued, what is the side length of the 
square spiral for which the ratio of primes along both diagonals first falls below 10%?

"""
""" ---------------- Discussion ----------------

I can use some of the relationships between the layers and odd squares to keep track of
layers and so on.

I want to calculate the numbers lying on each diagonal, as well as keep track of which
layer they are on.

For layer n, they are located at (nth odd num)^2 + 1*(nth odd num - 1)  

(nth odd num)^2 + 2*(nth odd num - 1)  
(nth odd num)^2 + 3*(nth odd num - 1) 

while (nth odd num)^2 + 4*(nth odd num - 1) is (n+1th odd num)^2


https://www.codegrepper.com/code-examples/delphi/importing+python+file+from+another+directory

*** Update Jan 19: ***
my approach has not been working. the size of the primes where the < .10 ratio condition is met appears to be
above 10,000,000. The thing is, I am calculating wayyyy too many primes for this to be efficient. I only need
to check the primality of the specific numbers being tested, which itself only requires checking against primes
less than or equal to the square root of the number being tested. 


"""

""" ---------------- Approach ----------------

1. I want to write a function that gives me the 4 numbers lying on the diagonals for
   that layer. 

2. Then I will check their primality and return (probably a list) with their primality
   status attached to their value. 

3. I am just going to assume that primes < 1,000,000 is enough. if not we try again.

"""
import time
import sys

sys.path.insert(1, 'C:\\Users\\Taylor\\OneDrive\\Documents\\Project Euler\\Useful Functions\\')

from prime import primeList, isPrime

#returns a list of the 4 corner values in descending order.
def cornerVals(n):

    return([(2*n-1)**2 - 2*(n-1)*i for i in range(4)])


#Let's run this baby
start_time = time.time()

# for i in range(1, 21):
#    print(i)
#    print(isPrime(i, primo))

primo = primeList(1000000)
doomer = False
primeCount = 0
n = 2

while doomer == False:

    for c in cornerVals(n):

        if isPrime(c, primo):
            primeCount += 1
        elif c > 1000000000:

            print("I bad")
            doomer = True
    
    if primeCount/(4*(n-1)+1) < .1:
        print(2*n-1)
        doomer = True
    else:
        n += 1

print("--- %s seconds ---" % (time.time() - start_time))