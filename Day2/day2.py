def openFile(filename):
    
    f = open(filename, 'r')
    result = f.readlines()
    f.close()

    return result

def calculateHandScore1(me, opp):

    hands = {'A': 0, 'B': 1, 'C': 2,
             'X': 0, 'Y': 1, 'Z': 2}
    if hands[me] == hands[opp]:
        return hands[me] + 3 + 1
    elif hands[opp] == ((hands[me] + 1)%3):
        return hands[me] + 1
    else:
        return hands[me] + 6 + 1
    
def calculateHandScore2(me, opp):

    hands = {'A': 0, 'B': 1, 'C': 2}
    if me == 'X':
        # LOSE
        myHand = hands[opp] - 1
        if myHand == -1:
            myHand = 2
        return myHand + 1
    elif me == 'Y':
        # DRAW
        return hands[opp] + 3 + 1
    else:
        # WIN
        myHand = (hands[opp]+1)%3
        return myHand + 1 + 6

# Round 2 hands and scores
# A X 3
# A Y 4
# A Z 8
# B X 1
# B Y 5
# B Z 9
# C X 2
# C Y 6
# C Z 7

def calculateScores(input):
    myScore1 = 0
    myScore2 = 0

    for line in input:
        opp, me = line.split()
        myScore1 += calculateHandScore1(me, opp)

        score = calculateHandScore2(me, opp)
        myScore2 += score

    
    return myScore1, myScore2

def main():
    print(calculateScores(openFile('input.txt')))

main()





