"""
PE
Created by Taylor Richards
January 23, 2021 
"""

""" ---------------- PROBLEM STATEMENT ----------------

Each character on a computer is assigned a unique code and the preferred standard is ASCII 
(American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, 
and lowercase k = 107. A modern encryption method is to take a text file, convert the bytes to ASCII, 
then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is 
that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, 
then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of 
random bytes. The user would keep the encrypted message and the encryption key in different locations, 
and without both "halves", it is impossible to decrypt the message. Unfortunately, this method is impractical 
for most users, so the modified method is to use a password as a key. If the password is shorter than the 
message, which is likely, the key is repeated cyclically throughout the message. The balance for this method 
is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. 

"""
""" ---------------- Discussion ----------------

How XOR works: 
A bitwise XOR is a binary operation that takes two bit patterns of equal length and performs the logical exclusive OR operation
 on each pair of corresponding bits. The result in each position is 1 if only one of the bits is 1, but will be 0 if both are 0 
 or both are 1. In this we perform the comparison of two bits, being 1 if the two bits are different, and 0 if they are the same.

ASCII Info
Originally based on the English alphabet, ASCII encodes 128 specified characters into seven-bit integers as shown by the ASCII chart above.[11] 
Ninety-five of the encoded characters are printable: these include the digits 0 to 9, lowercase letters a to z, uppercase letters A to Z, and punctuation symbols. 
In addition, the original ASCII specification included 33 non-printing control codes which originated with Teletype machines; most of these are now obsolete,
[12] although a few are still commonly used, such as the carriage return, line feed and tab codes.

Alright, I could probably ignore the 33 non printing characters, although i don't think it matters so I guess I will try them. 

- I note right away that it appears none of the encrypted values are larger than 100. interesting.

so, best as I can tell, I go through all the encrypted values, XORing with whatever value of the key is appropriate (going 1,2,3,1,2,3,...) and then I have to check
against a dictionary to see if I've got english words.

holy shit it says LOWER CASE (lul) characters. that really reduces the search space. so should i only exclude capital letters? hmmm...

"""
""" ---------------- Approach ----------------

- get the data into a list
- create a generator for all 3 ASCII-character combinations - and it specifies lowercase, so that gives us the numbers 33-64 and 91-126
    NOTE: there are 2.1 million possible keys with all characters eligible. 
- XOR each encrypted character with the relevant trial key character
    https://stackoverflow.com/questions/23416381/circular-list-iterator-in-python

Most troublesome step:
- check that the result is english


"""

import time
import csv
import itertools
import nltk
from nltk.corpus import words
import operator
import re

#nltk.download('words')

start_time = time.time()

with open('C:\\Users\\Taylor\\OneDrive\\Documents\\Project Euler\\PE59\\cipher.csv') as f:
    reader = csv.reader(f)
    encrypted_data = list(reader)

#We get the csv as a list with a single element which is a list of all the values. Let us not forget that these values are strings.
encrypted_data = [int(x) for x in encrypted_data[0]]

ASCII_search_space_iterator = itertools.chain((range(33,65)),range(91,127)) 

match_dict = {}

for trial_key in itertools.permutations(ASCII_search_space_iterator,3):

    trial_key_pool = itertools.cycle(trial_key)
    unencrypted_data = map(operator.xor, encrypted_data, trial_key_pool)
    unencrypted_string = ''.join(map(chr,unencrypted_data))
    re_match = re.search(' a ', unencrypted_string)

    if not re_match == None:

        re_match = re.search(' the ', unencrypted_string)
        
        if not re_match == None:
            
            print(trial_key)
            print(unencrypted_string)
            print(sum(map(operator.xor, encrypted_data, trial_key_pool)))


print("--- %s seconds ---" % (time.time() - start_time))