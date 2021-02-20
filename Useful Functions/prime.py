import math

def primeList(n):
    
    pList = [2, 3, 5, 7]

    for k in range(11, n+1):

        notPrime = False
        i = 0
        p = pList[i]
        sqrt_ceiling = math.sqrt(k)

        while p <= sqrt_ceiling and not notPrime:

            if k % p == 0:
                notPrime = True

            i += 1
            p = pList[i]

        if not notPrime:
            pList.append(k)

    return (pList)



def isPrime(c,primes):

    i = 0
    p = primes[i]
    notPrime = False

    while p <= math.sqrt(c) and not notPrime:

        if c % p == 0:
            notPrime = True

        i += 1
        p = primes[i]

    return(not notPrime)
    

