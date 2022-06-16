
import math as mt
from operator import itemgetter
import decimal
from decimal import Decimal


def main():

    decimal.getcontext().prec = 100

    def cfr(a):
    #this function works, it seems, for both finite and infinite continued fractions. of course, once a finite fraction gets exhausted, the function goes weird.
        while True:
            i = a // Decimal(1)
            yield(i)
            f = a % Decimal(1)
            a = Decimal(1)/f
    #print(next(cfr),next(cfr), next(cfr), next(cfr))

    ## This example works as intended for the first four next()s.
    # n = 415/93
    # cfr = cfr(n)
    # print(next(cfr),next(cfr), next(cfr), next(cfr))

    def convergents(cfr, conlist):
        a = next(cfr)
        hnew = a*conlist[-1][0] + conlist[-2][0]
        knew = a*conlist[-1][1] + conlist[-2][1]
        return(hnew, knew)

    #had to add this line otherwise the while loop would just always use the trivial solution (0, 1)

    def get_sols(D):
        
        conlist = [(Decimal(0), Decimal(1)), (Decimal(1), Decimal(0))]
        sqD = D.sqrt()
        rfc = cfr(sqD)
        
        conlist.append(convergents(rfc, conlist))
        while conlist[-1][0]**2-D*conlist[-1][1]**2 != 1:
            conlist.append(convergents(rfc, conlist))

        return((D, conlist[-1][0], conlist[-1][1]))

    squares = [x**2 for x in range(32)]
    upper_bound = 1001
    nums = [x for x in range(2, upper_bound) if x not in squares]
    sols=[]

    for D in nums:
        D = Decimal(D)
        sols.append(get_sols(D))

    sols.sort(key=itemgetter(1), reverse=True)

    print(sols[:3])

if __name__ == "__main__":
    main()

