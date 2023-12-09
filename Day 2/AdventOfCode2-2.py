import numpy as np

def get_data():
    file_name = 'day2.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

userInput = get_data()
powers = []
for n in userInput:
    inputs = n.split(':')[1]
    single_game_inputs = inputs.split(';')
    rgb_max = [0,0,0]
    for m in single_game_inputs:
        single_color_inputs = m.split(',')
        for num in single_color_inputs:
            parts = num.split(' ')
            if parts[2] == 'blue':
                rgb_max[2] = max(rgb_max[2], int(parts[1]))
            if parts[2] == 'red':
                rgb_max[0] = max(rgb_max[0], int(parts[1]))
            if parts[2] == 'green':
                rgb_max[1] = max(rgb_max[1], int(parts[1]))
    powers.append(rgb_max[0]*rgb_max[1]*rgb_max[2])

print(sum(powers))
