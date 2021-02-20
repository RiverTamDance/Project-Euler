# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:42:53 2020

@author: Taylor

PE 51: Prime digit replacements
"""

"""
plan for now: I think the efficient way to go is to generate a whole wack of prime numbers.
I know for certain that the prime family contains 8 members. and there is 10 digits in our
numeral-set, meaning only two numerals don't work. 

Immediately we can eliminate the last position as worth testing, as even numbers in the 
last position are no longer prime.so for an n-length prime, we only have n-1 digits to play
with.

I want to use sets, but because some digits in a given prime may repeat, this probably won't
work.

I guess if I have two primes and i want to determine that they only differ in certain
positions, and that the value in these positions is the same, I can take the difference
at each digit position. That is, treating each prime as a vector of its digits, i can 
subtract one vector from another, and I should get, say, [0,x,0,0,x,0].

how do i prevent myself from having to check all the primes of the same length against
one another?

------------------------------
August 21st, 2020

if we have an m-digit number, there are AT MOST sum((m-1)C(n)), n in [1..m-1] ways to choose which 
which digits get replaced, I think.  Thus for any string of m digits, there are at most
2^(m-1) ways to replace the digits and retain primality. This could probably be brought 
down quite a lot. 
    This is definitely the naive way to do it. I would then compare this string 
This doesn't make any sense, really. If the primes are generated... we don't need to make 
replacement in the string. We can just get to comparing primes. This probably also won't work.
how many comparisons would i have to do? How many 8 digit primes are there? about 5 million
    I think this means I can put the rest out of my mind. depending on how this problem
should be solved, I will in any case need to either (i) check primality, or (ii) produce 
a list of primes. So mainly for the novelty of it, I will write a prime generator.


"""

"""Prime Generator"""
"""First thing: I've gotta decide what this looks like... I like the way it is lazy in Haskell
But i'm not sure that's easy to implement here. So it would be a function that returns
a list of the first n primes, for an input of n. It seems like the best way to do this is
to check its modularity with all primes less than and equal to its square root. 

--------------------------------------
*** October 22, 2020
So the 'search space' is the set of prime numbers. 

"""

import math
from itertools import chain, combinations, groupby
from collections import Counter

# This function appears to work p good
# It returns the right amount of primes
# for primes under 10,000
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

#print(primeList(100))

""" I have a few options. I could try to solve the general problem, and then use that
to solve my specific problem. But it could be a case where my particular problem doesn't
fall cleanly from the general solution, so that would be a waste of time. well, partial
waste of time, because i would at least learn a lot writing the general solution."""

""" I still like the idea of turning all my generated primes into vectors and then 
subtracting them from each other. I could then sort them, and the longest run of
duplicates is the answer """

""" And I know that the rightmost digit is irrelevent""" 

""" I think I need some better tech to deal with this problem. 
but i will try the bruteforce"""

""" Program plan:

    1. I take all the primes that have a certain length of digits. 
       E.g. all primes of length 3.
    2. A thought just came to me. And I've now forgetten it :)
       Lets see: if for each sum((m-1)C(n)), n in [1..m-1] = 2^(m-1) 
       possible substitution "ways", I blank out those
       spots in each number, then sort the list, then check to see number of duplicates,
       I wonder what the runtime of that will be. 2^(m-1) really isn't too bad, so
       I will give this a shot.
    
    Notes: i'm definitely repeating myself. But I think the understanding that the
    'one's column digit can never be part of the asterisk family is key. it removes some
    degrees of freedom. That is, our family of numbers will all have the same value in
    the 'one's column. 

"""    

#Alright I'm going to have to make sure that I get the 'fenceposts' right. It's
#going to depend on my arguments to powerset.
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

#The output is a list of tuples. let me try it with a random 5 digit number.

#print(list(powerset((1,2,3,4,5))))

#print(type(list(powerset((1,2,3)))[1]))

"""alright, I've got some slow code for turning an int into a list of digits. 
   while i like how simple the code is, apparently it is gonna be slower than
   using some mod 10 math way to break up the number. which is frustratingly inelegant.
   but I think this will be such a minor portion of the runtime that optimisations here
   aren't worth it just yet, if ever.
