import numpy as np
import copy

def get_data():
    file_name = 'day11.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

userInput = get_data()
small_universe = []
for i in range(0,len(userInput)):
    small_universe.append([])
    for j in range(0,len(userInput[i])):
        small_universe[i].append(userInput[i][j])
blank_rows = []
blank_cols = []
single_blank_row = []

for i in range(0,len(small_universe)):
    if not '#' in small_universe[i]:
        single_blank_row = copy.deepcopy(small_universe[i])
        blank_rows.append(i)
blank_rows.reverse()

for j in range(0,len(small_universe[0])):
    col_has_hash = False
    for i in range(0,len(small_universe)):
        if small_universe[i][j] == '#':
            col_has_hash = True
            break
    if not col_has_hash:
        blank_cols.append(j)

blank_cols.reverse()

galaxy_idx = 1
locations = {}
for i in range(0,len(small_universe)):
    for j in range(0,len(small_universe[i])):
        if small_universe[i][j] == '#':
            small_universe[i][j] = str(galaxy_idx)
            locations[galaxy_idx] = (i,j)
            galaxy_idx += 1

distances = {}
for i in range(1,galaxy_idx):
    for j in range(i+1,galaxy_idx):
        if i != j:
            distances[(i,j)] = 0

blank_row_val = (1000000 - 1)

total_blank_cols_covered = 0
total_blank_rows_covered = 0

for key in list(distances.keys()):
    first_galaxy = key[0]
    second_galaxy = key[1]
    first_loc = locations[first_galaxy]
    second_loc = locations[second_galaxy]
    blank_rows_covered = 0
    blank_cols_covered = 0
    for eachBlankRow in blank_rows:
        if (eachBlankRow > first_loc[0] and eachBlankRow < second_loc[0]) or (eachBlankRow < first_loc[0] and eachBlankRow > second_loc[0]):
            blank_rows_covered += 1
    for eachBlankCol in blank_cols:
        if (eachBlankCol > first_loc[1] and eachBlankCol < second_loc[1]) or (eachBlankCol < first_loc[1] and eachBlankCol > second_loc[1]):
            blank_cols_covered += 1
    total_blank_cols_covered += blank_cols_covered
    total_blank_rows_covered += blank_rows_covered
    distances[key] = abs(first_loc[0] - second_loc[0]) + abs(first_loc[1] - second_loc[1])

sum = sum(list(distances.values())) + ((total_blank_cols_covered + total_blank_rows_covered) * blank_row_val)
print(sum)
