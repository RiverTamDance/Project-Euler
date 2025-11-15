#PE100

import math

def Quadz(a,b,c):

    determinant = b**2 - 4*a*c

    #if determinant >= 0:
    result = (-b + math.sqrt(determinant))/2

    return(result)


def IntCheck(x):
    
    if x == math.floor(x):
        return True
    else:
        return False



result = 0
n=30

while result == 0 and n < 10**15:
    
    Tar = Quadz(1,-1,-(n**2-n)/2)

    if IntCheck(Tar) == True:
        result = Tar
    else:
        n = n+1

print (result)
print(n)
