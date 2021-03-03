"""
PE 62
Created by Taylor Richards
taylordrichards@gmail.com
March 2, 2021 
"""

""" ---------------- PROBLEM STATEMENT ----------------

The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104 (384**3) and 66430125 (405**3). 
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

"""
""" ---------------- Discussion ----------------

https://stackoverflow.com/questions/8866652/determine-if-2-lists-have-the-same-elements-regardless-of-order

"""
""" ---------------- Approach ----------------



"""

import time
from collections import Counter, defaultdict
from itertools import takewhile
from math import ceil, floor

start_time = time.time()

#so the ceiling bit is the smallest integer which, when cubed, is >= 10**n
#the floor part is the smallest integer which, when cubed, is <= 10**n+1

#The "only" mistake I made was losing the cube itself. I need some way to keep track of that.

def counters(n):

    cubes_len_n = [str(b**3) for b in range(ceil((10**((n-1)/3))), floor(10**((n)/3) + 1))]
    cnts_dict = defaultdict(list)
    for c in cubes_len_n:
    
        tup_counter = tuple((k,Counter(c)[k]) for k in sorted(Counter(c).keys()))
        cnts_dict[tup_counter].append(c)

    return(cnts_dict)

sol_found = False
n = 12
sol = []

while sol_found == False:

    for k in counters(n).keys():
        if len(counters(n)[k]) == 5:
            sol = sol + counters(n)[k]
            sol_found = True
    
    n += 1

print(sol)

#print(Counter(counter_list(5)).values())
#Now I will turn my cubes into strings, and then turn the strings into Counter objects
#Then I will turn the counter objects into tuples -- this step feels unnecessary. But its easy lel
#Then I will use a counter on the list of tuples, and check if any of the values in the counter
#are equal to 5

print("--- %s seconds ---" % (time.time() - start_time))