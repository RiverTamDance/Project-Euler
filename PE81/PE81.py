"""
PE 81
Created by Taylor Richards
taylordrichards@gmail.com
March 27, 2021
"""

""" ---------------- PROBLEM STATEMENT ----------------

Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt

"""
""" ---------------- Discussion ----------------

Before any real "solving" work gets underway, I need to import the matrix. I don't know what data structure I want to store it as - a list comes to mind first.

I think a recursive approach to this problem sounds right n good. start at the bottom right, produce 2 numbers - the results of summing the bottom right number with
the number above it and the number to its left. and then do it again, consider the new location to be "the bottom right". I think I will begin by designing this
function. seems fun!

I didn't even stop and think about this, fortunately i assumed it was true - we don't have to record the path itself, we merely have to find the minimal path sum. 

Right now I am trying to figure out the right way to construct the base case/output. this is always
the challenge I find with trying to build these recursive functions. What I want as an output is
the path sum for each possible path in the matrix. So, a list, a set, a dictionary, whatever.
Seems that a list makes most sense, just feels the most natural, although i'm not sure why. 

the trouble, for is, is embiggening the list of results as the calls proceed. I'm just too dumb rn
hmmmmm. 

God i feel so dumb for not figuring this out. I can use a list comprehension to unpack whatever
the next call returns. ofc ofc.

"""
""" ---------------- Approach ----------------

    The Function
The function takes in a matrix and returns, in part, up to 2 numbers - the left number and the right number.
These two numbers should should be accompanied by two new function calls. 

"""

import time
import csv
from functools import lru_cache


start_time = time.time()

with open('C:\\Users\\Taylor\\OneDrive\\Documents\\Project Euler\\PE81\\p081_matrix.txt') as f:
    reader = csv.reader(f)
    str_matrix = list(reader)
    matrix = tuple(tuple(int(entry) for entry in row) for row in str_matrix)

@lru_cache()
def path_summer(matrix):
    #we don't need coords, as we are always dealing with the bottom right entry. 
    #matrix = [[row1],[row2],...]
    path_sums = ()
    br_num = matrix[-1][-1]

    #now we subset the matrix, creating two sub matrices. 1 with the bottom row removed, one with the rightmost col gone.
    #i really need to double check that these references I am creating do not affect one another. **************************************

    #we delete the last row to get the "up" matrix, this is the action of going up.
    mat_up = matrix[:-1]

    #we delete the last column to get the "left" matrix, this is the action of going left. 
    mat_left = tuple(row[:-1] for row in matrix)

    #base case:
    if len(mat_left[0]) == 0 and len(mat_up) == 0:
        
        path_sums = (br_num,)

    else:
        #We check the number of columns (by checking the number of entries in the first row), and if there is more than 1, we can go "left"
        if len(mat_left[0]) > 0:
            # this condition means that we will never do path sums for a matrix like [[],[],...]
            path_sums = tuple(br_num + path_sum for path_sum in path_summer(mat_left))
        
        if len(mat_up) > 0:
            
            path_sums = path_sums + tuple(br_num + path_sum for path_sum in path_summer(mat_up))
    
    return(path_sums)

#Okay the function works on the test matrix. now time to read in the real matrix. 
test_matrix = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]
test_matrix2 = tuple(tuple(int(entry) for entry in row) for row in test_matrix)

print(min(path_summer(matrix)))
print("--- %s seconds ---" % (time.time() - start_time))

# alright well this program doesn't work for large enough matrices. real shame.