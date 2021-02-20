"""
PE56
Created by Taylor Richards
January 16, 2021 
"""

""" ---------------- PROBLEM DESCRIPTION ----------------

A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: 
one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

"""

""" ---------------- Discussion ----------------

I don't see why I don't just compute this... this shouldn't be hard for my computer to compute? 
I guess I will find out lol. I 99**99 and it was no problem, so we'll find out if the naive approach 
causes problems. I also don't think there is any other way to do it. Of course there must be, 
but its not obvious to me.

Well, I suppse I could quite easily only check powers above 90, as thats probably where the solution lies. 
But then again, 100^100 has a sum less than 2^2.

"""

""" ---------------- Approach ----------------

1. I will loop a through [0..99], and then inner loop b through [0..99]. 
2. I will calculate a^b.
3. I will turn this number into an iterable of digits.
4. I will sum this iterable
5. I will check this sum against the previous, storing it if it is larger.
6. return the max sum.

"""

maxSoom = 0

for a in range(100):
    for b in range(100):
        
        soomer = sum([int(d) for d in str(a**b)])
        
        if soomer > maxSoom:
            maxSoom = soomer

print(maxSoom)
