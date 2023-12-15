import numpy as np
import copy

def get_data():
    file_name = 'day15.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

userInput = get_data()
parts = userInput[0].split(',')
hash_vals = [0] * len(parts)
boxes = []
for i in range(0,256):
    boxes.append([])

# print(parts)
# print(boxes)
for i in range(0,len(parts)):
    cur_val = 0
    for eachChar in parts[i]:
        #print(eachChar)
        if eachChar != '=' and eachChar != '-':
            cur_val += ord(eachChar)
            cur_val *= 17
            cur_val = cur_val % 256
        if eachChar == '=' or eachChar == '-':
            break
    hash_vals[i] = cur_val
    if parts[i][-1] == '-':
        for j in range(0,len(boxes[hash_vals[i]])):
            if parts[i][:len(parts[i])-1] == boxes[hash_vals[i]][j].split(' ')[0]:
                #print('remove', parts[i][:len(parts[i])-1])
                boxes[hash_vals[i]].pop(j)
                break
    elif '=' in parts[i]:
        part_to_check = parts[i].split('=')[0]
        found = False
        for j in range(0,len(boxes[hash_vals[i]])):
            if boxes[hash_vals[i]][j].split(' ')[0] == part_to_check:
                replacement = copy.deepcopy(parts[i])
                newString = replacement.replace('=',' ')
                #print('replacement',newString)
                boxes[hash_vals[i]][j] = newString
                #print('Box now',boxes[hash_vals[i]][j])
                found = True
                break
        if not found:
            replacement = copy.deepcopy(parts[i])
            newString = replacement.replace('=',' ')
            #print('adding',newString)
            boxes[hash_vals[i]].append(newString)
            #print(hash_vals[i],'after adding',boxes[hash_vals[i]])
            #print(hash_vals[i+1],'next',boxes[hash_vals[i+1]])

focusing_power = 0
for i in range(0,len(boxes)):
    for j in range(0,len(boxes[i])):
        focusing_power += ((i+1)*(j+1)*int(boxes[i][j][-1]))
#print(boxes)
print(focusing_power)
#print(hash_vals)
