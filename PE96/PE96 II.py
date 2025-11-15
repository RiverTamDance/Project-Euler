"""
Created by Taylor Richards
taylordrichards@gmail.com
April 12, 2023
"""
import time
from pathlib import Path
import itertools as it
from collections import defaultdict
import copy

def main():
    start_time = time.perf_counter()

    n = 51

    p = Path(__file__).with_name("p096_sudoku.txt")

    with p.open("r") as sudoku_file:
        sudoku_file_contents = sudoku_file.read()
    
    s1 = sudoku_file_contents.splitlines()

    sudokus = dict() 
    for i in range(n):

        rows, s1 = s1[1:10], s1[10:]
        sudoku = dict()

        for row_num, row_str in enumerate(rows):
            for col in range(9):
                #The values of a sudoku dictionary entry are [actual value, {potential values}]

                sudoku[row_num, col] = [int(row_str[col]), set()]

        sudokus[i] = sudoku
    
    squares = defaultdict(list)

    #I should probably use a generator for the list of keys, so I have an infinite list that I can keep taking from until the issue is solved
    num_coords = it.product(range(9), range(9))
    for coords in num_coords:
        row, col = coords[0], coords[1]
        squares[row//3, col//3].append((row, col))

    set_o_9 = {i for i in range(1,10)}

    #we need to initialise each entry with its potential set
    for i in sudokus:
        sudoku = sudokus[i]
        for coords in sudoku:
            row, col = coords[0], coords[1]
            actual_value = sudoku[row,col][0]

            if actual_value == 0:
                row_set = {sudoku[row, j][0]  for j in range(9)}
                col_set =  {sudoku[i, col][0] for i in range(9)}
                square_set = {sudoku[coord][0] for coord in squares[row//3, col//3]}

                union = row_set | col_set | square_set
                potential_set = set_o_9 - union
                sudoku[row, col] = [actual_value, potential_set]

    def checksum(sudoku):

        for i in range(9):
            rowset = {sudoku[i, col][0] for col in range(9)}
            colset = {sudoku[row, i][0] for row in range(9)}
            if rowset != set_o_9:
                return(f"row issue {i}, {rowset}")
            if colset != set_o_9:
                return(f"col issue {i}, {colset}")
            
        for i in it.product((0,1,2), repeat = 2):
            squareset = {sudoku[coords][0] for coords in squares[i]}
            if squareset != set_o_9:
                return(f"square issue {i}, {squareset}")
        
        return("okay")
    
    # test_sudoku = sudokus[0]
    # print(checksum(test_sudoku))
    
    def simplify(sudoku, change = True):

        while change:
            change = False
    
            for coords in sudoku:
                row, col = coords[0], coords[1]

                if sudoku[row, col][0] == 0:

                    potential_set = sudoku[row, col][1]

                    if len(potential_set) == 1:
                        change = True
                        sudoku[row,col][0] = potential_set.pop()
                        update_sudoku(sudoku, coords, sudoku[row,col][0])
                    else:
                        #compare potential sets
                        ## I think I subract from each potential set all the potential sets in its 3-fold path
                        row_potential_sets = set().union(*[sudoku[row, j][1] for j in range(9) if j != col])
                        column_potential_sets = set().union(*[sudoku[i, col][1] for i in range(9) if i != row])
                        square_potential_sets = set().union(*[sudoku[coord][1] for coord in squares[row//3, col//3] if coord != (row,col)])

                        row_potential_difference = potential_set - row_potential_sets
                        column_potential_difference = potential_set - column_potential_sets
                        square_potential_difference = potential_set - square_potential_sets


                        if len(row_potential_difference) == 1:
                            change = True
                            sudoku[row,col] = [row_potential_difference.pop(), set()]
                            update_sudoku(sudoku, coords, sudoku[row,col][0])
                        elif len(column_potential_difference) == 1:
                            change = True
                            sudoku[row,col] = [column_potential_difference.pop(), set()]
                            update_sudoku(sudoku, coords, sudoku[row,col][0])
                        elif len(square_potential_difference) == 1:
                            change = True
                            sudoku[row,col] = [square_potential_difference.pop(), set()]
                            update_sudoku(sudoku, coords, sudoku[row,col][0])
                        
                            #update potential sets

    def update_sudoku(sudoku, coords, actual_value):
        
        row, col = coords[0], coords[1]

        for i in range(9):
            #row update
            sudoku[i, col][1].discard(actual_value)
            #col update
            sudoku[row, i][1].discard(actual_value)
        #square update
        for square_coords in squares[row//3, col//3]:
            sudoku[square_coords][1].discard(actual_value)
    
    def solve(sudoku):
        #Isn't this actually a depth first search?
        guess_stack = [sudoku]
        solved = False

        while solved == False:

            sudoku = guess_stack.pop()

            simplify(sudoku)
            solved = no_zeros(sudoku)

            if solved == False:
                #add guesses to the stack
                #This if check kills a branch of the search if it finds an impossible scenario.
                if [0, set()] not in sudoku.values():
                    unsolved_items = filter(lambda x: x[1][0] == 0, sudoku.items())
                    minimum_unsolved_item = min(unsolved_items, key = lambda x: len(x[1][1]))
                    #I need to make sure to drop a sudoku if it has any value like [0:, set()], which indicates
                    ##that we have found a 0 element for which no solution exists. its a dead node. 
                    coords = minimum_unsolved_item[0]
                    for potential_value in minimum_unsolved_item[1][1]:
                        new_sudoku = copy.deepcopy(sudoku)
                        new_sudoku[coords] = [potential_value, set()]
                        update_sudoku(new_sudoku, coords, potential_value)
                        guess_stack.append(new_sudoku)
            else:
                somethings_wrong = checksum(sudoku)

                if somethings_wrong != "okay":
                    print(somethings_wrong)
                    # for i in range(9):
                    #     print([sudoku[i,j][0] for j in range(9)])
            
            if not guess_stack and solved == False:
                print("here!")
            
        return(sudoku)
    
    def no_zeros(sudoku):
        entries = list(zip(*sudoku.values()))
        if 0 in entries[0]:
            return(False)
        else:
            return(True)

    total = 0
    for i in range(n):
        sudoku = solve(sudokus[i])
        nums = [sudoku[0,col][0] for col in range(3)]

        for k in range(9):
            print([sudoku[k,j][0] for j in range(9)])

        total += 100*nums[0] + 10*nums[1] + nums[2]
        print(str(nums[0]) + str(nums[1]) + str(nums[2]))
    print(total)

    # n = 5

    # sudoku = solve(sudokus[n])
    # for i in range(9):
    #     print([sudoku[i,j][0] for j in range(9)])

    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()