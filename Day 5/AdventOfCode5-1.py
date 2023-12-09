import numpy as np

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
ongoingNumbers = seedNumbers
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

for i in range(0,len(ongoingNumbers)):
    inRange = False
    foundIdx = -1
    for j in range(0,len(seed_to_soil_map)):
        if ongoingNumbers[i] >= seed_to_soil_map[j][1] and ongoingNumbers[i] <= seed_to_soil_map[j][1] + seed_to_soil_map[j][2]:
            inRange = True
            foundIdx = j
            break
    if inRange:
        ongoingNumbers[i] = ongoingNumbers[i] - seed_to_soil_map[foundIdx][1] + seed_to_soil_map[foundIdx][0]

for i in range(0,len(ongoingNumbers)):
    inRange = False
    foundIdx = -1
    for j in range(0,len(soil_to_fertilizer_map)):
        if ongoingNumbers[i] >= soil_to_fertilizer_map[j][1] and ongoingNumbers[i] <= soil_to_fertilizer_map[j][1] + soil_to_fertilizer_map[j][2]:
            inRange = True
            foundIdx = j
            break
    if inRange:
        ongoingNumbers[i] = ongoingNumbers[i] - soil_to_fertilizer_map[foundIdx][1] + soil_to_fertilizer_map[foundIdx][0]

for i in range(0,len(ongoingNumbers)):
    inRange = False
    foundIdx = -1
    for j in range(0,len(fertilizer_to_water_map)):
        if ongoingNumbers[i] >= fertilizer_to_water_map[j][1] and ongoingNumbers[i] <= fertilizer_to_water_map[j][1] + fertilizer_to_water_map[j][2]:
            inRange = True
            foundIdx = j
            break
    if inRange:
        ongoingNumbers[i] = ongoingNumbers[i] - fertilizer_to_water_map[foundIdx][1] + fertilizer_to_water_map[foundIdx][0]

for i in range(0,len(ongoingNumbers)):
    inRange = False
    foundIdx = -1
    for j in range(0,len(water_to_light_map)):
        if ongoingNumbers[i] >= water_to_light_map[j][1] and ongoingNumbers[i] <= water_to_light_map[j][1] + water_to_light_map[j][2]:
            inRange = True
            foundIdx = j
            break
    if inRange:
        ongoingNumbers[i] = ongoingNumbers[i] - water_to_light_map[foundIdx][1] + water_to_light_map[foundIdx][0]

for i in range(0,len(ongoingNumbers)):
    inRange = False
    foundIdx = -1
    for j in range(0,len(light_to_temperature_map)):
        if ongoingNumbers[i] >= light_to_temperature_map[j][1] and ongoingNumbers[i] <= light_to_temperature_map[j][1] + light_to_temperature_map[j][2]:
            inRange = True
            foundIdx = j
            break
    if inRange:
        ongoingNumbers[i] = ongoingNumbers[i] - light_to_temperature_map[foundIdx][1] + light_to_temperature_map[foundIdx][0]

for i in range(0,len(ongoingNumbers)):
    inRange = False
    foundIdx = -1
    for j in range(0,len(temperature_to_humidity_map)):
        if ongoingNumbers[i] >= temperature_to_humidity_map[j][1] and ongoingNumbers[i] <= temperature_to_humidity_map[j][1] + temperature_to_humidity_map[j][2]:
            inRange = True
            foundIdx = j
            break
    if inRange:
        ongoingNumbers[i] = ongoingNumbers[i] - temperature_to_humidity_map[foundIdx][1] + temperature_to_humidity_map[foundIdx][0]

for i in range(0,len(ongoingNumbers)):
    inRange = False
    foundIdx = -1
    for j in range(0,len(humidity_to_location_map)):
        if ongoingNumbers[i] >= humidity_to_location_map[j][1] and ongoingNumbers[i] <= humidity_to_location_map[j][1] + humidity_to_location_map[j][2]:
            inRange = True
            foundIdx = j
            break
    if inRange:
        ongoingNumbers[i] = ongoingNumbers[i] - humidity_to_location_map[foundIdx][1] + humidity_to_location_map[foundIdx][0]

print(min(ongoingNumbers))
