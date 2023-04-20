#I would like to start by getting the snippets working again.

"""
PE
Created by Taylor Richards
taylordrichards@gmail.com
January 19, 2023
"""

import time
import sys
import itertools as it

useful_functions_path = ("C:\\Users\\Taylo\\OneDrive\\Documents"
    "\\Project Euler\\Useful Functions\\")

sys.path.insert(1, useful_functions_path)
import prime as p

def main():
    start_time = time.perf_counter()

    ## main code goes here
##----------------------------



#-----------------------------

    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()

