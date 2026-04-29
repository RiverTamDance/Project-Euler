#March 31, 2026
 
"""
I think that Lagrange polynomial interpolation is the right way to proceed
a kth degree polynomial needs k+1 terms to agree before its good to go.
"""
 
import itertools as it
import math as mt
from decimal import Decimal
from typing import Callable
 
def polynomial_of_interest(x: int) -> Callable[[int],int]:
    terms = zip(it.cycle((1,-1)), range(11))
    u = sum([coeff*x**power for coeff, power in terms])
    return(u)
 
def basis_polynomial(xj: [int], nodes: [int]):
    def basis_polynomial_inner(arg):
        lj = mt.prod([Decimal((arg-xi))/Decimal((xj-xi)) for xi in nodes if xi != xj])
        return lj
    return basis_polynomial_inner
   
 
def lagrange_polynomial(nodes, values):
    def lagrange_polynomial_inner(arg):
        basis = [basis_polynomial(xj, nodes) for xj in nodes]
        L = sum([Decimal(y)*l(arg) for y,l in zip(values, basis)])
        return L
    return lagrange_polynomial_inner
 
u = polynomial_of_interest
target_values = [u(k) for k in range(1,20)] #20 is a safe upper bound
 
print(target_values)
 
fits = []
for k in range(1,11):
    nodes = range(1, k+1)
    values = target_values[:k+1]
    L = lagrange_polynomial(nodes, values)
    fits.append(L(k+1).quantize(Decimal('1')))
 
print(sum(fits))

