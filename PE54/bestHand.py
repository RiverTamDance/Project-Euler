def lilVerter(arg1):
    if arg1 == 'T':
        return '10'
    if arg1 == 'J':
        return '11'
    if arg1 == 'Q':
        return '12'
    if arg1 == 'K':
        return '13'
    if arg1 == 'A':
        return '14'
    else:
        return arg1
    
def bestHand(arg1):
    
    cards = arg1.split()

    values = sorted([int(lilVerter(x[0])) for x in cards],reverse = True)  

    score = 0

    #check for multiples
    
    dubs = False
    dubdubs = False
    trips = False
    boat = False
    quads = False
    
    for x in [0,1,2,3]:
        if values[x] == values[x+1] and values[x-1] != values[x]:
            if dubs == True:
                dubdubs = True
                score = 3
            else: 
                dubs = True
                score = 2
            
    if dubs == True:
        for x in [0,1,2]:
            if values[x] == values[x+1] == values[x+2]:
                trips = True
                score = 4
                
    if (dubdubs == True) and (trips == True):
        boat = True
        score = 7

    if trips == True:
        for x in [0,1]:
            if values[x] == values[x+1] == values[x+2] == values[x+3]:
                quads = True
                score = 8

    #check for straight

    print(values)
    
    if values[0]==(values[1]+1)==(values[2]+2)==(values[3]+3)==(values[4]+4):
        score = 5
    else:
        if values[0]==14 and values[1]==5 and values[2]==4 and values[3]==3 and values[4]==2:
            score = 5

    #Check for flush

    if arg1[1:2] == arg1[4:5] == arg1[7:8] == arg1[10:11] == arg1[13:14]:
        flush = True
    else:
        flush = False

    if flush == True:
        if score == 5:
            if values[1]==13:
                score = 10
            else:
                score = 9
        else: 
            score=6
    else:
        score = 1
        
    return(score)
    
            

    
