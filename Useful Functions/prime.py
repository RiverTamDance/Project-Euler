import math

def primeList_old(n):
    
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

def primeList(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if sieve[i]:
            # i*i is the square of the number we are working with, duh. 
            sieve[i*i::2*i]=[False]*int(((n-i*i-1)//(2*i)+1))
    return [2] + [i for i in range(3,n,2) if sieve[i]]

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
    

