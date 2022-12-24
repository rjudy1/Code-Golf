# Advent of Code 2022 Day 24
# Author:   Rachael Judy
# Date:     12/24/22
# Purpose:  navigate through moving blizzard, bfs with cache
# Note - who knew in set was so much faster than in list

import math
import parseMod
import time

stage = 'b'
day = 24
year = 2022
parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row(f"data/{str(day).zfill(2)}data.csv")
start = time.time()

# set of time t (cyclical of lcm of rows and cols inside) : where blizzards will be
blizzards = {i: set() for i in range(math.lcm(len(data) - 2, len(data[0]) - 2))}
for row in range(1, len(data)-1):
    for col in range(1, len(data[1])-1):
        for i in range(math.lcm(len(data) - 2, len(data[0]) - 2)):
            if data[row][col] == '<' or data[row][col] == '>':
                blizzards[i].add(complex(row, (col-1+i*((data[row][col]=='>')-(data[row][col]=='<')))
                                       % (len(data[1])-2) + 1))
            elif data[row][col] == '^' or data[row][col] == 'v':
                blizzards[i].add(complex((row-1+i*((data[row][col]=='v')-(data[row][col]=='^')))
                                       % (len(data)-2) + 1, col))
            else:
                break


def bfs(origin: complex, end: complex, start_time=0) -> int:
    global blizzards
    exploring, cache = [(origin, start_time)], set()
    while len(exploring):
        for move in [1, 1j, 0, -1, -1j]:
            if (exploring[0][0]+move, (exploring[0][1]+1) % math.lcm(len(data) - 2, len(data[0]) - 2)) not in cache \
                and exploring[0][0]+move not in blizzards[(exploring[0][1]+1) % math.lcm(len(data) - 2, len(data[0]) - 2)] \
                and (0 < (exploring[0][0]+move).real < len(data)-1 and 0 < (exploring[0][0]+move).imag < len(data[0])-1
                     or exploring[0][0]+move == end) and exploring[0][0]+move != origin:
                if exploring[0][0]+move == end:
                    return exploring[0][1]+1
                exploring.append((exploring[0][0]+move, exploring[0][1]+1))
                cache.add((exploring[0][0] + move, (exploring[0][1] + 1) % math.lcm(len(data) - 2, len(data[0]) - 2)))
        exploring.pop(0)


if stage == 'a':
    result = bfs(1j, len(data)-1+(len(data[0])-2)*1j)
else:
    result = bfs(1j, len(data)-1+(len(data[0])-2)*1j,
                 bfs(len(data)-1+(len(data[0])-2)*1j, 1j, bfs(1j, len(data)-1+(len(data[0])-2)*1j)))

print(f"Time: {time.time() - start}")
print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
