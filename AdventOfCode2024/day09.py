# Advent of Code 2024 Day 9
# Author:   Rachael Judy
# Purpose:  defragment chunks of memory back into gaps/then only full gaps

import csv
import parseMod

ready = True
day = 9
stage = 'b'
year = 2024

parseMod.createDataFile(year=year, day=day)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file)
    map = [row[0] for row in reader][0]

# populate initial memory and note locations of gaps and blocks
blocks, gaps, memory = dict(), list(), list()
running_position = 0
for i, element in enumerate(map):
    if i % 2 == 0:
        blocks[i//2] = [running_position, int(element)]
        memory.extend([i//2 for _ in range(int(element))])
    else:
        gaps.append([running_position, int(element),])
        memory.extend([-1 for _ in range(int(element))])
    running_position += int(element)
    last_index = i//2  # save greatest id for later

if stage == 'a':  # iterate through memory grabbing from the back to fill slots
    termination_position = len(memory)-1
    for i in range(len(memory)):
        if memory[i] == -1:
            if termination_position == i:
                break
            # move values in memory back
            memory[i] = last_index
            memory[blocks[last_index][0] + blocks[last_index][1]-1] = -1
            termination_position = blocks[last_index][0] + blocks[last_index][1]-1

            if blocks[last_index][1] - 1 > 0:
                blocks[last_index][1] -= 1
            else:
                last_index -= 1

else:  # defragment whole blocks
    for i in range(last_index, -1, -1):
        for gap in gaps:
            if gap[1] >= blocks[i][1] and gap[0] < blocks[i][0]:  # if full block fits
                for j in range(blocks[i][1]):
                    memory[gap[0]+j] = i
                    memory[blocks[i][0]+j] = -1
                gap[1] -= blocks[i][1]
                if gap[1] == 0:
                    gaps.remove(gap)
                else:
                    gap[0] += blocks[i][1]
                break

result = sum(memory[i] * i for i in range(len(memory)) if memory[i] != -1)
if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
