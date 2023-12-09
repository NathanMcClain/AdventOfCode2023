import numpy as np

def get_data():
    file_name = 'day7.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

def get_type(handOfNums):
    dict = {}
    for eachCard in handOfNums:
        if eachCard in dict.keys():
            dict[eachCard] += 1
        else:
            dict[eachCard] = 1
    counts = list(dict.values())
    counts.sort()
    counts.reverse()
    if counts[0] == 5:
        return 7
    elif counts[0] == 4:
        return 6
    elif counts[0] == 3 and counts[1] == 2:
        return 5
    elif counts[0] == 3 and counts[1] == 1:
        return 4
    elif counts[0] == 2 and counts[1] == 2:
        return 3
    elif counts[0] == 2 and counts[1] == 1:
        return 2
    elif counts[0] == 1:
        return 1

def first_wins_tie(hand1, hand2):
    for i in range(0,len(hand1)):
        if hand1[i] > hand2[i]:
            #print('first hand wins because of idx',i,'with value',hand1[i])
            return True
        elif hand1[i] < hand2[i]:
            #print('second hand wins because of idx',i,'with value',hand2[i])
            return False

userInput = get_data()
handsStr = []
bids = []
for line in userInput:
    handsStr.append([*line.split(' ')[0]])
    bids.append(int(line.split(' ')[1]))
handsUnsorted = []
for eachHand in handsStr:
    curHand = []
    for eachCard in eachHand:
        if eachCard.isdigit():
            curHand.append(int(eachCard))
        elif eachCard == 'A':
            curHand.append(14)
        elif eachCard == 'K':
            curHand.append(13)
        elif eachCard == 'Q':
            curHand.append(12)
        elif eachCard == 'J':
            curHand.append(11)
        elif eachCard == 'T':
            curHand.append(10)
    handsUnsorted.append(curHand)
handsSorted = []

for eachHand in handsUnsorted:
    handCopy = eachHand.copy()
    handCopy.sort()
    handCopy.reverse()
    handsSorted.append(handCopy)

types = []
for eachHand in handsSorted:
    types.append(get_type(eachHand))

ranks = []
for i in range(0,len(types)):
    countHigher = 0
    countLower = 0
    for j in range(0,len(types)):
        if i != j:
            #comparing hands that aren't itself
            #print(i,j)
            if types[i] > types[j]:
                #print('hand',i,'beats hand',j)
                countLower += 1
            elif types[i] < types[j]:
                #print('hand',i,'loses to hand',j)
                countHigher += 1
            else:
                if first_wins_tie(handsUnsorted[i],handsUnsorted[j]):
                    #print('hand',i,'beats hand',j,'in a tie')
                    countLower += 1
                else:
                    #print('hand',i,'loses to hand',j,'in a tie')
                    countHigher += 1
    ranks.append(countLower+1)
total_winnings = 0
for i in range(0, len(ranks)):
    total_winnings += ranks[i] * bids[i]
hands_in_rank_order = [0] * len(ranks)

for i in range(0, len(ranks)):
    hands_in_rank_order[ranks[i]-1] = handsUnsorted[i]
#print(handsUnsorted)
# for hand in hands_in_rank_order:
#     print(hand)
print(total_winnings)
