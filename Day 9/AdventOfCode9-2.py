import numpy as np

def get_data():
    file_name = 'day9.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

def list_is_all_zeroes(ls):
    for itm in ls:
        if itm != 0:
            return False
    return True

userInput = get_data()
inputs = []
for line in userInput:
    inputs.append([int(i) for i in line.split(' ')])
differences = []

for i in range(0,len(inputs)):
    differences.append([inputs[i]])
    difIdx = 0
    while not list_is_all_zeroes(differences[i][difIdx]):
        differences[i].append([differences[i][difIdx][k+1]-differences[i][difIdx][k] for k in range(0,len(differences[i][difIdx])-1)])
        difIdx += 1

# answerVals = []
# for i in range(0, len(inputs)):
#     tempSum = 0
#     for j in range(0,len(differences[i])):
#         #print(differences[i][j][-1])
#         tempSum += differences[i][j][-1]
#     answerVals.append(tempSum)
# print(sum(answerVals))
#
outputs = differences.copy()
for i in range(0,len(outputs)):
    outputs[i].reverse()
    outputs[i][0].insert(0,0)

#print(outputs)
for i in range(0,len(outputs)):
    for j in range(1, len(outputs[i])):
        outputs[i][j].insert(0,outputs[i][j][0]-outputs[i][j-1][0])
#print(outputs)
lastVals = []
for i in range(0,len(outputs)):
    lastVals.append(outputs[i][-1][0])
print(sum(lastVals))
