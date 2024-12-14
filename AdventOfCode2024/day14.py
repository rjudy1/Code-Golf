# Advent of Code 2024 Day 14
# Author:   Rachael Judy
# Purpose:  track robot positions in grid, look for Christmas tree (wth is a Christmas tree shape?, look for unique positions for all?)


import csv

import parseMod

ready = True
day = 14
stage = 'a'
year = 2024

parseMod.createDataFile(year=year, day=day)
robot_positions = dict()  # id (row originally on to coordinates)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file, delimiter='\n')
    for i, row in enumerate(reader):
        p_str, v_str = row[0].split()
        robot_positions[i] = ([int(p_str[2:].split(',')[0]), int(p_str[2:].split(',')[1]), int(v_str[2:].split(',')[0]), int(v_str[2:].split(',')[1])])
    map = [row[0] for row in reader]

result = 0
row_limit = 103
col_limit = 101

move = 100
for move in range(100000):
    quadrant_robots = [0, 0, 0, 0]
    import numpy as np
    grid = np.zeros((col_limit, row_limit))
    for i in robot_positions:
        final_position = [(robot_positions[i][0] + robot_positions[i][2]*move) % col_limit, (robot_positions[i][1] + robot_positions[i][3]*move) % row_limit]
        if 0 <= final_position[0] < col_limit // 2 and 0 <= final_position[1] < row_limit // 2:
            quadrant_robots[0] += 1
        elif 0 <= final_position[0] < col_limit // 2 and final_position[1] > row_limit // 2:
            quadrant_robots[1] += 1
        elif final_position[0] > col_limit // 2 and 0 <= final_position[1] < row_limit // 2:
            quadrant_robots[2] += 1
        elif final_position[0] > col_limit // 2 and final_position[1] > row_limit // 2:
            quadrant_robots[3] += 1
        grid[tuple(final_position)] += 1

    unique_test = True
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i,j] > 1:
                unique_test = False
    if unique_test:
        print(move)

    # print(move)
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         print(int(grid[i,j]),end='')
    #     print()

import math
result = math.prod(quadrant_robots)

# count robots in each quadrant


if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
