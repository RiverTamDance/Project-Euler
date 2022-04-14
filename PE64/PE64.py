# Funny enough I think i actually want to start things off with the simplify step.

# I think the data I want to pass back and forth in this program should look llike ((rt, x), y). Although, maybe passing it is too tricky. hmmm


#rt_tuple = (rt, term, d)

from math import sqrt
import itertools as it


def one_pass(rt_tuple):

    rt2, term, d = rt_tuple

    #Flip
    #Get difference of squares
    #Simplify

    m = (sqrt(rt2) + term)//d
    term = abs(term - m*d)
    d = (rt2 - term**2)//d

    rt_tuple = rt2, term, d

    return (rt_tuple, m)

rt1 = (23, 0, 1)

def period_length(n):
    results = []
    result = ((n,0,1),0)
    while result not in results:

        results.append(result)
        result = one_pass(result[0])

    return(len(results) - 2)

#list(it.islice(map(lambda x: x**2, it.count(1)), 0,100))
#Because I know the upper bound on the squares that are to be ignored, i can use a finite range.
squares = [i**2 for i in range(101)]
not_squares = [i for i in range(10001) if i not in squares]
len_list = [period_length(i) for i in not_squares]
odd_len_list = [i for i in len_list if i % 2 != 0]

print(len(odd_len_list))