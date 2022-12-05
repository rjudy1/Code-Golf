# Advent of Code 2022 Day 5
# Author:   Rachael Judy
# Date:     12/5/22
# Purpose:  move stacks of crates either in batches or one at a time

import parseMod

stage = 'b'
day = 5
year = 2022

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

# set initial state of stacks
stacks = [[] for j in range(int((len(data[0])+1)/4))]
for i in range(len(data)):
    # finds end of stack initial conditions
    if data[i][1].isdigit():
        data = data[i+1:]
        break
    for j in range(1, len(data[i]), 4):
        if data[i][j].isalpha():
            stacks[int((j-1)/4)].insert(0, data[i][j])

if stage == 'a':
    for action in data:
        line = action.split(' ')
        stacks[int(line[5]) - 1].append(stacks[int(line[3]) - 1].pop() for i in range(int(line[1])))
else:
    for action in data:
        line = action.split(' ')
        stacks[int(line[5]) - 1].extend(stacks[int(line[3]) - 1][0-int(line[1]):])
        stacks[int(line[3]) - 1] = stacks[int(line[3]) - 1][:0-int(line[1])]

result = ''.join([s[-1] for s in stacks])
print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
