"""
Created by Taylor Richards
taylordrichards@gmail.com
October 07, 2024

I have done the early work for this on my work computer. Now I need to tackle the meat. 

Let me use the example SADDERR - DRREADS - DARREDS. This example has 2 properties we would like
to anticipate and handle: its has 3 anagrams, and it repeated letters. I should also spoof up some
numbers that correspond to these three words.

SADDERR
1233455

DRREADS
3554231

DARREDS
3255431

I need to make this clear: my task is to find the "transformation sequence(s)" for an anagram pair
of letters, and then see if any anagram squares of the right size share this transformation sequence.

So let's write a function that takes in a pair of confirmed anagrams, and generates all of their
transformation sequences.

Because letters map to numbers one-to-one, 

"""
import time
from collections import defaultdict, deque
import time
from math import sqrt, ceil
import itertools as it

def main():
    start_time = time.perf_counter()

    input_file_location = r"PE98\0098_words.txt"

    with open(input_file_location) as f:
        text = f.read()
        words = text.split(',')
        words = [w.strip('"') for w in words]

    anagram_words = defaultdict(list)

    for w in words:
        anagram_words[''.join(sorted(w))].append(w)
        
    anagram_words = [ws for ws in anagram_words.values() if len(ws) > 1]

    #----------------------------------------------------    
    #The word with the most unique letters
    longest = (0,'')
    for ws in anagram_words:
        for w in ws:
            unique_count = len(''.join(set(w)))
            if unique_count > longest[0]:
                longest = (unique_count,w)

    #Let's find the max length word in our colleciton
    longest = 0
    for ws in anagram_words:
        if len(ws[0])> longest:
            longest = len(ws[0])
            longest_word = ws
    # print(longest)
    # print(longest_word)
    #----------------------------------------------------

    squares = {n:n**2 for n in range(10**((longest+1)//2))}

    anagram_squares = defaultdict(list)
    for s in squares.values():
        anagram_squares[''.join(sorted(str(s)))].append(s)

    anagram_squares = [ss for ss in anagram_squares.values() if len(ss) > 1]

    #----------------------------------------------------
    # Let's find the number with the most unique digits.
    # I think this was a waste of time.

    # longest = (0,0)
    # for ss in anagram_squares:
    #     for s in ss:
    #         unique_count = len(''.join(set(str(s))))
    #         if unique_count > longest[0]:
    #             longest = (unique_count,s)
    # print(longest)

    #----------------------------------------------------


    def transformations(anagram_1, anagram_2):
        """returns a record of the transformations required to send anagram_1 into anagram_2
        Example: "bat" -> "tab". b gets sent to position 3, a gets sent to position 2, and t gets sent to position 1.
        therefore, the transformation [3,2,1] transforms bat into tab. 

        Example: "free" -> "reef" [4,1,3,2] and [4,1,2,3]. Note: I can reverse the transormation sequence t by taking
        t[i] = t[t[i]]. Take care to ensure that swaps are all made simultaneously.

        Now, what I need to consider is: do I need to worry about duplicated letters? I don't think i do, so long as the order
        in which I transform them is consistent for both words and numbers. CONSISTENT ORDER MATTERS

        So, how do I do this? I want to do this without designing some monstrosity of an algo. If I wanted to transform
        "free" into "reef", I could do the following:

            - create a dictionary where the keys are the letters of "reef", and the values are the positions of those letters.
              In this case, "reef" would get r:[0], e:[1,2], f:[3]
            - I may then scan "free" from left to right, and create a transformation sequence by taking the corresponding 
              leftmost value from the dictionary for each letter in "free", where I would get [D[f], D[r], D[e], D[e]]
              = [3,0,1,2]
        ^^^ Whoopsie, the above is sound but backwards. I sent reef into free. So I need to create a dictionary of "free" and 
        map "reef" into it. So we get f:[0], r:[1], e:[2,3], giving [D[r], D[e], D[e], D[f]] = [1,2,3,0]

        returns the transformation sequence (a list of ints) that sends anagram_1 into anagram_2

        Note that the two words better be anagrams or this function fails. no error-handling, get rekt.

        """
        r = zip(anagram_1, it.count())
        anagram_1_positions = defaultdict(deque)

        for k,v in r:
            anagram_1_positions[k].append(v)

        transformation_sequence = []
        for letter in anagram_2:
            transformation_sequence.append(anagram_1_positions[letter].popleft())        
        
        return(tuple(transformation_sequence))

    # print(anagram_squares[:10])
    # print(anagram_words[:10])

    """Now I need to actually find the answers. I think I have nearly all the setup done. I believe I "reverse" search
    Should find the answer, because we want the biggest... ? Yeah squaring is monotonic so yeah.

    So I will filter the list of squares to only include squares of length 9 or less.

    What I really want is to find pairs that have matching transformation sequences. As I stated above. very good. 
    Excellent, in fact.
    """
    #only get squares of length 9 or less.
    anagram_squares = [ss for ss in anagram_squares if len(str(ss[0])) <= 9]

    #print(anagram_squares[-10:])

    """Now I need to consider how I actually go about matching transformation sequences to transformation sequences.
    In an example like RACE CARE ACRE, where there should be 3 (or 6, given we want reverse sequences too) sequences,
    I can't discard any of the transformation sequences. because I have no way of knowing which transformation sequence
    will be associated with the largest square number, which is what I want.

    And, note the scenario: CARE and RACE have the same transformation sequence as RATE and TARE. so how do I deal with that?
    If I use a dicionary, as I am planning, to store transformation_sequence:original_words, does the fact that multiple sets of original
    words can share a transformation sequence? No, it doesn't, because the problem doesn't care about the contents of the words.
    It cares about the size of the squares. so when I store transformation_sequence:squares, if I have a collision there, that is where
    I should test qhich square is bigger and store the larger squares.
 
    Plan:
    
    Create dictionary of transformation sequences, with items as follows:
        transformation_sequence: [anagram_1, anagram_2]
    which means that we will also have 
        reverse(transformation_sequence): [anagram_2, anagram_1]
    And anagrams with more than two entries will simply get entries for each pair, like ACRE RACE CARE.
    And for situations like TARE RATE vs CARE RACE, I will simply update to the latest entry or whatever. it doesn't matter.



    After creating this dictionary, I will create another dictionary, this time for the square anagrams. Again, each pair
    of squares in a cluster will produce 2 entries, a forewards and backwards transformation sequence. However, this time,
    There will be an updating rule in the dictionary that matters. When there is a collision in transformation sequence, 
    I will check which of the pairs in the the value entry list contain a higher maximum value. That is the pair list I will store. 

    ^^^ This may be all unneccessary. Instead, I can just take the largest square set, produce the corresponding set transfromation sequences,
    and search through the original dictionary for a hit.

    """
 
    #more_than_two = [ss for ss in anagram_squares if len(ss) > 2]
    #print(more_than_two[:10])

    #Generate dictionary of transformation_sequences:original_words
    transformations_to_word_pairs = {}
    for words in anagram_words:
        pairs_of_words = it.permutations(words, 2)
        for pair in pairs_of_words:
            transformations_to_word_pairs[transformations(pair[0], pair[1])] = pair
    #---------------------------------------------------------------

    largest_square = 0
    for squares in anagram_squares:
        pairs_of_squares = it.permutations(squares,2)
        for pair in pairs_of_squares:
            transformation_sequence = transformations(str(pair[0]), str(pair[1]))
            if transformation_sequence in transformations_to_word_pairs.keys():
                check = zip(str(pair[0]),transformations_to_word_pairs[transformation_sequence][0])
                C = defaultdict(list)
                for k,v in check:
                    C[k].append(v)
                if max([len(v) for v in C.values()]) == 1:
                    print(pair, transformations_to_word_pairs[transformation_sequence])
                    largest_entry = max(pair[0], pair[1])
                    largest_square = max(largest_square, largest_entry)
                    print(pair, transformations_to_word_pairs[transformation_sequence], largest_square)

    """ Okay, I made a mistake. I need to figure out a way to check that duplicate numbers correspond to duplicate letters, in both the
    original sequence and the transformed sequence. or vice versa.
    
    Because of the transformation sequence work I've already done, I know that the mapping from one to the other is solid. But what
    I'm not sure about is the number uniqueness. Does simply checking if they have the same number of unique characters work?

    
    Updated, now the solution works. A bit of a cock-up, but hey, whatever.
    -----
    Okay, lmao, I got totally lucky. I guessed that the answer was BROAD BOARD because that was the biggest number on my list that was acceptable.
    My work, as it stands, fails. But I still managed to get the right answer.
    -----
    """

    print(largest_square)

    #print(transformations_to_word_pairs.items())


    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()