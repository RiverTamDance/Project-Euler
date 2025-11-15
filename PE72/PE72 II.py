"""
Created by Taylor Richards
taylordrichards@gmail.com
June 13, 2024

It strikes me immediately that a diagonalization argument could work here.

HCF(n,d) = 1 is equivalent to n and d being coprime/relatively prime.

I can look at this from the numerator or denominator perspective. I'm not sure which is better.

My first idea was to simply find all coprimes of all numbers <= 1,000,000. However, that involves 500 billion invocations of the gcd function,
which is probably not a great way to solve this. Although I think it is doable. 

Reading the wiki, this looks like its just a boring application of Euler's totient. So we just need to count all numbers that are comprime
to all d <= 1,000,000


"""
import time
import sys
sys.path.insert(1, 'C:\\Users\\John Q Hackerman\\OneDrive\\Documents\\Project Euler\\Useful Functions\\')
from prime import eulers_totients

def main():
    start_time = time.perf_counter()

    ## main code goes here
    
    target = 1000001

    result = sum(eulers_totients(target).values())

    print(result)

    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()