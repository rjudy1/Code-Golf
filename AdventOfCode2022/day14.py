# Advent of Code 2022 Day 14
# Author:   Rachael Judy
# Date:     12/14/22
# Purpose:  simulate falling sand

import parseMod
import time

start = time.time()
stage = 'b'
day = 14
year = 2022
parseMod.createDataFile(year=year, day=day)
rocks = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")


# returns path taken by dropped grain
def drop_grain(blocks, path_thus_far):
    pos = path_thus_far[-1]
    while pos[1] < 200:
        if not blocks.issuperset({(pos[0], pos[1] + 1)}):
            pos = (pos[0], pos[1] + 1)
        elif not blocks.issuperset({(pos[0] - 1, pos[1] + 1)}):
            pos = (pos[0] - 1, pos[1] + 1)
        elif not blocks.issuperset({(pos[0] + 1, pos[1] + 1)}):
            pos = (pos[0] + 1, pos[1] + 1)
        else:
            break
        path_thus_far.append(pos)


# add rocks
blocked_space = set()
for row in rocks:
    paths = [[*map(int, path.split(','))] for path in row.split('->')]
    blocked_space.add((paths[0][0], paths[0][1]))
    for i in range(1, len(paths)):
        position = paths[i - 1]
        while position != paths[i]:
            if paths[i][0] == position[0]:
                position[1] = position[1] + int((paths[i][1] - position[1]) / abs((paths[i][1] - position[1])))
            else:
                position[0] = position[0] + int((paths[i][0] - position[0]) / abs((paths[i][0] - position[0])))
            blocked_space.add((position[0], position[1]))

if stage == 'b':
    peak = max(point[1] for point in blocked_space)
    for i in range(300, 700):
        blocked_space.add((i, peak + 2))  # add a floor

tracked_path = [(500, 0)]
grains = 0
while True:
    drop_grain(blocked_space, tracked_path)
    blocked_space.add(tracked_path[-1])
    if tracked_path[-1][1] == 200 or tracked_path[-1] == (500, 0):
        result = grains + int(stage == 'b')
        break
    tracked_path.pop()  # path will start above where last one ended
    grains += 1

print("SUBMITTING RESULT: ", result)
print(f"Time: {time.time() - start}")
parseMod.submit(result, part=stage, day=day, year=year)
