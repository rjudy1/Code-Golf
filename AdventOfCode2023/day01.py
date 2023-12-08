# Advent of Code 2023 Day 1
# Author:   Rachael Judy
# Date:     12/1/23
# Purpose:  first and last digit/spelled out digit on each line is value, sum values

import parseMod

ready = False
day = 1
stage = 'b'
year = 2023

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

nums = []
for line in array:
    temp = ''
    for idx, letter in enumerate(line):
        if letter.isdigit():
            temp = ''.join([temp, letter])
        elif stage=='b':
            options = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
            for i, op in enumerate(options):
                if len(op)+idx <= len(line) and line[idx:idx+len(op)] == op:
                    temp = ''.join([temp, str(i)])
                    break
    nums.append(int(temp[0]+temp[-1]))
result = sum(nums)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
