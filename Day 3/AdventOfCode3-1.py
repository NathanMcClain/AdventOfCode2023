import numpy as np

def get_data():
    file_name = 'day3.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

userInput = get_data()
totalLen = len(userInput) * len(userInput[0])
allBuf = [''] * totalLen
lineOffset = len(userInput[0])
rightOffset = 1
lineNum = 0
lineVals = []
sum = 0
for line in userInput:
    line = line.replace('$', '*')
    line = line.replace('@', '*')
    line = line.replace('#', '*')
    line = line.replace('+', '*')
    line = line.replace('=', '*')
    line = line.replace('-', '*')
    line = line.replace('%', '*')
    line = line.replace('/', '*')
    line = line.replace('&', '*')
    userInput[lineNum] = line
    for i in range(0,len(line)):
        allBuf[lineNum*len(userInput[0]) + i] = line[i]
    lineNum += 1
start_stop = []
pair_idx = 0
offsets = [-lineOffset - 1, -lineOffset, -lineOffset+1, -1, 1, lineOffset-1, lineOffset, lineOffset+1]
for i in range(0,len(allBuf)):
    if allBuf[i] in "0123456789":
        if len(start_stop) == pair_idx:
            #beginning of a new num
            start_stop.append([i])
    elif len(start_stop) > 0 and len(start_stop) == pair_idx +1 and len(start_stop[pair_idx]) == 1:
        #found the end, mark the previous spot as end
        start_stop[pair_idx].append(i-1)
        pair_idx += 1
#NOTE: start_stop is a list of all the start and stop indexes of all the numbers in the grid
for i in range(0, len(allBuf)):
    if allBuf[i] == '*':
        for offSet in offsets:
            if i + offSet >= 0 and allBuf[i+offSet].isdigit():
                for j in range(0, len(start_stop)):
                    if i+offSet >= start_stop[j][0] and i+offSet <= start_stop[j][1]:
                        numStr = ''
                        for numInRange in range(int(start_stop[j][0]), int(start_stop[j][1])+1):
                            numStr += allBuf[numInRange]
                        #print(numStr)
                        sum += int(numStr)
                        start_stop.pop(j)
                        break
print(sum)
