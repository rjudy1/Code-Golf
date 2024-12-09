# Advent of Code 2024 Day
# Author:   Rachael Judy
# Purpose:  move chunks of memory back into gaps/then only full gaps

import csv

import parseMod

ready = True
day = 9
stage = 'a'
year = 2024

parseMod.createDataFile(year=year, day=day)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file)
    map = [row[0] for row in reader][0]

running_position = 0
blocks = dict()
block_positions = list()
gaps = list()
memory = list()
for i, element in enumerate(map):
    if i%2==0:
        blocks[i//2] = [running_position, int(element)]
        for j in range(int(element)):
            memory.append(i//2)
            block_positions.append(running_position+j)
    else:
        gaps.append([running_position, int(element),])
        for j in range(int(element)):
            memory.append(-1)

    running_position += int(element)
    last_index = i//2

# collapse
if stage == 'a':
    taken = 0
    termination_position = len(memory)-1
    for i in range(running_position):
        if memory[i] == -1:
            # grab from back of blocks
            if last_index == 0 or termination_position == i:
                break

            memory[i] = last_index
            taken += 1
            memory[block_positions[len(block_positions)-taken]] = -1
            termination_position = block_positions[len(block_positions)-taken]
            if blocks[last_index][1] - 1 > 0:
                blocks[last_index][1] -= 1
            else:
                blocks[last_index][1] -= 1
                last_index -= 1

else:
    # move left if it can
    for i in range(last_index, -1, -1):
        for gap in gaps:
            if gap[1] >= blocks[i][1] and gap[0] < blocks[i][0]:
                # put here
                for j in range(blocks[i][1]):
                    memory[gap[0]+j] = i
                    memory[blocks[i][0]+j] = -1
                gap[1] -= blocks[i][1]
                if gap[1] == 0:
                    gaps.remove(gap)
                else:
                    gap[0] += blocks[i][1]
                break

result = sum(memory[i] * i if memory[i] != -1 else 0 for i in range(len(memory)))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
