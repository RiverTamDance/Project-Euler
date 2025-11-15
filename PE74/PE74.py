"""
Created by Taylor Richards
taylordrichards@gmail.com
June 14, 2024


This problem is interesting because everything eventually falls into 1 of 4 loops. Unless "1" and "2" also
count as possible 1-loops.

I kind of just want to do this the naive way, but I'm worried about sequences that "blow up" and go much larger.

I don't believe order matters for this question. so that 69 and 96 give the same answer. This sounds crazy,
But I think there are only 5005 (wrong, this is only for 6 digit numbers) combinations with replacement of 
10**5 <= numbers < 10**6 with entries from 0..9.

Alright, reproved the stars and bars formula to myself. Leading 0s make the math a little weird, maybe.
I'm not sure at which point I will ahve to account for the leading 0s problem.

Dang, I think I will have to put some thought into the issue of the leading zeros. I will need to decide how many 
"viable unique orderings" a collection of digits has.

for example, 0012 has: 1200, 1020, 1002, 2100, 2010, 2001. I think this works out to the following: I have 2 choices
for the lead digit... dang this is annoying, because 1100 would have a different answer. frick.

how many unique orderings does 1100 have? 1100, 1001, 0011, 1010, 0101, 0110. I believe this is correct. 
--> How many of these are viable? 3. How many orderings have 0 at the start? 
I think the way to find the number we want, the number of viable orderings, meaning orderings that don't start with 0,
is: assume there is a 0 in the left most position, and then find the number of all arrangements with the remaining n-1
digits. We then have to divide out all digits with multiplicity > 1
    For example: 0,0,0,0,0,5 only has 1 legitimate arrangement: 500000. total number of arrangements:
6!/(5!*1!) = 6. subtract out all 0-starting arrangements. 5!/(4!*1!) = 5. answer: 1, as expecting. good.
    After thinking about it, I dont think there is anyway to do this math more efficiently without isking some floating point
nonsense.

Okay, now I want to think about how to actually solve this, I think i have enough pieces to get started.
    - I can determine the "factorial sum" of all numbers from 1 to 1000000. 
    - At which point, I think I have a recursive serach type structure. I create chains that accumulate until they reach
      a value that is already part of the chain.
      A big issue here is that chains can diverge off pretty bigly. However, since we can drop chains once they have length
      > 60, I'm not sure how much of an issue this really is. 

On the other hand, it is kind of tempting to try this problem backward. slash that might be the only way to do this...


"""
import time
from math import prod, comb
import itertools as it
import typing
from collections import Counter

factorial = {n:prod([n-i for i in range(n)]) for n in range(10)}

def factorial_sum(arrangement):
    return(sum([factorial[int(s)] for s in arrangement]))

def distinct_combinations(counter):
    length = factorial[(counter.total())]
    repeats = prod([factorial[v] for v in counter.values()])
    return(length/repeats)

def distinct_combinations_zero(counter):
    if counter['0'] > 0:
        counter['0'] -= 1
        return(distinct_combinations(counter))
    else:
        return(0)

def number_of_numbers(sequence):
    counter = Counter(sequence)
    return(distinct_combinations(counter)-distinct_combinations_zero(counter))


def main():
    start_time = time.perf_counter()

    #let's generate the search space
    ss: list[tuple[str, ...]] = [x for i in range(1,7) for x in list(it.combinations_with_replacement(['0','1','2','3','4','5','6','7','8','9'],i)) if x not in [('0',) *i for i in range(1, 7)]]

    #create dictionary with factorial sum values for 8007 options
    D: dict[tuple[str, ...], int] = {sequence:factorial_sum(sequence) for sequence in ss}
    
    # Fill out the rest of the dictionary
    filled_out = False
    while not filled_out:
        no_corresponding_entry = [tuple(sorted(str(D[k]))) for k in D.keys() if tuple(sorted(str(D[k]))) not in D]
        if no_corresponding_entry:
            T = {sequence:factorial_sum(sequence) for sequence in no_corresponding_entry}
            D = D | T
        else:
            filled_out = True

    counts = {sequence:number_of_numbers(sequence) for sequence in D.keys()}

    #145 is a special case, I think my program should be able to handle it. I can just ignore it, because it will loop
    #after 1 node, meaning its no where close to 60 nodes, so nothing to worry about.
    solutions = []
    for starter in D.keys():
        no_repeats = True
        node = D[starter] # nodes are numbers, not sequences
        nodes = [starter, node]

        while no_repeats and len(nodes) <= 60:
            node = factorial_sum(str(node))
            if node in nodes:
                #exit time
                no_repeats = False
            else:
                #keep the loop going
                nodes.append(node)
            if len(nodes) == 60:
                solutions.append(nodes)
                no_repeats = False

    # Finally, let me multiply each chain in the solution list by the number of numbers that would begin that chain.

    print(sum([counts[sol[0]] for sol in solutions]))

    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()