# Advent of Code 2024 Day 4
# Author:   Rachael Judy
# Purpose:

import parseMod


ready = True
day = 4
stage = 'b'  #
year = 2024

parseMod.createDataFile(year=year, day=day)
grid = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")


result = 0


# pass over possible directions? - do LR/RL pass first
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if j+3 < len(row):
            if ''.join(grid[i][j:j+4]) == 'XMAS' or ''.join(grid[i][j:j+4]) == 'SAMX':
                result += 1
        if i+3 < len(grid):
            if ''.join([grid[i][j], grid[i+1][j], grid[i+2][j], grid[i+3][j]]) == 'XMAS' or ''.join([grid[i][j], grid[i+1][j], grid[i+2][j], grid[i+3][j]]) == 'SAMX':
                result += 1
        if i+3 < len(grid) and j+3 < len(row):
            if ''.join([grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3]]) == 'XMAS' or ''.join([grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3]]) == 'SAMX':
                result += 1
        if  i+3 < len(grid) and j-3 >= 0:
            if ''.join([grid[i][j], grid[i+1][j-1], grid[i+2][j-2], grid[i+3][j-3]]) == 'XMAS' or ''.join([grid[i][j], grid[i+1][j-1], grid[i+2][j-2], grid[i+3][j-3]]) == 'SAMX':
                result += 1

result = 0
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if i+2 < len(grid) and j+2 < len(row):
            if ''.join([grid[i][j], grid[i+1][j+1], grid[i+2][j+2]]) == 'MAS' and ''.join([grid[i][j+2], grid[i+1][j+1], grid[i+2][j]]) == 'MAS':
                result += 1
            if ''.join([grid[i][j], grid[i+1][j+1], grid[i+2][j+2]]) == 'MAS' and ''.join([grid[i][j+2], grid[i+1][j+1], grid[i+2][j]]) == 'SAM':
                result += 1
            if ''.join([grid[i][j], grid[i + 1][j + 1], grid[i + 2][j + 2]]) == 'SAM' and ''.join([grid[i][j+2], grid[i+1][j+1], grid[i+2][j]]) == 'MAS':
                result += 1
            if ''.join([grid[i][j], grid[i + 1][j + 1], grid[i + 2][j + 2]]) == 'SAM' and ''.join([grid[i][j+2], grid[i+1][j+1], grid[i+2][j]]) == 'SAM':
                result += 1

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
