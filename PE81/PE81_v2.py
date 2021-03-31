"""
PE
Created by Taylor Richards
taylordrichards@gmail.com
January 16, 2021 
"""

""" ---------------- PROBLEM STATEMENT ----------------

Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt

"""
""" ---------------- Discussion ----------------

because our matrix is 80x80, we have to be clever about this, else we get 158 choose 79 path sums
to pick from. 

I think the boring "rolling sum" method is the way to go. I will go imperative this time. 

"""
""" ---------------- Approach ----------------

#This has a fencepost counting problem inside it. a -> b -> c has three nodes but 2 edges.
# for a 5x5 matrix, a path has 9 nodes, and therefore has 8 edges. This 2*#rows -2

"""

import time
import csv

start_time = time.time()

with open('C:\\Users\\Taylor\\OneDrive\\Documents\\Project Euler\\PE81\\p081_matrix.txt') as f:
    reader = csv.reader(f)
    str_matrix = list(reader)
    matrix = [[[int(entry),0] for entry in row] for row in str_matrix]

n = len(matrix) 

for path_step in range(2*n - 2):

    #for now I will leave it at 157 path steps because our program "looks forward", so on the 157th path step we will be 
    #adding to the final layer.

    #The 'starting layer' is the sinister bend diagonal that contains the entries whose row+col is
    #equal to the path step. i.e. for path step 1, the set of entries under consideration
    # is {a(1,0), a(0,1)}, for path step 0 we have {a(0,0)}. well for FUGGS sake man, python is 0 based... so our matrix
    # is really 0...79 x 0...79. cmon BUDDY. 
    # I think a good place to start is to create a collection of (row, col) for entries in the 
    # starting layer.

    starting_layer = [(i,j) for i in range(n) for j in range(n) if i + j == path_step]

    for row, col in starting_layer:

        #alright this is the meat and potatoes of the venture.
        #alright so i've decided that the matrix will have a 2-length list as each entry. the first entry will be the 
        # natural number, as given by PE, and the second entry will be the result of summing the the previous layer with 
        # this entry. this is probably not the fastest way to do it, but I don't care :)
        if path_step == 0:
            node_val = matrix[row][col][0]
        else:
            node_val = matrix[row][col][1]

        #here we go "south". we have to do this check to ensure we don't throw an error for looking out of bounds of the matrix.
        if row < n - 1:

            check_val1 = matrix[row+1][col][0] + node_val
            
            #check if we have added to this node before
            if matrix[row+1][col][1] == 0:
                matrix[row+1][col][1] = check_val1

            elif matrix[row+1][col][1] > check_val1 :
                matrix[row+1][col][1] = check_val1
            
        #here we go "east"
        if col < n - 1:
        
            check_val2 = matrix[row][col+1][0] + node_val

            if matrix[row][col+1][1] == 0:
                matrix[row][col+1][1] = check_val2

            elif matrix[row][col+1][1] > check_val2:
                matrix[row][col+1][1] = check_val2

print(matrix[79][79])

print("--- %s seconds ---" % (time.time() - start_time))