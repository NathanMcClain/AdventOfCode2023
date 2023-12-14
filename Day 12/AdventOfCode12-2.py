import numpy as np
import copy
from functools import cache

def get_data():
    file_name = 'day12.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

@cache
def valid_layout_count(layout, group, ongoing_count = 0):
    if not layout:
        # if we are out of groups to make and do not have ongoing counting group, then this matches
        return not group and not ongoing_count
    num_sols = 0
    options = ['#','.'] if layout[0] == '?' else layout[0]
    for eachOption in options:
        if eachOption == '#':
            #this is part of the current group
            num_sols += valid_layout_count(layout[1:],group,ongoing_count+1)
        else:
            if ongoing_count > 0:
                #We have a group remaining and the size matches what we just made
                if group and ongoing_count == group[0]:
                    num_sols += valid_layout_count(layout[1:],group[1:])
            else:
                #continue to the next iteration, we aren't in a group
                num_sols += valid_layout_count(layout[1:],group)

    return num_sols

userInput = get_data()
counts = []


for i in range(0,len(userInput)):
    layout_part = userInput[i].split(' ')[0]
    full_layout = layout_part + '?' + layout_part + '?' + layout_part + '?' + layout_part + '?' + layout_part + '.'
    groupsStr = userInput[i].split(' ')[1]
    numList = tuple(map(int,groupsStr.split(',')))
    #print(numList*5)
    counts.append(valid_layout_count(full_layout+'.',numList*5))
    #print(i,counts[i])

print(sum(counts))
