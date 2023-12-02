# Advent of Code 2023 Day 2
# Author:   Rachael Judy
# Date:     12/2/23
# Purpose:

import parseMod

ready = False
day = 2
stage = 'b'

year = 2023

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

result = 0
for num, game in enumerate(array):
    if stage == 'a':
        possible = True
        for draw in game.split(':')[1].split(';'):
            for color in draw.split(','):
                if color.strip().split(' ')[1] == 'red' and int(color.strip().split(' ')[0]) > 12 or \
                   color.strip().split(' ')[1] == 'green' and int(color.strip().split(' ')[0]) > 13 or \
                   color.strip().split(' ')[1] == 'blue' and int(color.strip().split(' ')[0]) > 14:
                    possible = False
                    break
        if possible:
            result += num+1
    else:
        red_max, green_max, blue_max = 0, 0, 0
        for draw in game.split(':')[1].split(';'):
            for color in draw.split(','):
                if color.strip().split(' ')[1] == 'red':
                    red_max = max(red_max, int(color.strip().split(' ')[0]))
                elif color.strip().split(' ')[1] == 'green':
                    green_max = max(green_max, int(color.strip().split(' ')[0]))
                elif color.strip().split(' ')[1] == 'blue':
                    blue_max = max(blue_max, int(color.strip().split(' ')[0]))
        result += red_max * green_max * blue_max

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
