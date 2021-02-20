#Quadratic roots finder

import math

def Quadz(a,b,c):

    determinant = b**2 - 4*a*c

    #if determinant >= 0:
    result = (-b + math.sqrt(determinant))/2

    return(result)
    print(result)
        
