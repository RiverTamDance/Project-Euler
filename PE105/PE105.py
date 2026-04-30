import itertools as it
import time
 
def check_numerosity(seq):
   
    for i in range(2, (len(seq)+1)//2 + 1):
    	if sum(seq[:i]) <= sum(seq[1-i:]):
        	return False
   
    return True
   
 
def compare_subsets(seq):
   
    for i in range(2, len(seq)//2+1):
    	tuple_sums = (sum(t) for t in it.combinations(seq, i))
    	if has_duplicates(tuple_sums):
        	return False
   
    return True
   
 
def has_duplicates(iterable):
	seen = set()
	return any(x in seen or seen.add(x) for x in iterable)
   
 
 
 
with open("0105_sets.txt", "r") as f:
	sequences = f.readlines()
	sequences = [x.strip().split(",") for x in sequences]
	sequences = [
    	[int(x) for x in seq]
    	for seq in sequences
	]
	sequences = [sorted(x) for x in sequences]
 
start_time = time.time()
 
total = 0
for seq in sequences:
	if check_numerosity(seq) and compare_subsets(seq):
    	total += sum(seq)
 
print(total)
print("--- %s seconds ---" % (time.time() - start_time))