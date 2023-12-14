import numpy as np
import copy

def get_data():
    file_name = 'day14.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

userInput = get_data()
damage = 0
for j in range(0,len(userInput[0])):
    stack_counts = []
    square_idx = [-1]
    cur_stack_count = 0
    for i in range(0,len(userInput)):
        if userInput[i][j] == '#':
            square_idx.append(i)
            stack_counts.append(cur_stack_count)
            cur_stack_count = 0
        elif userInput[i][j] == 'O':
            cur_stack_count += 1
    if cur_stack_count > 0:
        stack_counts.append(cur_stack_count)
        cur_stack_count = 0

    #calculate damage
    #print(stack_counts)
    #print(square_idx)
    for k in range(0,len(stack_counts)):
        if len(square_idx) == 1:
            #No squares, all stacks are at the top
            idxs = [i for i in range(len(userInput),len(userInput)-stack_counts[k],-1)]
            #print(j,'damage no square',sum(idxs))
            damage += sum(idxs)
        elif stack_counts[k] > 0:
            if square_idx[k] == -1:
                #these are at the top
                idxs = [i for i in range(len(userInput),len(userInput)-stack_counts[k],-1)]
                #print(j,'damage at top',sum(idxs))
                damage += sum(idxs)
            else:
                idxs = [i for i in range(len(userInput)-square_idx[k]-1,len(userInput) - square_idx[k]-1-stack_counts[k],-1)]
                #print(j,'damage elsewhere',sum(idxs))
                damage += sum(idxs)

print(damage)
