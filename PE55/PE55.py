"""
PE55
Created by Taylor Richards
January 14, 2021 
"""

"""
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.
Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. 
A number that never forms a palindrome through the reverse and add process is called a Lychrel number. 
Due to the theoretical nature of these numbers, and for the purpose of this problem, 
we shall assume that a number is Lychrel until proven otherwise. 
In addition you are given that for every number below ten-thousand, it will either 
    (i) become a palindrome in less than fifty iterations, or, 
    (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. 
         In fact, 10677 is the first number to be shown to require over fifty iterations before producing a
         palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

***How many Lychrel numbers are there below ten-thousand?***
"""

""" --------------DISCUSSION----------------

How do I go about solving this? Let me have a think. 

    - I need to be able to identify palindromes.
    - I need to be able to reverse a number.
    - I need to be able to count 50 iterations and then stop (Fencepost potential).

1. I take next number in [0..9999]
   Note: I don't know if 0 is counted or not. so right away the answer might be 1 higher or lower.

2. I check if iterations are <= 48 (they start at 0). Go back to 1 if > 48
3. I reverse it and then add the original and the reverse, and +1 an iteration. 

4. I check if I have produced a palindrome. 
   If I have, then I increase the palindrome (non-Lychrel) counter +1. I go back to 1
   Otherwise, I go back to 2

5. I subtract the number of non-Lychrels from 9999 and that is the answer. 
"""

# i plan to be really cancer and just switch back and forth between strings and integers.

""" EXAMPLE
Taking every nth-element of a list
>>> nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> nums[::2]
[10, 30, 50, 70, 90]

The full slice syntax is: start:stop:step. 
"""
import time

def isLychrel(num):

    goes = 0
    lychrel = True

    while goes <= 48 and lychrel == True:

        soomer = num + int(str(num)[::-1])
        goes += 1 

        if soomer == int(str(soomer)[::-1]):
            lychrel = False
        else:
            num = soomer

    return(lychrel)

start_time = time.time()

count = 0

for num in range(10000):

    if isLychrel(num) == True:
        count += 1

print("--- %s seconds ---" % (time.time() - start_time))
print(count)