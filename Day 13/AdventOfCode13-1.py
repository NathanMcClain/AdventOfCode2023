import numpy as np
import copy

def get_data():
    file_name = 'day13.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

userInput = get_data()
patterns = []
pattern_idx = 0
for line in userInput:
    if len(patterns) == pattern_idx:
        patterns.append([])
    if line == '':
        pattern_idx += 1
        continue
    patterns[pattern_idx].append(line)

total_contribution = []
for k in range(0,len(patterns)):
    horizontal_sym_idx = -1
    for i in range(1,len(patterns[k])):
        if patterns[k][i] == patterns[k][i-1]:
            #Two rows match, check the other rows as well
            rest_of_rows_match = True
            for h in range(1, min(len(patterns[k])-1-i,i-1)+1):
                if patterns[k][i-h-1] != patterns[k][i+h]:
                    rest_of_rows_match = False

            if rest_of_rows_match:
                horizontal_sym_idx = i
                total_contribution.append( 100 * horizontal_sym_idx )
                print(k,'has horizontal sym',horizontal_sym_idx)
                break

    if horizontal_sym_idx == -1:
        cols = []
        for r in range(0,len(patterns[k][0])):
            cols.append([patterns[k][p][r] for p in range(0,len(patterns[k]))])
        vertical_sym_idx = -1
        for j in range(1,len(cols)):
            if cols[j] == cols[j-1]:
                #Two cols match, check the other rows as well
                rest_of_cols_match = True
                for y in range(1,min(len(cols)-1-j,j-1)+1):
                    if cols[j-y-1] != cols[j+y]:
                        # print('comparing',(r-y-1),(r+y))
                        #print(y,'breaks it')
                        rest_of_cols_match = False
                        break
                if rest_of_cols_match:
                    vertical_sym_idx = j
                    total_contribution.append(j)
                    print(k,'has vertical sym',j)

print(sum(total_contribution))
