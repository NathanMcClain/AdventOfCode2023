import numpy as np
import copy
import heapq
import sys

def get_data():
    file_name = 'day17.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

userInput = get_data()
grid = []
direction = -1 #up is 0, right is 1, down is 2, left is 3
next_offset = [[-1,0],[0,1],[1,0],[0,-1]]
starting_idx = [0,0]
heat_lost = []
destination_idx = [len(userInput)-1,len(userInput[0])-1]
for i in range(0,len(userInput)):
    grid.append(userInput[i])
    heat_lost.append([])

for i in range(0,len(userInput)):
    for j in range(0,len(userInput[0])):
        heat_lost[i].append(sys.maxsize)
heat_lost[0][0] = 0
num_in_direction = 0
path = [[0,0]]
q = [[heat_lost[0][0],starting_idx[0],starting_idx[1],direction,num_in_direction,path]]
#We start in the top left corner
seen = set()
least_heat = sys.maxsize
shortest_path = []
count_added_to_q = 0
while q:
    #print('inside while')
    # if( count_added_to_q % 10000 == 0):
    #     print(count_added_to_q,'searched')
    curData = heapq.heappop(q)
    curHeatLost = curData[0]
    curRow = curData[1]
    curCol = curData[2]
    curDirection = curData[3]
    curNumInDirection = curData[4]
    curPath = curData[5]
    if (curRow,curCol,curDirection,curNumInDirection) in seen:
        continue
    seen.add((curRow,curCol,curDirection,curNumInDirection))
    #print('path',curPath)
    if curRow == destination_idx[0] and curCol == destination_idx[1] and curHeatLost < least_heat:
        least_heat = curHeatLost
        shortest_path = copy.deepcopy(curPath)
        #print('found it', curHeatLost)
        #print('found path',curPath)
    #on the first iteration, we start in the top left so you can either go right or down
    if curDirection == -1:
        possibleDirections = [1,2]
    else:
        possibleDirections = [(curDirection + 1)%4,(curDirection-1+4)%4]
    if curNumInDirection < 3 and 0 <= curRow + next_offset[curDirection][0] < len(grid) and 0 <= curCol + next_offset[curDirection][1] < len(grid[0]):
        possibleDirections.append(curDirection)
    #print('curDirection',curDirection,'possible new directions',possibleDirections)
    for eachpossibleDirection in possibleDirections:
        newRow = curRow + next_offset[eachpossibleDirection][0]
        newCol = curCol + next_offset[eachpossibleDirection][1]
        if 0 <= newRow < len(grid):
            if 0 <= newCol < len(grid[0]):
                newHeatLoss = curHeatLost + int(grid[newRow][newCol])
                #if newHeatLoss < heat_lost[newRow][newCol]:
                heat_lost[newRow][newCol] = newHeatLoss
                newPath = copy.deepcopy(curPath)
                #print('copy path',newPath)
                newPath.append([newRow,newCol])
                newNumInDirection = curNumInDirection + 1 if eachpossibleDirection == curDirection else 1
                if not ((newRow,newCol,eachpossibleDirection,newNumInDirection) in seen):
                    heapq.heappush(q,[newHeatLoss,newRow,newCol,eachpossibleDirection,newNumInDirection,newPath])


print('Least heat loss', least_heat)
# print('shortest path', shortest_path)
# calculated_loss = 0
# for i in range(0,len(grid)):
#     line = ''
#     for j in range(0,len(grid[0])):
#         if [i,j] in shortest_path:
#             line += '.'
#             if not(i == 0 and j == 0):
#                 calculated_loss += int(grid[i][j])
#         else:
#             line += grid[i][j]
#     print(line)
# print(calculated_loss)
