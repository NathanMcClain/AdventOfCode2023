import numpy as np

def get_data():
    file_name = 'day4.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

userInput = get_data()
cardNums = len(userInput)
totalPoints = 0
for card in userInput:
    cardPoints = 0.5
    numsStr = card.split(':')[1]
    winningNumsStr = numsStr.split('|')[0].split(' ')
    myNumsStr = numsStr.split('|')[1].split(' ')
    winningNumsStr = [i for i in winningNumsStr if i != '']
    winningNums = [int(i) for i in winningNumsStr ]
    myNumsStr = [i for i in myNumsStr if i != '']
    myNums = [int(i) for i in myNumsStr ]
    for eachWinningNum in winningNums:
        if eachWinningNum in myNums:
            cardPoints = int(cardPoints*2)
    if cardPoints >= 1:
        totalPoints += cardPoints
print(totalPoints)
