import operator as o
import itertools as it
import time

start_time = time.time()

def add_rat(rat1, rat2):
    a,b = rat1
    c,d = rat2
    return((a*d + c*b, b*d))

def left_sub_rat(rat1, rat2):
    a,b = rat1
    c,d = rat2
    return((a*d - c*b, b*d))

def right_sub_rat(rat1, rat2):
    a,b = rat1
    c,d = rat2
    return((c*b - a*d, b*d))

def mul_rat(rat1, rat2):
    a,b = rat1
    c,d = rat2
    return((a*c, b*d))

def right_div_rat(rat1, rat2):
    a,b = rat1
    c,d = rat2
    return((a*d, b*c))

def left_div_rat(rat1, rat2):
    return(right_div_rat(rat1,rat2)[::-1])

def one_expression(ops, ns):

    op1, op2, op3 = ops

    n1 = (ns[0], 1)
    n2 = (ns[1], 1)
    n3 = (ns[2], 1)
    n4 = (ns[3], 1)

    def f(g, a, b):
        return(g(a,b))

    p1 = f(op1, n1, n2)
    p2 = f(op2, p1, n3)
    p3 = f(op3, p2, n4)

    if p3[1] != 0:
        total = p3[0]/p3[1]
        return(total)
    else:
        return("div0")

# ops=(o.add,o.add,o.add)
# ns = (1, 2, 3, 4)

op_list = [add_rat, left_sub_rat, right_sub_rat, mul_rat, right_div_rat, left_div_rat]
op_cart = list(it.product(op_list, repeat = 3))

#I tried this all the way up to 49 and still (1,2,5,6) was the best at 43. So I believe what is needed is better "rationals"
#handling code.
# n_list = [i for i in range(25)]
# #n_list = [1,2,3,4]
# n_possibilities = list(it.combinations(n_list, 4))

# count_and_fours = []
# for four_n in n_possibilities:

#     n_cart = list(it.permutations(four_n, 4))

#     solutions = []
#     for ops in op_cart:

#         #list of lists of all outputs for a given ops and all perms of ns.
#         solutions.append([one_expression(ops, ns) for ns in n_cart])

#     #union together all the solution sets (so this is now across all ops and perms of [x1, x2, x3, x4])
#     solutions = list(set().union(*solutions))

#     #remove "div0" results
#     solutions = [i for i in solutions if i != "div0"]
#     #remove non-whole numbers
#     solutions = [i for i in solutions if i % 1 == 0]
#     #remove negatives and sort
#     solutions = sorted([i for i in solutions if i > 0])
#     sol_count = list(zip(solutions,it.count(1)))
#     count_and_fours.append([len(list(it.takewhile(lambda x: x[0] == x[1], sol_count)))] + [four_n])

# count_and_fours.sort(key = o.itemgetter(0), reverse = True)
# print(count_and_fours)

# print([i for i in count_and_fours if i[1] == (1,2,4,8)])
# print("--- %s seconds ---" % (time.time() - start_time))

inputs = it.permutations([1,5,6,7])

outputs = []
for input in inputs:
    for ops in op_cart:
        outputs.append((input, ops, one_expression(ops,input)))

solutions = [output for output in outputs if output[2] == 21]

print(solutions)