"""

#This will turn my integer into a list of integers.
#[int(x) for x in str(n)]

"""
workflow here: 

    1. generate tuple of primes with the requisite number of digits. Here I shall
       ensure that each prime is written as a list of digits.
       I want a tuple because I am going to have to access each member 2^(m-1) times.
    

    2.
      (1) ALL PRIMES 1 SUBSTITUTION
    Now should I try all primes in one pass, making a single pattern of '*' substitution, 
    store the highest number of identical results, and then go on to the next pattern,
    
    or

      (2) ALL SUBSTITIONS 1 PRIME
    should i generate all the patterns for 1 prime, and then do the next prime, so that
    i end up with a table of results and i just need to count the modal duplicates in each
    column?

    Important consideration: I need to be able to recover the primes which generated the
    family of '*' numbers. 

    As far as I can tell, these two approaches require the same amount of computation,
    aside from the number of times I need to compute powerset. 
    However, the 'all substitutions' approach require much more storage/memory. so uh...
    lets go with approach 1. 

    Actual implementation: 
        - take '*'-pattern from powerset list.
        - from tuple of primes, get 0th element.
        - keep only those digits as indicated by the '*'-pattern.

    3. How should I store all these same '*'-pattern primes? A dictionary seems like
       the right way to go here. Yes, store the values in a dictionary.
    
    4. Count them up and take the highest number of duplicates
       https://stackoverflow.com/questions/9401095/calculating-frequency-of-values-in-dictionary
 
       
    5. If this number of duplicates is higher than the previous number of duplicates,
       drop the old number and then find the small prime which was transformed 
       into one of those duplicates. Store it. 

    6. The value at the end should be the answer for that-number-of-digits-prime

    Note: probably THE most important thing to do is to figure out which '*'-patterns
          can be ignored because for 8-number families they won't produce primes. For the
          time being I won't think about this, because it may be that the problem
          doesn't require extra tricks, although I think it will/does.
        
    Note: i also need to decide how to store values at each stage. I should use tuples
          whenever possible, because I think they are reasonably faster.

"""
    
def primeFamily(d):

    #First we generate all the primes with d digits
    #Note that this is a tuple of tuples (integer, tuple of numchars like ('1','2',...)).
    primes = tuple([(p, tuple([x for x in str(p)])) for p in primeList(10**d) if p > 10**(d-1)])

    #Generate the list of '*'-patterns. I must be quite careful here. Say d = 5. Generically,
    # [[0], [1], [2], [3], [4]]. I do not want to touch [4]. so powerset(range(4)), cause range(4) is 0,1,2,3,
    # does the trick, however 4 is never included in the powerset results. 

    permuties = powerset(range(d-1))

    #Now we open get cooking on a big fat loop that does most of the processing.

    biggestFamily = (0,0)

    #I'm not sure a loop is the best structure for this but i'll roll with it for now.
    for nCr in permuties:

        pDict = {}

        for p in primes:

            #alright, you best believe i don't know how to optimise this at ALL. 
            #I think I will start by going for the 'easiest' solution, and then optimising
            #when it comes to it.

            #Like what data structure should I be using??
            #I think I will use a string. where I use asterisks as the replacement char.
            #so p looks like ('1','2','3','9') or something. now should it be a list rather than a tuple?
            # i'm unsure. and now i need to transform this string into e.g. for combination (0,2), 
            # ('1','x','3','9'). what is the fastest way to do this? I think it is worth worrying about speed here
            # but i can't figure it out so i shan't.
            
            #here i check to make sure that all the 'x' values are the same, and only proceed if they are.
            if all_equal([p[1][i] for i in nCr]):

                pDict[p[0]] = tuple([p[1][i] if i not in nCr else 'x' for i in range(d)])

        #With the dictionary in hand, now we extra the value with the most duplicates.
        #This extracts for us a tuple (value, count)
        #Only immutable types may be used as dictionary keys. frick. 

        if biggestFamily[1] < Counter(pDict.values()).most_common()[0][1]:
            biggestFamily = Counter(pDict.values()).most_common()[0]

    return(biggestFamily)


print(primeFamily(6))

#I just guessed the answer from here

""" 
Alright, big pause. I didn't account for the fact that the replaced digits (the 'x's) need to have the same
value. like xxxx7 could be 11117 or 22227 or... Fortunately, I think it is a straightforward fix. that is,
I have to edit the code that assigns key:value pairs in the dictionary. just a couple of lines should do it.
"""