import math
import time

start_time = time.time()
winner = [1,1,0]
x=0
    
with open(r"C:\Users\Taylor\Desktop\p099_base_exp.txt",'r') as ProblemFile:
    for line in ProblemFile:

        x=x+1
        Prep = line.rstrip()
        Prep2 = Prep.split(",")
        BasExp=[int(Prep2[0]),int(Prep2[1])]
        
        Current = math.log(BasExp[0])*BasExp[1]

        if Current > (math.log(winner[0])*winner[1]):
            winner=[BasExp[0],BasExp[1],x]

print(winner)
print("--- %s seconds ---" % (time.time() - start_time))
 
