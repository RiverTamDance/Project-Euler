# PE53


def FacToR(n,limN):
        
    if n == limN:
        return limN
    else:
        return n * FacToR(n-1,limN)

def factorial(n):
        
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def Cnr(n,r):

    limN = n-r+1
    
    num = (FacToR(n,limN)//(factorial(r)))

    return(num)                            


def BigNuff(n):

    r = 2
    result = 0
    
    while result == 0 and r<=n:
        if Cnr(n,r) > 1000000:
            result = n-2*r+1
        else:
            r = r+1

    return result

print(sum ([BigNuff(n) for n in range(101)]))
    

            
