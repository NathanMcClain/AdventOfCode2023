import numpy as np
import copy

def get_data():
    file_name = 'day14.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

def indices(lst, item):
    return int([i for i, x in enumerate(lst) if x == item][0])

def calculate_damage_in_position(board):
    damage = 0
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j] == 'O':
                damage += (len(board) - i)
    return damage

userInput = get_data()
cycle_max = 1000000000
positions_reached = []
damages = []
directions = ['north', 'west', 'south', 'east']
for i in range(0, cycle_max):
    for w in directions:
        if 'north' == w:
            for h in range(0,len(userInput)):
                has_moved = False
                for k in range(0,len(userInput)-1):
                    for l in range(0,len(userInput[0])):
                        if userInput[k][l] == '.' and userInput[k+1][l] == 'O':
                            topRow = list(userInput[k+1])
                            topRow[l] = '.'
                            userInput[k+1] = ''.join(topRow)
                            bottomRow = list(userInput[k])
                            bottomRow[l] = 'O'
                            userInput[k] = ''.join(bottomRow)
                            has_moved = True
                if not has_moved:
                    break
        if 'south' == w:
            for h in range(0,len(userInput)):
                has_moved = False
                for k in range(len(userInput)-1,0,-1):
                    for l in range(0,len(userInput[0])):
                        if userInput[k][l] == '.' and userInput[k-1][l] == 'O':
                            topRow = list(userInput[k])
                            topRow[l] = 'O'
                            userInput[k] = ''.join(topRow)
                            bottomRow = list(userInput[k-1])
                            bottomRow[l] = '.'
                            userInput[k-1] = ''.join(bottomRow)
                            has_moved = True
                if not has_moved:
                    break
        if 'east' == w:
            for h in range(0,len(userInput)):
                has_moved = False
                for k in range(len(userInput[0])-1,0,-1):
                    for l in range(0,len(userInput)):
                        if userInput[l][k] == '.' and userInput[l][k-1] == 'O':
                            rowList = list(userInput[l])
                            rowList[k] = 'O'
                            rowList[k-1] = '.'
                            userInput[l] = ''.join(rowList)
                            has_moved = True
                if not has_moved:
                    break
        if 'west' == w:
            for h in range(0,len(userInput)):
                has_moved = False
                for k in range(0,len(userInput[0])-1):
                    for l in range(0,len(userInput)):
                        if userInput[l][k] == '.' and userInput[l][k+1] == 'O':
                            rowList = list(userInput[l])
                            rowList[k] = 'O'
                            rowList[k+1] = '.'
                            userInput[l] = ''.join(rowList)
                            has_moved = True
                if not has_moved:
                    break
    cur_board = copy.deepcopy(userInput)
    if cur_board in positions_reached:
        cycle_length = i-int(indices(positions_reached,cur_board))
        break
    positions_reached.append(cur_board)
    damages.append(calculate_damage_in_position(cur_board))
offset = (cycle_max-indices(positions_reached,cur_board)-1) % cycle_length
sublist = damages[indices(positions_reached,cur_board):]
print(sublist[offset])
