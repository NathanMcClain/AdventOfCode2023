import numpy as np
import math

def get_data():
    file_name = 'day8.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

def done(nodes_list):
    for each in nodes_list:
        if each[-1] != 'Z':
            return False
    return True

userInput = get_data()
instructions = userInput[0]
nodes = {}
for i in range(2, len(userInput)):
    nodes[userInput[i].split(' = ')[0]] = [userInput[i][7:10],userInput[i][12:15]]

#print(nodes)
steps = 0
allNodes = list(nodes.keys())

curNodes = [i for i in allNodes if i[-1] == 'A']
stepsNeeded = []
for eachStart in curNodes:
    curNode = eachStart
    steps = 0
    while not done([curNode]):
        nextIdx = -1
        if instructions[steps%len(instructions)] == 'L':
            nextIdx = 0
        else:
            nextIdx = 1

        curNode = nodes[curNode][nextIdx]
        #curNodes[i] = nodes[curNodes[i]][nextIdx]
        steps += 1
    stepsNeeded.append(steps)
print(math.lcm(*stepsNeeded))
