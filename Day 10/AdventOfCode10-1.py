import numpy as np

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
    for j in range(0, len(grid)):
        if grid[i][j] == 'S':
            s_idx = (i,j)
connected = []
for i in range(0, len(grid)):
    connected.append([])
    for j in range(0, len(grid)):
        connected[i].append([])

for i in range(0, len(grid)):
    for j in range(0, len(grid)):
        if grid[i][j] == '|':
            if i != 0:
                connected[i-1][j].append((i,j))
            if i != len(grid)-1:
                connected[i+1][j].append((i,j))
        if grid[i][j] == '-':
            #print((i,j))
            if j != 0:
                #print('connected',(i,j),'to',(i-1,j))
                connected[i][j-1].append((i,j))
            if j != len(grid)-1:
                #print('connected',(i,j),'to',(i+1,j))
                connected[i][j+1].append((i,j))
        if grid[i][j] == 'L':
            if j != len(grid) - 1:
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
            if j != len(grid) - 1:
                connected[i][j+1].append((i,j))
        if grid[i][j] == 'S':
            if i != 0:
                connected[i-1][j].append((i,j))
            if j != 0:
                connected[i][j-1].append((i,j))
            if i != len(grid) - 1:
                connected[i+1][j].append((i,j))
            if j != len(grid) - 1:
                connected[i][j+1].append((i,j))

for i in range(0,len(grid)):
    for j in range(0,len(grid)):
        if grid[i][j] == '.':
            connected[i][j] = []
for i in range(0,len(grid)):
    for j in range(0,len(grid)):
        coords_to_remove = []
        for coord in connected[i][j]:
            if (i,j) not in connected[coord[0]][coord[1]]:
                coords_to_remove.append(coord)
        connected[i][j] = [k for k in connected[i][j] if k not in coords_to_remove]
for i in range(0,len(grid)):
    for j in range(0,len(grid)):
        if len(connected[i][j]) == 1:
            connected[i][j] = []

connected_updated = connected.copy()
path = []
path.append(s_idx)

# for i in range(0,len(connected_updated)):
#     print(connected_updated[i])
#print(path)
steps = 0
#print(connected_updated[path[-1][0]][path[-1][1]])
while (path[-1] != s_idx or len(path) == 1):
    #print(path)
    #print(len(connected_updated[path[-1][0]][path[-1][1]]))
    #print(connected_updated[path[-1][0]][path[-1][1]])
    #print('options',connected_updated[path[-1][0]][path[-1][1]])
    for r in connected_updated[path[-1][0]][path[-1][1]]:
        #print(r)
        if r not in path or r == s_idx:
            connected_updated[path[-1][0]][path[-1][1]].remove(r)
            path.append(r)
            break
    steps += 1
#print(path)
print(steps/2)
