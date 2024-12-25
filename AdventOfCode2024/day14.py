# Advent of Code 2024 Day 14
# Author:   Rachael Judy
# Purpose:  track robot positions in grid, look for Christmas tree (wth is a Christmas tree shape? unique positions)
# also had solution that found minimum entropy arrangement but this added an n^2 per move so just chose unique positions

import csv
import math
import parseMod

ready = True
day = 14
stage = 'b'  # 210587128, 7286
year = 2024

parseMod.createDataFile(year=year, day=day)
robot_positions = dict()  # id (row originally on to coordinates)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file, delimiter='\n')
    for i, row in enumerate(reader):
        p_str, v_str = row[0].split()  # x,y,vx,vy
        robot_positions[i] = ([int(p_str[2:].split(',')[0]), int(p_str[2:].split(',')[1]), int(v_str[2:].split(',')[0]), int(v_str[2:].split(',')[1])])
    map = [row[0] for row in reader]

row_limit, col_limit = 103, 101
for move in range(row_limit*col_limit):
    quadrant_robots = [0, 0, 0, 0]
    npl = list()
    for i in robot_positions:
        npl.append(((robot_positions[i][0] + robot_positions[i][2]*move) % col_limit, (robot_positions[i][1] + robot_positions[i][3]*move) % row_limit))
        if 0 <= npl[-1][0] < col_limit // 2 and 0 <= npl[-1][1] < row_limit // 2:
            quadrant_robots[0] += 1
        elif 0 <= npl[-1][0] < col_limit // 2 and npl[-1][1] > row_limit // 2:
            quadrant_robots[1] += 1
        elif npl[-1][0] > col_limit // 2 and 0 <= npl[-1][1] < row_limit // 2:
            quadrant_robots[2] += 1
        elif npl[-1][0] > col_limit // 2 and npl[-1][1] > row_limit // 2:
            quadrant_robots[3] += 1
    # entropy = sum((p[0]-q[0])**2 + (p[1]-q[1])**2 for p in new_position_list for q in new_position_list)
    if stage == 'a' and move == 100:
        result = math.prod(quadrant_robots)
        break
    if stage == 'b' and len(set(npl)) == len(npl):  # unique positions
        result = move
        break

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
