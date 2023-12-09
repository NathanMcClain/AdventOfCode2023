import numpy as np

def get_data():
    file_name = 'day8.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

userInput = get_data()
instructions = userInput[0]
nodes = {}
for i in range(2, len(userInput)):
    nodes[userInput[i].split(' = ')[0]] = [userInput[i][7:10],userInput[i][12:15]]

#print(nodes)
steps = 0
curNode = 'AAA'
while curNode != 'ZZZ':
    nextIdx = -1
    if instructions[steps%len(instructions)] == 'L':
        nextIdx = 0
    else:
        nextIdx = 1
    curNode = nodes[curNode][nextIdx]
    steps += 1
print(steps)
