import numpy as np

def get_data():
    file_name = 'day1.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

userInput = get_data()
elves = []
index = 0
for food in userInput:
    if len(elves) == index:
        elves.append(0)
    if food == '':
        index = index + 1
    else:
        elves[index] = elves[index] + int(food)

print(max(elves))
