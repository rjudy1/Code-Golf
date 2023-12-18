# Advent of Code 2023 Day 17
# Author:   Rachael Judy
# Date:     12/17/23
# Purpose:  Djikstra with constraints of min 3 consecutive steps in a direction, 4<=streak<10 for b, slow :(

from collections import defaultdict
import heapq
import math
import time
import parseMod

ready = False
day = 17
stage = 'a'
year = 2023

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")


def djikstra(start: (int, int), objective: (int, int)):
    global data
    minimum_costs = defaultdict(lambda: math.inf)
    settled = set()
    queue = [(0, start, (0, 1), 0), (0, start, (1, 0), 0)]  # cost, position, dir, streak
    minimum_costs[(start, (0, 1), 0)] = 0
    minimum_costs[(start, (1, 0), 0)] = 0
    while len(queue):
        cost, pos, dir, streak = heapq.heappop(queue)
        settled.add((pos, dir, streak))
        if pos == objective:
            return minimum_costs[(pos, dir, streak)]

        for dr, dc in {(0, 1), (0, -1), (1, 0), (-1, 0)}:
            if 0 <= pos[0] + dr < len(data) and 0 <= pos[1] + dc < len(data[0]) and (-dr, -dc) != dir:
                if stage == 'a':
                    increment = int(data[pos[0]+dr][pos[1]+dc])
                    if (dr, dc) != dir:
                        new_key = ((pos[0] + dr, pos[1] + dc), (dr, dc), 1)
                    elif streak < 3 and (dr, dc) == dir:
                        new_key = ((pos[0] + dr, pos[1] + dc), (dr, dc), streak+1)
                    else:
                        continue

                else:
                    if (streak == 0 and dir == (dr, dc) or streak >= 4 and (dr, dc) != dir)\
                            and 0 <= pos[0] + 4*dr < len(data) and 0 <= pos[1] + 4*dc < len(data[0]):
                        new_key = ((pos[0] + 4*dr, pos[1] + 4*dc), (dr, dc), 4)
                        increment = sum(int(data[pos[0] + i * dr][pos[1] + i * dc]) for i in range(1, 5))
                    elif 4 <= streak < 10 and (dr, dc) == dir:
                        new_key = ((pos[0] + dr, pos[1] + dc), (dr, dc), streak+1)
                        increment = int(data[pos[0] + dr][pos[1] + dc])
                    else:
                        continue

                minimum_costs[new_key] = min(minimum_costs[new_key],
                                             minimum_costs[(pos, dir, streak)] + increment)
                if new_key not in settled and (minimum_costs[new_key], *new_key) not in queue:
                    heapq.heappush(queue, (minimum_costs[new_key], *new_key))


start = time.time()
result = djikstra((0, 0), (len(data) - 1, len(data[0]) - 1))
print(time.time()-start)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
