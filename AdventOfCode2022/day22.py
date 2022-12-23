# Advent of Code 2022 Day 22
# Author:   Rachael Judy
# Date:     12/22/22
# Purpose:  travel map with wraparound to non blank and then actually folds into cube
# Note - this will solve all inputs (as the nets are the same shape, see below) but isn't truly generic
#       _a__ _b__
#      f    |    c
#      |____|__d_|
#      g    |
#  _g__|____d
# |    |    |
# f____|_e__c
# a    e
# |_b__|

import parseMod
import regex as re
import time

stage = 'b'
day = 22
year = 2022
parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row(f"data/{str(day).zfill(2)}data.csv")
start = time.time()

# parse out commands
commands = re.findall('\d+\D', data[-1])
commands.append(re.findall('\d+', data[-1])[-1]+'N')  # otherwise misses the last move with no turn

# parse maze into dictionary for val, four directions points
maze = dict()
RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
for r in range(len(data[:-1])):  # fills the map to be rectangular
    while len(data[r]) < max(len(data[i]) for i in range(len(data[:-1]))):
        data[r] += ' '
for r in range(len(data[:-1])):
    for c in range(len(data[0])):
        if data[r][c] != ' ':
            maze[(r, c)] = [data[r][c]]
            for dire in directions:
                if stage == 'a':  # simple wrap around
                    x, y = (r + dire[0]) % len(data[:-1]), (c + dire[1]) % len(data[0])
                    while data[x][y] == ' ':
                        x = (x + dire[0]) % len(data[:-1])
                        y = (y + dire[1]) % len(data[0])
                    maze[(r, c)].append(((x, y), directions.index(dire)))
                else:  # wrap to paired edge
                    # non edge mappings
                    if 0 <= r+dire[0] < len(data[:-1]) and 0 <= c + dire[1] < len(data[0]) \
                            and data[r+dire[0]][c+dire[1]] != ' ':
                        maze[(r, c)].append(((r+dire[0], c+dire[1]), directions.index(dire)))
                    # paired edge mappings
                    elif directions.index(dire) == UP and 50 <= c < 100:  # a mapping
                        maze[(r, c)].append(((c+100, 0), RIGHT))
                    elif directions.index(dire) == LEFT and 150 <= r < 200:  # a mapping
                        maze[(r, c)].append(((0, r-100), DOWN))
                    elif directions.index(dire) == UP and 100 <= c < 150:  # b mapping
                        maze[(r, c)].append(((199, c-100), UP))
                    elif directions.index(dire) == DOWN and 0 <= c < 50:  # b mapping
                        maze[(r, c)].append(((0, c+100), DOWN))
                    elif directions.index(dire) == RIGHT and 0 <= r < 50:  # c mapping
                        maze[(r, c)].append(((149-r, 99), LEFT))
                    elif directions.index(dire) == RIGHT and 100 <= r < 150:  # c mapping
                        maze[(r, c)].append(((149-r, 149), LEFT))
                    elif directions.index(dire) == DOWN and 100 <= c < 150:  # d mapping
                        maze[(r, c)].append(((c-50, 99), LEFT))
                    elif directions.index(dire) == RIGHT and 50 <= r < 100:  # d mapping
                        maze[(r, c)].append(((49, r+50), UP))
                    elif directions.index(dire) == DOWN and 50 <= c < 100:  # e mapping
                        maze[(r, c)].append(((c+100, 49), LEFT))
                    elif directions.index(dire) == RIGHT and 150 <= r < 200:  # e mapping
                        maze[(r, c)].append(((149, r-100), UP))
                    elif directions.index(dire) == LEFT and 100 <= r < 150:  # f mapping
                        maze[(r, c)].append(((149-r, 50), RIGHT))
                    elif directions.index(dire) == LEFT and 0 <= r < 50:  # f mapping
                        maze[(r, c)].append(((149-r, 0), RIGHT))
                    elif directions.index(dire) == UP and 0 <= c < 50:  # g mapping
                        maze[(r, c)].append(((c+50, 50), RIGHT))
                    elif directions.index(dire) == LEFT and 50 <= r < 100:  # g mapping
                        maze[(r, c)].append(((100, r-50), DOWN))

# go through commands
pos, dire = (0, min(point[1] if point[0]==0 else 1000000 for point in maze)), 0  # right initially
for cmd in commands:
    for _ in range(int(cmd[:-1])):
        if maze[maze[pos][dire + 1][0]][0] != '#':
            pos, dire = maze[pos][dire + 1]
        else:
            break
    dire = (dire + (cmd[-1] == 'R') - (cmd[-1] == 'L')) % 4

result = 1000 * (pos[0]+1) + 4 * (pos[1]+1) + dire
print(f"Time: {time.time() - start}")
print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
