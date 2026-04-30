"""
    Plan
I think I can only compare tuples composed of alternating elements.
"""
 
#Sketch
"""
ex = [0,1,2,3,4,5,6]
 
(0,2) -> {(1,3),(1,4),(1,5),(1,6)}
(0,3) -> {(1,2),(1,4),(1,5),(1,6)}
(0,4)
 
Looks to me like some rules are:
    1. a pair can never have adjacent values,
    2. pairs must be interleaved
   
for n=4,
(1) {0,1,1,0} vs (1,0,0,1}
(2) {1,0,1,0} vs {0,1,0,1}
However, I know that one of these is unacceptable. Which one?
(2) is unacceptable, as s2 > s1 and s4 > s3, so (s2, s4) = (s1+a,s3+b)
 
So the actual rule is that for any pair of ordered tuples, all three elements can not all be larger or smaller.
"""
 
import itertools as it
 
def compare(pairs_of_tuples):
    acceptable = []
   
    for pair in pairs_of_tuples:
        lt_condition = all(x[0] < x[1] for x in zip(*pair))
        gt_condition = all(x[0] > x[1] for x in zip(*pair))
        if not (lt_condition or gt_condition):
            acceptable.append(pair)
   
    return acceptable
   
def unique(pair):
    t1, t2 = pair
    if len(set(t1+t2)) == 2*len(t1):
        return True
    else:
        return False
 
n=12
total = 0
for tuple_size in range(2, n//2+1):
    dummy = range(n)
    tuples = it.combinations(dummy, tuple_size)
    pairs_of_tuples = list(it.combinations(tuples, 2))
    pairs_of_tuples = filter(unique, pairs_of_tuples)
   
    total+=len(compare(pairs_of_tuples))
 
print(total)

