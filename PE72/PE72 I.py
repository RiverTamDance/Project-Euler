# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 09:52:07 2019

@author: Taylor

PE72


It dost appear to me that it would be computationally far easier to generate the reduced
fractions, rather than generating the list of all potential fractions and then reducing
this list. May be theoretically less easy, however. Especially considering I already have
the fraction reducer algo all sorted out.

Something something coprime. Yes this does appear to be the correct path to take. There is,
conveniently, a method for generating all coprime pairs. This method is exhaustive and 
non-redundant. Seems ez? Let us impliment it. Then we will take each coprime pair, where the
first element should be the largest (that is, the denominator), and the second element is the
numerator. bada bing, bada boom, we should have all the fractions we require.

I suppose the biggest problem/unknown at this point is how many branches we need to generate 
before we exceed the d <= 1,000,000 requirement.

"""

#Because my rule of thumb is to get a working version first, and worry about perfomance as
# a secondary concern, I will use a list as my data structure of choice.


Tree1 = [(2,1)] # even - odd pairs
Tree2 = [(3,1)] # odd - odd pairs

def CoprimeGenerator(t):
    
    m = t[0]
    n = t[1]
    
    Branch1 = (2*m-n,m)
    Branch2 = (2*m+n,m)
    Branch3 = (m+2*n,n)

    return(Branch1,Branch2,Branch3)

f = 0
j = 0

DenominatorLimit = 9

while f < 3:
    
    f = 0
    NewPairs1 = CoprimeGenerator(Tree1[j])
    
    for i in range(3):
        
        if (NewPairs1[i][0] < DenominatorLimit and
            NewPairs1[i][1] < DenominatorLimit):
            
            Tree1.append(NewPairs1[i])
        
        else:
            f += 1
            
    j += 1



f = 0
j = 0
            
while f < 3:

    f = 0
    NewPairs2 = CoprimeGenerator(Tree2[j])
    
    for i in range(3):
        
        if (NewPairs2[i][0] < DenominatorLimit and
            NewPairs2[i][1] < DenominatorLimit):
            
            Tree2.append(NewPairs2[i])
        
        else:
            f += 1
            
    j += 1
    


""" 

This shit was way too big to ever run. requires too much memory, too much time

"""

