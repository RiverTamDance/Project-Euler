"""
PE 82
Created by Taylor Richards
taylordrichards@gmail.com
March 31, 2021 
"""

""" ---------------- PROBLEM STATEMENT ----------------

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the 
left column and finishing in any cell in the right column, and only moving up, down, and right

"""
""" ---------------- Discussion ----------------

Because I had a looksee in the solution for PE81, I learned about Djikstra's Algorithm and Bellman-Ford. Because our matrix
doesn't contain negative values, i do not believe there is an advantage to using BF.

This does seem to clarify/simplify what I have to do. I hope.

1. determine if I can use Djikstra's algo on this problem. I think it requires me constructing a graph, where there is an
   an edge between nodes a and b if b is above, below, or to the right of a.

2. I want to write this as object, so i will finally have to try some python OOP.


"""
""" ---------------- Approach ----------------
"""

import time
import sys
sys.path.insert(1, 'C:\\Users\\Taylor\\OneDrive\\Documents\\Project Euler\\Useful Functions\\')

from prime import primeList, isPrime

start_time = time.time()

print("--- %s seconds ---" % (time.time() - start_time))