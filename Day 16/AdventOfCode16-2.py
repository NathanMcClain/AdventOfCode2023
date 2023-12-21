import numpy as np
import copy

def get_data():
    file_name = 'day16.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

def in_grid(point,gridHeight,gridWidth):
    if point[0] < 0 or point[0] >= gridHeight:
        return False
    if point[1] < 0 or point[1] >= gridWidth:
        return False
    return True

def at_least_one_still_going(current_rays):
    for ray in current_rays:
        if ray == True:
            return True
    return False

userInput = get_data()
grid = []
for i in range(0,len(userInput)):
    grid.append(userInput[i])
next_offset = [[-1,0],[0,1],[1,0],[0,-1]]
grid_height = len(userInput)
grid_width = len(userInput[0])
energized_counts = []
has_split = {}
possible_start_locations = []
possible_start_directions = []
for i in range(0,grid_height):
    possible_start_locations.append([i,0])
    possible_start_directions.append(1)
    possible_start_locations.append([i,grid_width-1])
    possible_start_directions.append(3)
for j in range(0,grid_width):
    possible_start_locations.append([0,j])
    possible_start_directions.append(2)
    possible_start_locations.append([grid_height-1,j])
    possible_start_directions.append(0)

for k in range(0,len(possible_start_locations)):
    still_going = []
    still_going.append(True)
    paths = []
    paths.append([])
    paths[0].append(possible_start_locations[k])
    directions = []
    directions.append(possible_start_directions[k])
    has_split = {}
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if grid[i][j] == '|' or grid[i][j] == '-':
                has_split[(i,j)] = False
    while at_least_one_still_going(still_going):
        for i in range(0,len(paths)):
            if still_going[i] == False:
                continue
            if grid[paths[i][-1][0]][paths[i][-1][1]] == '.':
                #Keep moving in the same direction
                possible_new_point = [paths[i][-1][0] + next_offset[directions[i]][0],paths[i][-1][1] + next_offset[directions[i]][1]]
                if in_grid(possible_new_point,grid_height,grid_width):
                    paths[i].append(possible_new_point)
                else:
                    still_going[i] = False
            elif grid[paths[i][-1][0]][paths[i][-1][1]] == '/':
                if directions[i] == 0:
                    directions[i] = 1
                elif directions[i] == 1:
                    directions[i] = 0
                elif directions[i] == 2:
                    directions[i] = 3
                elif directions[i] == 3:
                    directions[i] = 2
                possible_new_point = [paths[i][-1][0] + next_offset[directions[i]][0],paths[i][-1][1] + next_offset[directions[i]][1]]
                if in_grid(possible_new_point,grid_height,grid_width):
                    paths[i].append(possible_new_point)
                else:
                    still_going[i] = False
            elif grid[paths[i][-1][0]][paths[i][-1][1]] == '\\':
                if directions[i] == 0:
                    directions[i] = 3
                elif directions[i] == 1:
                    directions[i] = 2
                elif directions[i] == 2:
                    directions[i] = 1
                elif directions[i] == 3:
                    directions[i] = 0
                possible_new_point = [paths[i][-1][0] + next_offset[directions[i]][0],paths[i][-1][1] + next_offset[directions[i]][1]]
                if in_grid(possible_new_point,grid_height,grid_width):
                    paths[i].append(possible_new_point)
                else:
                    still_going[i] = False
            elif grid[paths[i][-1][0]][paths[i][-1][1]] == '-' : # | character
                if directions[i] == 0 or directions[i] == 2:
                    if has_split[(paths[i][-1][0],paths[i][-1][1])] == True:
                        still_going[i] = False
                        continue
                    has_split[(paths[i][-1][0],paths[i][-1][1])] = True
                    #going up or down, so split left and right
                    possible_new_point_left = [paths[i][-1][0] + next_offset[3][0],paths[i][-1][1] + next_offset[3][1]]
                    is_left_valid = False
                    is_right_valid = False
                    if in_grid(possible_new_point_left,grid_height,grid_width):
                        is_left_valid = True
                    possible_new_point_right = [paths[i][-1][0] + next_offset[1][0],paths[i][-1][1] + next_offset[1][1]]
                    if in_grid(possible_new_point_right,grid_height,grid_width):
                        is_right_valid = True
                    if is_left_valid and not is_right_valid:
                        paths[i].append(possible_new_point_left)
                        directions[i] = 3
                    elif is_right_valid and not is_left_valid:
                        paths[i].append(possible_new_point_right)
                        directions[i] = 1
                    elif not is_right_valid and not is_left_valid:
                        still_going[i] = False
                    else:
                        #both are valid
                        paths[i].append(possible_new_point_left)
                        directions[i] = 3
                        newPath = [possible_new_point_right]
                        paths.append(newPath)
                        directions.append(1)
                        still_going.append(True)
                else:
                    #going left or right, so just keep going
                    possible_new_point = [paths[i][-1][0] + next_offset[directions[i]][0],paths[i][-1][1] + next_offset[directions[i]][1]]
                    if in_grid(possible_new_point,grid_height,grid_width):
                        paths[i].append(possible_new_point)
                    else:
                        still_going[i] = False
            elif grid[paths[i][-1][0]][paths[i][-1][1]] == '|':
                if directions[i] == 1 or directions[i] == 3:
                    if has_split[(paths[i][-1][0],paths[i][-1][1])] == True:
                        still_going[i] = False
                        continue
                    has_split[(paths[i][-1][0],paths[i][-1][1])] = True
                    #going left or right, so split up and down
                    possible_new_point_up = [paths[i][-1][0] + next_offset[0][0],paths[i][-1][1] + next_offset[0][1]]
                    is_up_valid = False
                    is_down_valid = False
                    if in_grid(possible_new_point_up,grid_height,grid_width):
                        is_up_valid = True
                    possible_new_point_down = [paths[i][-1][0] + next_offset[2][0],paths[i][-1][1] + next_offset[2][1]]
                    if in_grid(possible_new_point_down,grid_height,grid_width):
                        is_down_valid = True
                    if is_up_valid and not is_down_valid:
                        paths[i].append(possible_new_point_up)
                        directions[i] = 0
                    elif is_down_valid and not is_up_valid:
                        paths[i].append(possible_new_point_down)
                        directions[i] = 2
                    elif not is_up_valid and not is_down_valid:
                        still_going[i] = False
                    else:
                        #both are valid
                        paths[i].append(possible_new_point_up)
                        directions[i] = 0
                        newPath = [possible_new_point_down]
                        paths.append(newPath)
                        directions.append(2)
                        still_going.append(True)
                else:
                    #going up or down, so just keep going
                    possible_new_point = [paths[i][-1][0] + next_offset[directions[i]][0],paths[i][-1][1] + next_offset[directions[i]][1]]
                    if in_grid(possible_new_point,grid_height,grid_width):
                        paths[i].append(possible_new_point)
                    else:
                        still_going[i] = False

    energized_grid = []
    for i in range(0,grid_height):
        energized_grid.append([])
        for j in range(0,grid_width):
            energized_grid[i].append(0)

    for i in range(0,len(paths)):
        for j in range(0,len(paths[i])):
            energized_grid[paths[i][j][0]][paths[i][j][1]] += 1

    energized_count = 0
    for i in range(0,len(energized_grid)):
        for j in range(0,len(energized_grid[i])):
            if energized_grid[i][j] > 0:
                energized_count += 1
    energized_counts.append(energized_count)

#print(energized_counts)
print(max(energized_counts))
