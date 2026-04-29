#Problem 103
#Special Subset Sums: Optimum
"""
Let's be bitter-lessonpilled, shall we? Brute force first, please and thank you.

What about getting all the partitions of a number, and from each partition of size n, we may select n-1 elements, 
which locks the nth element out from being considered for the rest of the special sum set.

OR

what about considering gaps between numbers. How about we try as many numbers that are 1 away, then 2 away, etc.


If the largest number in the set is 25, then the smallest two numbers have to be greater than 25


"""
"""
Created by Taylor Richards
taylordrichards@gmail.com
April 29, 2026
"""
import time
import itertools as it



def search(state):
    if len(state) == 7:
        return [state]
    else:
        states = []
        for state in get_choices(state):
            if (result := search(state)):
                states += result
        return states

def get_choices(state):

    candidates = range(state[-2]+1, state[-1])

    choices = []
    for v in candidates:
        new_state = state[:-1] + [v] + state[-1:]

        if check_subset_sums(new_state):
            choices.append(new_state)
    return choices

def check_subset_sums(values):
    double_sums = (sum(c) for c in it.combinations(values, 2))
    triple_sums = (sum(c) for c in it.combinations(values, 3))
    if has_duplicates(double_sums) or has_duplicates(triple_sums):
        return False
    else:
        return True


def has_duplicates(iterable):
    seen = set()
    return any(x in seen or seen.add(x) for x in iterable)

def size_check(state):
    if sum(state[:3]) > sum(state[-2:]):
        if sum(state[:4]) > sum(state[-3:]):
            return True

#-----------------------------------------------------------

start_time = time.perf_counter()

successes = []
for s2 in range(19, 32):
    for s1 in range(10, s2):
        for m in range(s2+1,s1+s2):
            state = [s1,s2,m]
            successes += search(state)


sums = [(sum(s),s) for s in successes if size_check(s)]
print(min(sums, key = lambda x: x[0]))

end_time = time.perf_counter()
print("--- %s seconds ---" % (end_time - start_time))
