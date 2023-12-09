import numpy as np
import sys

def get_data():
    file_name = 'day5.txt'

    with open(file_name) as fp:
        data = fp.read().strip()
        user_input = data.strip().split('\n')
        return user_input

userInput = get_data()
seedNumbersStr = userInput[0].split(':')[1].split(' ')
seedNumbersStr = [i for i in seedNumbersStr if i != '']
seedNumbers = [int(i) for i in seedNumbersStr]
ongoingRanges = []
for i in range(0,len(seedNumbers),2):
    ongoingRanges.append([seedNumbers[i],seedNumbers[i]+seedNumbers[i+1]-1])
userInput = [line for line in userInput if line != '']

seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []
map_idx = 0
for i in range(2,len(userInput)):
    if userInput[i][0].isdigit():
        if map_idx == 0:
            seed_to_soil_map.append(userInput[i])
        elif map_idx == 1:
            soil_to_fertilizer_map.append(userInput[i])
        elif map_idx == 2:
            fertilizer_to_water_map.append(userInput[i])
        elif map_idx == 3:
            water_to_light_map.append(userInput[i])
        elif map_idx == 4:
            light_to_temperature_map.append(userInput[i])
        elif map_idx == 5:
            temperature_to_humidity_map.append(userInput[i])
        elif map_idx == 6:
            humidity_to_location_map.append(userInput[i])
    if not userInput[i][0].isdigit():
        map_idx += 1

for i in range(0,len(seed_to_soil_map)):
    seed_to_soil_map[i] = [int(i) for i in seed_to_soil_map[i].split(' ')]
for i in range(0,len(soil_to_fertilizer_map)):
    soil_to_fertilizer_map[i] = [int(i) for i in soil_to_fertilizer_map[i].split(' ')]
for i in range(0,len(fertilizer_to_water_map)):
    fertilizer_to_water_map[i] = [int(i) for i in fertilizer_to_water_map[i].split(' ')]
for i in range(0,len(water_to_light_map)):
    water_to_light_map[i] = [int(i) for i in water_to_light_map[i].split(' ')]
for i in range(0,len(light_to_temperature_map)):
    light_to_temperature_map[i] = [int(i) for i in light_to_temperature_map[i].split(' ')]
for i in range(0,len(temperature_to_humidity_map)):
    temperature_to_humidity_map[i] = [int(i) for i in temperature_to_humidity_map[i].split(' ')]
for i in range(0,len(humidity_to_location_map)):
    humidity_to_location_map[i] = [int(i) for i in humidity_to_location_map[i].split(' ')]

maps = [seed_to_soil_map,soil_to_fertilizer_map,fertilizer_to_water_map,water_to_light_map,light_to_temperature_map,temperature_to_humidity_map,humidity_to_location_map]
#maps = [seed_to_soil_map]
for m in maps:
    newRanges = []
    for singleMapping in m:
        items_to_remove = []
        for eachRange in ongoingRanges:
            #find if there is any overlap between our ongoingRanges and the mapping conversions and store that as a new range
            if eachRange[0] >= singleMapping[1] and eachRange[0] <= singleMapping[1] + singleMapping[2]-1:
                #there is at least some overlap since the lower ongoingRange is within the map range
                if eachRange[1] <= singleMapping[1] + singleMapping[2]-1:
                    #the entire eachRange is within the map range, so change both ends of the range
                    newRanges.append([eachRange[0]-singleMapping[1]+singleMapping[0],eachRange[1]-singleMapping[1]+singleMapping[0]])
                    items_to_remove.append(eachRange)
                else:
                    #print(eachRange, 'only left overlaps with ', singleMapping)
                    #only the lower range is in the limit, so change the upper limit of the range and append the excess upper part of the range to be checked against other mappings
                    newRanges.append([eachRange[0]-singleMapping[1]+singleMapping[0],singleMapping[2]-1+singleMapping[0]])
                    #need to take the range that isn't overlapping and add it as a new range in order to see if it overlaps with another mapping
                    ongoingRanges.append([singleMapping[1]+singleMapping[2],eachRange[1]])
                    items_to_remove.append(eachRange)
            elif eachRange[1] >= singleMapping[1] and eachRange[1] <= singleMapping[1] + singleMapping[2]-1:
                #print('only right overlaps', eachRange)
                #only the right side overlaps with the map
                #the part that didn't overlap, put in ongoingRanges to check if there are future overlaps
                ongoingRanges.append([eachRange[0],singleMapping[1]-1])
                #the part that did overlap should be mapped
                newRanges.append([singleMapping[0],eachRange[1]-singleMapping[1]+singleMapping[0]])
                items_to_remove.append(eachRange)
            #else:
                #no overlap at all
        ongoingRanges = [i for i in ongoingRanges if i not in items_to_remove]
    ongoingRanges = newRanges + ongoingRanges

#print(ongoingRanges)
lowest = sys.maxsize
for eachRange in ongoingRanges:
    if eachRange[0] < lowest:
        lowest = eachRange[0]
print(lowest)
