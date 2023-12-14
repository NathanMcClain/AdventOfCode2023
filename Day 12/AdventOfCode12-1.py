import numpy as np
import copy

def get_data():
    file_name = 'day12.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

def replace_questions(run_iter, layout, question_idx):
    options = ['#','.']
    replace_plan = str(bin(run_iter)[2:].zfill(len(question_idx)))
    newlayout = copy.deepcopy(layout)
    stringNew = list(newlayout)
    for i in range(0,len(question_idx)):
        stringNew[question_idx[i]] = options[int(replace_plan[i])]
    return "".join(stringNew)

def is_valid_layout(layout, group):
    layout_copy = copy.deepcopy(layout)
    layout_counts = []
    ongoing_count = 0
    #print(layout)
    for i in range(0,len(layout_copy)):
        if layout_copy[i] == '#':
            ongoing_count += 1
        elif ongoing_count > 0:
            new_count = copy.deepcopy(ongoing_count)
            layout_counts.append(new_count)
            ongoing_count = 0
    if ongoing_count > 0:
        new_count = copy.deepcopy(ongoing_count)
        layout_counts.append(new_count)
    return layout_counts == group


userInput = get_data()
counts = []
layouts = []
groups = []
for i in range(0,len(userInput)):
    layouts.append(userInput[i].split(' ')[0])
    groupsStr = userInput[i].split(' ')[1]
    numList = groupsStr.split(',')
    groups.append([int(i) for i in numList])
options = ['#','.']
for i in range(0,len(layouts)):
    counts.append(0)
    question_idx = [j for j in range(0,len(layouts[i])) if layouts[i][j] == '?']
    #Replace every combination of the ? with # or . and check if it is a valid layout
    for h in range(0,len(options) ** len(question_idx)):
        #create a deep copy of the layout string
        newStr = copy.deepcopy(layouts[i])
        outputStr = replace_questions(h,newStr,question_idx)
        if is_valid_layout(outputStr,groups[i]):
            counts[i] += 1

print(sum(counts))
