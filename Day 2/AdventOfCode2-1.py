import numpy as np

def get_data():
    file_name = 'day2.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

userInput = get_data()
red_max = 12
green_max = 13
blue_max = 14
invalid = False
count_valid = 0
running_id = 1
for n in userInput:
    inputs = n.split(':')[1]
    single_game_inputs = inputs.split(';')
    for m in single_game_inputs:
        single_color_inputs = m.split(',')
        for num in single_color_inputs:
            parts = num.split(' ')
            if parts[2] == 'blue' and int(parts[1]) > blue_max:
                invalid = True
                break
            if parts[2] == 'red' and int(parts[1]) > red_max:
                invalid = True
                break
            if parts[2] == 'green' and int(parts[1]) > green_max:
                invalid = True
                break
        if invalid == True:
            break
    if invalid == False:
        count_valid += running_id
        #print("%d valid", running_id)
    invalid = False
    running_id += 1
print(count_valid)
