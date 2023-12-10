import numpy as np
from matplotlib.path import Path

def get_data():
    file_name = 'day10.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

userInput = get_data()
grid = []
s_idx = ()
for i in range(0, len(userInput)):
    grid.append(userInput[i])

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] == 'S':
            s_idx = (i,j)
connected = []
for i in range(0, len(grid)):
    connected.append([])
    for j in range(0, len(grid[i])):
        connected[i].append([])

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] == '|':
            if i != 0:
                connected[i-1][j].append((i,j))
            if i != len(grid)-1:
                connected[i+1][j].append((i,j))
        if grid[i][j] == '-':
            if j != 0:
                connected[i][j-1].append((i,j))
            if j != len(grid[i])-1:
                connected[i][j+1].append((i,j))
        if grid[i][j] == 'L':
            if j != len(grid[i]) - 1:
                connected[i][j+1].append((i,j))
            if i != 0:
                connected[i-1][j].append((i,j))
        if grid[i][j] == 'J':
            if i != 0:
                connected[i-1][j].append((i,j))
            if j != 0:
                connected[i][j-1].append((i,j))
        if grid[i][j] == '7':
            if j != 0:
                connected[i][j-1].append((i,j))
            if i != len(grid) - 1:
                connected[i+1][j].append((i,j))
        if grid[i][j] == 'F':
            if i != len(grid) - 1:
                connected[i+1][j].append((i,j))
            if j != len(grid[i]) - 1:
                connected[i][j+1].append((i,j))
        if grid[i][j] == 'S':
            if i != 0:
                connected[i-1][j].append((i,j))
            if j != 0:
                connected[i][j-1].append((i,j))
            if i != len(grid) - 1:
                connected[i+1][j].append((i,j))
            if j != len(grid[i]) - 1:
                connected[i][j+1].append((i,j))

for i in range(0,len(grid)):
    for j in range(0,len(grid[i])):
        if grid[i][j] == '.':
            connected[i][j] = []

for i in range(0,len(grid)):
    for j in range(0,len(grid[i])):
        coords_to_remove = []
        for coord in connected[i][j]:
            if (i,j) not in connected[coord[0]][coord[1]]:
                coords_to_remove.append(coord)
        connected[i][j] = [k for k in connected[i][j] if k not in coords_to_remove]
for i in range(0,len(grid)):
    for j in range(0,len(grid[i])):
        if len(connected[i][j]) == 1:
            connected[i][j] = []

connected_updated = connected.copy()
path = []
path.append(s_idx)

while (path[-1] != s_idx or len(path) == 1):
    for r in connected_updated[path[-1][0]][path[-1][1]]:
        if r not in path or (r == s_idx and len(path) > 2):
            connected_updated[path[-1][0]][path[-1][1]].remove(r)
            path.append(r)
            break

#need to replace S with the actual shape
s_connects_north = False
s_connects_south = False
s_connects_east = False
s_connects_west = False
first_node = path[1]
last_node = path[-2]
if first_node[0] == s_idx[0]:
    if first_node[1] == s_idx[1] + 1:
        s_connects_south = True
    if first_node[1] == s_idx[1] - 1:
        s_connects_north = True
if first_node[1] == s_idx[1]:
    if first_node[0] == s_idx[0] + 1:
        s_connects_east = True
    if first_node[1] == s_idx[0] - 1:
        s_connects_west = True

if last_node[0] == s_idx[0]:
    if last_node[1] == s_idx[1] + 1:
        s_connects_south = True
    if last_node[1] == s_idx[1] - 1:
        s_connects_north = True
if last_node[1] == s_idx[1]:
    if last_node[0] == s_idx[0] + 1:
        s_connects_east = True
    if last_node[1] == s_idx[0] - 1:
        s_connects_west = True
s_pipe = ''
if s_connects_north:
    if s_connects_south:
        s_pipe = '|'
    elif s_connects_east:
        s_pipe = 'L'
    elif s_connects_west:
        s_pipe = 'J'
elif s_connects_south:
    if s_connects_east:
        s_pipe = 'F'
    elif s_connects_west:
        s_pipe = '7'
elif s_connects_east and s_connects_west:
    s_pipe = '-'
grid[s_idx[0]] = grid[s_idx[0]].replace('S',s_pipe)

library_enclosed = 0
p = Path(path)
lib_enclosed = []
for i in range(0,len(grid)):
    for j in range(0,len(grid[0])):
        if (i,j) not in path:
            if p.contains_point((i,j)):
                library_enclosed += 1
                lib_enclosed.append((i,j))

print(library_enclosed)
