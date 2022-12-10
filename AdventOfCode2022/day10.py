# Advent of Code 2022 Day 10
# Author:   Rachael Judy
# Date:     12/10/22
# Purpose:  Assembly-esque instructions to draw pixels

import parseMod
import time
start = time.time()

stage = 'a'
day = 10
year = 2022
parseMod.createDataFile(year=year, day=day)
instructions = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", ' ')
for i in range(len(instructions)-1, -1, -1):
    if instructions[i][0] == 'addx':
        instructions.insert(i, ['noop'])

x = 1
signal_strength = 0
display = [['.' for _ in range(40)] for _ in range(6)]
for i in range(len(instructions)):
    # compute signal strength
    signal_strength += (i + 1) * x if (i - 19) % 40 == 0 else 0
    # update display based on sprite
    display[int(i/40)][i%40] = '#' if (i % 40) in {x-1, x, x+1} else '.'
    # modify x
    x += int(instructions[i][1]) if instructions[i][0] == 'addx' else 0

result = signal_strength
print("OUTPUT for B cannot be submitted via module: see display below")
for row in display:
    print(*row)

print("SUBMITTING RESULT A: ", result)
print(f"Time: {time.time()-start}")
parseMod.submit(result, part=stage, day=day, year=year)
