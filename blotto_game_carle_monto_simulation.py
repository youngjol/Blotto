import random, math


#returns true if player 1 (A) wins, false if player 1 loses (player 2 wins) 
def player1WinsBlottoMatch(A, B):
    scoreA = 0
    scoreB = 0
    
    for i in range(0, 10):
        if A[i] == B[i]: 
            continue
        elif A[i] > B[i]:
            scoreA += i+1
            if scoreA >= 20: 
                return True
        else:
            scoreB += i+1
            if scoreB >= 20: 
                return False

    return scoreA > scoreB;
    
    
def randomAllocate100Soldiers():
    
    temp, B = [0] * 10, [0] * 10
    indices = list(range(10))
    currSum = 0
    
    for i in range(10):
        temp[i] = random.randint(0, 100-currSum)
        currSum += temp[i]
        if currSum == 100:
            break
    
    n = 0
    for i in range(10):
        index = random.randint(0, 9-n)
        numSoldiers = temp[indices.pop(index)]
        B[i] = numSoldiers
        n += 1
    
    return B
    
    
# Returns true if given entry guarantees a loss for player
def losingEntry(B):
    nonZeroBattles = 0
    for i in range(10):
        if B[i] != 0:
            nonZeroBattles += i+1    
    
    return nonZeroBattles < 20


# Allocate 100 soldiers s.t. player is not guaranteed to lose 
def smartAllocate100Soldiers():
    
    firstAlloc = True
    
    while firstAlloc or losingEntry(B):
        
        firstAlloc = False
                
        temp, B = [0] * 10, [0] * 10
        indices = list(range(10))
        currSum = 0
        
        for i in range(10):
            temp[i] = random.randint(0, 100-currSum)
            currSum += temp[i]
            if currSum == 100:
                break
        
        n = 0
        for i in range(10):
            index = random.randint(0, 9-n)
            numSoldiers = temp[indices.pop(index)]
            B[i] = numSoldiers
            n += 1
    
    return B


def player1Wins(A, numMatches):
    numWins = 0
    
    for i in range(numMatches):    
        B = smartAllocate100Soldiers()
        if player1WinsBlottoMatch(A, B):
            numWins += 1
    
    return numWins/numMatches
    
    