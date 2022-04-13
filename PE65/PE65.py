from math import gcd
import itertools as it

def flip(flippable):
    """print(flip([1,2,3,4]))"""
    return flippable[::-1]

def rational_add(rat1, rat2):

    a, b = rat1
    c, d = rat2

    return ((a*d + c*b, b*d))

def frac_reduce(rat):

    a, b = rat
    k = gcd(a,b)

    return((a//k, b//k))

def cont_frac(values, depth):

    depth -= 1

    if depth == 0:
        return ((values[0], 1))
    
    rat1 = (values[0], 1)
    rat2 = flip(cont_frac(values[1:], depth))
    rat3 = rational_add(rat1, rat2)
    result = frac_reduce(rat3)
    return(result)

def make_two(num):

    if num % 3 != 0:
        return(1)
    else:
        return(num // 3 * 2)

#gives [2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1,..., 66, 1]
terms = list(it.islice(map(make_two, it.count(3)), 0, 200))

e_terms = [2,1] + terms

numerator = str(cont_frac(e_terms, 100)[0])

print(sum([int(i) for i in numerator]))



# print(gcd(3,7))