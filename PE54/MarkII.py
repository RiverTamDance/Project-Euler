# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 21:14:49 2020

@author: Taylor
"""

#PE54 Poker hands

#https://stackoverflow.com/questions/1198777/double-iteration-in-list-comprehension

# First off, lets read in the data.

import pandas as pd
import operator
import collections

df = pd.read_csv('p054_poker.txt',header=None, engine = 'python',
                 sep = r"(?<=^.. .. .. .. ..) ", names = ["p1hand","p2hand"])

# For 'high card' situations, we basically need to sort the hands into highest to
# lowest order. Then essentially the high card comparison is natural. The other main
# issue is the use of letters and numbers to designate card 'value'. I guess there
# are a few options here. I can actually change the value of each letter into a 
# number. or I could create some kind of dictionary and reference that whenever 
# I need to. As far as i can tell, this seems easiest to do the 'hardcode' way.
#T = 10
#J = 11
#Q = 12
#K = 13
#A = 14
#S
#C
#H
#D

def handCleaner(hand):
    
    #Overall this is the 'housekeeping' function. finessing things the way
    #they should be. Data cleaning and pre-processing.
    
    #Change face cards letter to their value
    hand = hand.replace('A','14')
    hand = hand.replace('K','13')
    hand = hand.replace('Q','12')
    hand = hand.replace('J','11')
    hand = hand.replace('T','10')
    
    #create list of tuples, each tuple being a card. e.g (value, suit). note that
    # I turned the 'value' into an integer.
    cards = hand.split()
    handTuple = [(int(card[0:-1]),card[-1]) for card in cards]
    
    #sort list of tuples based on card value (1st element)
    handTuple = sorted(handTuple, key = operator.itemgetter(0), reverse=True)
    
    return(handTuple)

def seqMaker(handTuple):
    seq = [handTuple[i][0] for i in range(0,5)]
    return(seq)

def diffSeq(seq1,seq2):
    diffList = list(map(operator.sub,seq1,seq2))
    return(diffList)

#--------------- above are data prep function, below are domain specific functions

def flush(hand):
    
    cards = hand.split()
    boolResult = all(card[-1] == cards[0][-1] for card in cards[1:5])

    return(boolResult)

def straight(hand):
    
    straightBool = False
    handDiff = list(map(operator.sub, hand[:-1], hand[1:]))
    
    if all(cardDiff == 1 for cardDiff in handDiff):
        straightBool = True
    elif hand == [14,5,4,3,2]:
        straightBool = True

    return(straightBool)

def repeatCards(hand):
    
    handCounter = collections.Counter(hand)
    repeatCardTuples = [cards for cards in list(handCounter.items()) if cards[-1] > 1]

    return(repeatCardTuples)

def straightFlush(flushBool, seqBool):
    
    straightFlushBool = False
    
    if flushBool == True and seqBool == True:
        straightFlushBool = True
        
    return(straightFlushBool)

## ---------------put it all together into the WhoWon function, which is basically a ton of if statements. because i knew
## -------------- I wouldn't have to deal with certain types of ties, this does not work for the general case.

def WhoWon(p1hand_tuple, p2hand_tuple, p1_val_seq, p2_val_seq, diffList, p1_Flush, p2_Flush, p1_Straight, p2_Straight,
           p1_CardRepeats, p2_CardRepeats, p1_StrFlush, p2_StrFlush):
    ## 0 := tie, 1 := p1 win, 2:= p2 win, 3 := unassigned 
    winner = 3
    
    p1CardMultiples = [n for (c,n) in p1_CardRepeats]
    p2CardMultiples = [n for (c,n) in p2_CardRepeats]
    
    FH = [2,3]
    
    ## check for straight flush
    if p1_StrFlush==True and p2_StrFlush==False:
        winner = 1
    elif p1_StrFlush==False and p2_StrFlush==True:
        winner = 2
    elif p1_StrFlush==True and p2_StrFlush==True:
        winner = 0
    
    ## check for four of a kind
    if winner == 3:
        if 4 in p1CardMultiples and 4 not in p2CardMultiples:
            winner = 1
        elif 4 not in p1CardMultiples and 4 in p2CardMultiples:
            winner = 2
        elif 4 in p1CardMultiples and 4 in p2CardMultiples:
            winner = 0
    
    ## check for full house
    if winner == 3:
        if set(FH) == set(p1CardMultiples) and set(FH) != set(p2CardMultiples):
            winner = 1
        if set(FH) != set(p1CardMultiples) and set(FH) == set(p2CardMultiples):
            winner = 2
        if set(FH) == set(p1CardMultiples) and set(FH) == set(p2CardMultiples):
            winner = 0
    
    ## check for flush
    if winner == 3:
        if p1_Flush and not p2_Flush:
            winner = 1
        if not p1_Flush and p2_Flush:
            winner = 2
        if p1_Flush and p2_Flush:
            winner = 0
    
    ## check for straight
    if winner == 3:
        if p1_Straight and not p2_Straight:
            winner = 1
        if not p1_Straight and p2_Straight:
            winner = 2
        if p1_Straight and p2_Straight:
            winner = 0
        
    ## check for three of a kind
    if winner == 3:
        if 3 in p1CardMultiples and 3 not in p2CardMultiples:
            winner = 1
        elif 3 not in p1CardMultiples and 3 in p2CardMultiples:
            winner = 2
        elif 3 in p1CardMultiples and 3 in p2CardMultiples:
            winner = 0
            
    ## check for two pair
    ##IDK how strongly I believe in this code.
    if winner == 3:
        if [2,2] == p1CardMultiples and [2,2] != p2CardMultiples:
            winner = 1
        elif [2,2] != p1CardMultiples and [2,2] == p2CardMultiples:
            winner = 2
        elif [2,2] == p1CardMultiples and [2,2] == p2CardMultiples:
            winner = 0
        
    ##check for two of a kind
    if winner == 3:
        if 2 in p1CardMultiples and 2 not in p2CardMultiples:
            winner = 1
        elif 2 not in p1CardMultiples and 2 in p2CardMultiples:
            winner = 2
        elif 2 in p1CardMultiples and 2 in p2CardMultiples:
            
            ## here we resolve tied pairs, which appears to be the only ties so 
            
            p1PairValue = p1_CardRepeats[0][0]
            p2PairValue = p2_CardRepeats[0][0]
            
            if p1PairValue > p2PairValue:
                winner = 1
            elif p1PairValue < p2PairValue:
                winner = 2
            elif p1PairValue == p2PairValue:
                
                HC = next(filter(lambda x: x!=0, diffList))
        
                if HC > 0:
                    winner = 1
                elif HC < 0:
                    winner = 2
                else:
                    # I think this is a true tie
                    winner = 0
                
    ## check for high card
    if winner == 3:
        ## next simply gets the 'next' item in an iterator.
        HC = next(filter(lambda x: x!=0, diffList))
        
        if HC > 0:
            winner = 1
        elif HC < 0:
            winner = 2
        else:
            # I think this is a true tie
            winner = 0
        
        
    return(winner)

#Here I transform the dataframe into what should hopefully be the end result.

df['p1hand_tuple'] = df['p1hand'].apply(handCleaner)
df['p2hand_tuple'] = df['p2hand'].apply(handCleaner)
df['p1_val_seq'] = df['p1hand_tuple'].apply(seqMaker)
df['p2_val_seq'] = df['p2hand_tuple'].apply(seqMaker)
df['p1-p2 seq'] = df.apply(lambda x: diffSeq(x['p1_val_seq'],x['p2_val_seq']),axis=1)
df["p1_Flush"] = df['p1hand'].apply(flush) 
df["p2_Flush"] = df['p2hand'].apply(flush)
df['p1_Straight'] = df["p1_val_seq"].apply(straight)
df['p2_Straight'] = df["p2_val_seq"].apply(straight)
df['p1_CardRepeats'] = df['p1_val_seq'].apply(repeatCards)
df['p2_CardRepeats'] = df['p2_val_seq'].apply(repeatCards)
df['p1_StrFlush'] = df.apply(lambda x: straightFlush(x['p1_Flush'],x['p1_Straight']),axis=1)
df['p2_StrFlush'] = df.apply(lambda x: straightFlush(x['p2_Flush'],x['p2_Straight']),axis=1)
df['winner'] = df.apply(lambda x: WhoWon(x['p1hand_tuple'], x['p2hand_tuple'], x['p1_val_seq'], x['p2_val_seq'], 
                                         x['p1-p2 seq'], x['p1_Flush'], x['p2_Flush'], x['p1_Straight'], x['p2_Straight'],
                                         x['p1_CardRepeats'], x['p2_CardRepeats'], x['p1_StrFlush'], x['p2_StrFlush']),axis = 1)

df_p1_wins = df.loc[df['winner'] == 1]
