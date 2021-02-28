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

    BIG MISTAKE HERE^^^^ - I am looking for complete subgraphs with 5 nodes.
    This is what I actually want: https://en.wikipedia.org/wiki/Clique_problem#Cliques_of_fixed_size
    The big O notation here is giving us the worst-case. And I think it's unrealistic. This is testing
    EVERY NODE with replacement, not even bothering to find relevant nodes by looking down adjacent edges. 
    Excitingly, I suppose this means I can come up with my own algo :).

DFS for Cycles: say I start x0. in our dictionary we have x0: {x1,x2,x3,x4,x5}. There are now 5 places I can go. Because I need to check all 
the cycles, I don't think breadth first or depth first matters. Not sure though. 

https://stackoverflow.com/questions/12367801/finding-all-cycles-in-undirected-graphs

"""
""" ---------------- Approach ----------------

I am going to start with a primeset less than 1,000,000 and solve the problem for the original example, that is cycles of length 4 

1. I will build the set of prime pairs. For each prime in our primeset, I will take all len(p)-1 pairs and check their individual primality and their reverse primality.  
2. Now i need to do my DFS bit. 
    a. I build the graph as a dictionary with { node : {nodes} }
    NOTE: there is definitely some symmetry here I am failing to exploit. might not matter though.
   I might have been a bit hasty assuming that DFS was the ticket. I'm going to try the brain dead for loop approach, and then if that takes too long i'll try the spanning tree approach. 

   The loop should go something like this:
   -for each key in the dictionary (starting node), 

"""

import time
import sys
sys.path.insert(1, 'C:\\Users\\Taylor\\OneDrive\\Documents\\Project Euler\\Useful Functions\\')
from itertools import zip_longest

from prime import primeList, isPrime

start_time = time.time()

#Here I begin building my list elidgible prime pairs
primes = primeList(10000000)
prime_set = set(primes)

subprimes = []

for p in prime_set:

    p_str = str(p)

    # I have to add in code to catch if we have a number like 3019, which turns into 3 & 19...

    for i in range(1,len(p_str)):

        if p_str[:i][0] != '0' and p_str[i:][0] != '0':
            if prime_set.issuperset({int(p_str[:i]), int(p_str[i:]), int(p_str[i:] + p_str[:i])}):

                subprimes.append([int(p_str[:i]), int(p_str[i:])])
            
#I have now built the list of elidgible prime pairs. 
# print(prime_set.issuperset({319}))
# print(prime_set.issuperset({int("193"[2:] + "193"[:2])}))
# print([3,19] in subprimes)
# print([19,3] in subprimes)

# testvals = []
# for a in range(1,6):
#     for b in range(1,6):
#         testvals.append([a,b])

#subprimes = subprimes + testvals

flat_subprimes = {p for pair in subprimes for p in pair}
graph_dict = {node : {adj_node for edge in [edge for edge in subprimes if node in edge] 
             for adj_node in edge if adj_node != node} for node in flat_subprimes}

def cycle_delver(node, n, subgraph):

    #Hmmm i'm really not sure if this base case helps us exit properly
    
    #now I can assume that the list graph_dict[node] is sorted. which is v useful. 

    if n == 0:
        return([[node]])
    else:
        paths = []
        for adj_node in graph_dict[node]:
            if adj_node > node:
                if graph_dict[adj_node].issuperset(subgraph):
                    paths = paths + [[node] + path for path in cycle_delver(adj_node, n-1, subgraph.union({adj_node}))]

        return(paths)


winner = 0
winnercycle = []

print("--- %s seconds ---" % (time.time() - start_time))

for p in flat_subprimes:
    for cycle in cycle_delver(p,4,{p}):

        if winner == 0:
            winner = sum(cycle)
            winnercycle = cycle
        elif sum(cycle) < winner:
            winner = sum(cycle)
            winnercycle = cycle

print(winner)
print(winnercycle)

#print(graph_dict[19])

print("--- %s seconds ---" % (time.time() - start_time))

# okay, issues:
# 1. I haven't been checking that within the cycle, there is an edge from each node to every other node
# 2. 