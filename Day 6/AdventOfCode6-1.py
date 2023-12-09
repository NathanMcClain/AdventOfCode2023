import numpy as np

def get_data():
    file_name = 'day6.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

userInput = get_data()
times = [int(i) for i in userInput[0].split(':')[1].split(' ') if i != '']
records = [int(i) for i in userInput[1].split(':')[1].split(' ') if i != '']

ways_to_win = [0] * len(times)
for i in range(0,len(times)):
    for j in range(1,times[i]):
        if (times[i]-j) * j > records[i]:
            ways_to_win[i] += 1
error = np.prod(ways_to_win)
print(error)
