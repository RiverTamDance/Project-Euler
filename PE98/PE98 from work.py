#find all anagrams


""" 
    -sort each word
    -add it to a dictionary, sorted version as the key, actual version as the value.
    
    I have determined that the longest word in our anagram collection is 9 digits.
    Question:    What length does the square have to be to produce that?
    Answer: 99,999 is the largest number that needs to be checked.
    
"""

from collections import defaultdict
import time
from math import sqrt, ceil
start_time = time.time()

input_file_location = "0098_words.txt"

with open(input_file_location) as f:
    text = f.read()
    words = text.split(',')
    words = [w.strip('"') for w in words]


anagram_words = defaultdict(list)

for w in words:
    anagram_words[''.join(sorted(w))].append(w)
    
anagram_words = [ws for ws in anagram_words.values() if len(ws) > 1]

#----------------------------------------------------    
#Let's find the max length word in our colleciton
longest = 0
for ws in anagram_words:
    if len(ws[0])> longest:
        longest = len(ws[0])
#----------------------------------------------------

squares = {n:n**2 for n in range(10**((longest+1)//2))}

anagram_squares = defaultdict(list)
for s in squares.values():
    anagram_squares[''.join(sorted(str(s)))].append(s)

anagram_squares = [ss for ss in anagram_squares.values() if len(ss) > 1]

"""
Alright, so now I'm at a bit of a loss for how to proceed...
I need some way to check if permutations are equivalent. I need to check if 
there is an isomorphism, I think. 

Let me think through this:
say I have 'SHUT', 'TUSH', 'HUTS'. 
    - I know I need to look at 4 digit long squares.
    - I need these squares to have 4 distinct digits.
    - unfortunately, I think I still need to develop some way to track how the mapping in performed.
    - and the other thing to take care of is for instances where there are more
    than two words in the anagram set and more than two squares in the other anagram set
    
    I think some sort of easy positional encoding type thing is right.
    so SHUT -> TUSH is 4312. The fourth character becomes the first character, and so on. Going the other way we get 3421
    
    

print("--- %s seconds ---" % (time.time() - start_time))