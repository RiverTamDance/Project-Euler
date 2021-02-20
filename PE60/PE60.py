"""
PE
Created by Taylor Richards
February 14, 2021 
"""

""" ---------------- PROBLEM STATEMENT ----------------
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will
always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the
lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
""" ---------------- Discussion ----------------

right away, i note that i could find the 5 primes themselves, or I could find the nPr(5,2) = 20 primes that this family of 5 primes
creates.

Brainstorming: I could take an arbitrary prime p that looks like p1p2p3p4...pn. then I could split p into all possible pair-components, like (p1, p2p3...pn) and 
(p1p2p3.  p4...pn). so if p has n digits, this split produces n-1 pairs of numbers. each of these would have to be tested for primality (e.g. checked against the primelist)
In addition, e.g. p4...pnp1p2p3 would have to be tested for primality. I will turn the results of the prime-generator into a set, for muh speed. :)

For each prime I will then have "a list" of all its acceptable prime-splits. For instance, for 1097 I would discover 109 and 7.
NOTE: I will need to take care to exclude potential prime-splits where one of the splitees begins with 0. 

PAUSE: I have not done the analysis to determine if the 'backwards' approach is more efficient than the forwards approach. Let's check: there are 78498 primes < 1,000,000.
       for any two primes in our set, say p, q, we need to check p&q and q&p. very worst case, we have to check 6,000,000,000 numbers for primality. and then we have to figure
       out which 5 sub primes work.

       For the "backwards" method, I will state right away that I am not exploring the same problem space AT ALL. but the most straightforward analysis for me is:
       for each of the 78498 primes, which have about 6 digits on average, we have to test 5 split-pairs and their concatenation for primality, but only by consulting our 
       primeset - which is fast af. so that is 15 numbers to check. so 15*80,000=1,200,000 total numbers to check, but by consulting the primeset we've already generated.
       assuming that only about 5 of those get accepted, each of our 80,000 primes now has a "list" of 5 primes attached - 400,000 numbers total. and then we have to solve the
       same problem as above, but with far fewer numbers to check.  


I need to figure out how to "check" my list of acceptable prime splits and discover my family of 5. There is probably a computer science way to actually do this... time to think.
Think Pooh, think. Say I have the 'atoms' 3, 6, 20. This is what I am looking for. Together these generate 36, 63, 320, 203, 620, 206, which all pass 'the test'. I feel like
there is some graph trversal here or something... so with 36, i start with 3 and 6. then i will look for the 'next' pair that has 6 and x. then I will look for x and y. then
y and z, and finally z and 3. z 

Looks like I have a big ol' graph and i'm looking for cycles of length 5. 

DFS for Cycles: say I start x0. in our dictionary we have x0: {x1,x2,x3,x4,x5}. There are now 5 places I can go. Because I need to check all 
the cycles, I don't think breadth first or depth first matters. Not sure though. 

https://stackoverflow.com/questions/12367801/finding-all-cycles-in-undirected-graphs

"""
""" ---------------- Approach ----------------

I am going to start with a primeset less than 1,000,000. 



"""

import time
import sys
sys.path.insert(1, 'C:\\Users\\Taylor\\OneDrive\\Documents\\Project Euler\\Useful Functions\\')

from prime import primeList, isPrime

start_time = time.time()

primes = primeList(1000000)

print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()

prime_set = set(primes)

print(len(prime_set))

print("--- %s seconds ---" % (time.time() - start_time))