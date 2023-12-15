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
for i in range(0,len(parts)):
    cur_val = 0
    for eachChar in parts[i]:
        cur_val += ord(eachChar)
        cur_val *= 17
        cur_val = cur_val % 256
    hash_vals[i] = cur_val
print(sum(hash_vals))
