import numpy as np

def get_data():
    file_name = 'day6.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

userInput = get_data()
times = [i for i in userInput[0].split(':')[1].split(' ') if i != '']
records = [i for i in userInput[1].split(':')[1].split(' ') if i != '']
actual_time = ''
actual_record = ''
for i in range(0,len(times)):
    actual_time += times[i]
    actual_record += records[i]
actual_time = int(actual_time)
actual_record = int(actual_record)
ways_to_win = 0
for j in range(1,actual_time):
    if (actual_time-j) * j > actual_record:
        ways_to_win += 1
print(ways_to_win)
