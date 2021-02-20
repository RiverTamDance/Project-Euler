# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:53:31 2019

@author: Taylor

PE71

"""

"""
Let's write the Euclidean Algorithm. This will give us the greatest common divisor (GCD), aka
the HCF. so for any pair of numbers, we run the algo, find the GCD, divide both numbers by
this GCD, and then we GO AGANE until the GCD is 1. Then we will have a reduced fraction.
"""
import math

def EuclideanAlgorithm(a,b):
    
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)
    else:
        if a >= b:
            return EuclideanAlgorithm(b, a%b)
        if b > a:
            return EuclideanAlgorithm(a, b%a)
        
def FractionReducer(n,d):
    
    c = EuclideanAlgorithm(n,d)
    
    if c == 1:
        return (n,d)
    else:
        return FractionReducer(n/c,d/c)
    
OrderedFractionList = []
g = (3/7)
tol = 0.000001
    
for i in range(1,1000001):
    
    upperbound = min(int(i//(g-tol)),1000001)
    lowerbound = min(math.ceil(i/(g+tol)),upperbound-1)
    
    for j in range (lowerbound-1, upperbound+1):
        t1 = FractionReducer(i,j)
        OrderedFractionList.append(t1)
#    OrderedFractionList = list(set(OrderedFractionList))
#print (OrderedFractionList[OrderedFractionList.index([3,7])-1][0])
    
NewList = [[3,7,(3/7)]]
    
for el in OrderedFractionList:
    if el[1] != 0:
        NewList.append([el[0],el[1],(el[0]/el[1])])
    
import operator
    
NewList2 = sorted(NewList,key=operator.itemgetter(2))

    
    