"""
Created by Taylor Richards
taylordrichards@gmail.com
April 05, 2023
"""
import time
from pathlib import Path
import itertools as it
from collections import defaultdict, deque
import copy

def main():
    start_time = time.perf_counter()

    p = Path(__file__).with_name("p096_sudoku.txt")

    ## main code goes here
    with p.open("r") as sudoku_file:
        sudoku_file_contents = sudoku_file.read()
    
    s1 = sudoku_file_contents.splitlines()

    sudokus = dict()
    for i in range(50):

        rows, s1 = s1[1:10], s1[10:]
        sudoku = dict()

        for row_num, row_str in enumerate(rows):
            for col in range(9):
                #The values of a sudoku dictionary entry are (actual value, potential values)
                sudoku[row_num, col] = [int(row_str[col]),set()]

        sudokus[i] = sudoku

    

    squares = defaultdict(list)

    #I should probably use a generator for the list of keys, so I have an infinite list that I can keep taking from until the issue is solved
    num_coords = it.product(range(9), range(9))
    for coords in num_coords:
        row, col = coords[0], coords[1]
        squares[row//3, col//3].append((row, col))

    set_o_9 = {i for i in range(1,10)}

    def simplify(sudoku, change = True):

        while change:
            change = False

            for num in sudoku.keys():

                row, col = num[0], num[1]
                
                if sudoku[row, col][0] == 0:

                    row_set = {sudoku[row, j][0]  for j in range(9)}
                    col_set = {sudoku[i, col][0] for i in range(9)}
                    square_set = {sudoku[coord][0] for coord in squares[row//3, col//3]}

                    union = row_set | col_set | square_set

                    # for i in range(9):
                    #     print([sudoku[i,j][0] for j in range(9)])

                    potential_set = set_o_9 - union

                    # print(num)
                    # print(potential_set)

                    if len(potential_set) == 1:
                        sudoku[row, col][0] = potential_set.pop()
                        change = True
                    elif sudoku[row, col][1] != potential_set:
                        #This portion of code reduces the potential set even if it doesn't determine an answer for a given element.
                        #This could be an opportunity for an infinite loop
                        sudoku[row, col][1] = potential_set
                        change = True
    
    def no_zeros(sudoku):
        entries = list(zip(*sudoku.values()))
        if 0 in entries[0]:
            return(False)
        else:
            return(True)

    
    def solver(sudoku):

        guess_stack = deque()
        guess_stack.append(sudoku)
        solved = False

        while solved == False:

            sudoku = guess_stack.pop()

            simplify(sudoku)
            solved = no_zeros(sudoku)

            if solved == False:
                #add guesses to the stack
                if [0, set()] not in sudoku.values():
                    unsolved_coords = [values[0] for values in sudoku.items() if values[1][0] == 0]
                    #I need to make sure to drop a sudoku if it has any value like [0:, set()], which indicates
                    ##that we have found a 0 element for which no solution exists. its a dead node. 
                    for coords in unsolved_coords:
                        for potential_value in sudoku[coords][1]:
                            new_sudoku = copy.deepcopy(sudoku)
                            new_sudoku[coords] = [potential_value, set()]
                            
                            guess_stack.appendleft(new_sudoku)

        return(sudoku)

    
    solved_sudokus = dict()
    solved_sudokus[3] = solver(sudokus[5])    
    # for i in range(50):
    #     solved_sudokus[i] = solver(sudokus[i])

    total = 0
    for s in solved_sudokus:
        for j in range(3):
            total += solved_sudokus[s][0,j][0]
        print(no_zeros(solved_sudokus[s]))



    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()