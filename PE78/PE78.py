"""
PE
Created by Taylor Richards
taylordrichards@gmail.com
March 17, 2023
"""

import time
import itertools as it

def main():
    start_time = time.perf_counter()


    
    def gen_table():
    
        table = {(0,0) : 1}
        
                    #populate the next row and column of the table
        for n in it.count(1):
            
            table[0,n] = 1
            
            for i in range(1, n+1):

                #row calculate
                if i == 1:
                    #print("i == 1")
                    table[n,i] = 1
                elif n == 0:
                    #print("n == 0")
                    table[n,i] = 1
                else:
                    #print("recursion")
                    table[n,i] = table[n-i, i] + table[n,i-1]
                
                #column calculate
                #print("i,i")
                table[i,n] = table[i,i] 
                
            yield(table[n,n])

    partitions = gen_table()

    sol = None
    n = 0
    while not sol:
        n += 1
        p = next(partitions)
        
        if n % 1000 == 0:
            print(f'{n} | {p}')
        
        if p % 10**6 == 0:
            sol = n



    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()
