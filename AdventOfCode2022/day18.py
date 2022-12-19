# Advent of Code 2022 Day 18
# Author:   Rachael Judy
# Date:     12/18/22
# Purpose:  compute surface area given points and then only exposed SA by taking border and inside SA of that
# Note: doing list might have been faster instead of in set searching

import parseMod
import time
import itertools

stage = 'b'
day = 18
year = 2022
parseMod.createDataFile(year=year, day=day)
points = {(int(x), int(y), int(z)) for [x, y, z] in parseMod.readCSV_rowEl(f"data/{str(day).zfill(2)}data.csv", ',')}
start = time.time()

sides = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
add_tuple = lambda tuple1, tuple2: tuple(map(sum, zip(tuple1, tuple2)))

if stage == 'b':
    max_point = max(max(x, y, z) for (x, y, z) in points)
    exterior_points = set(itertools.permutations([i for i in range(-1, max_point + 2) for _ in range(3)], 3))
    exploring, index = [(-1, -1, -1)], 0
    while index != len(exploring):
        for side in sides:
            if add_tuple(exploring[index], side) not in points \
                    and add_tuple(exploring[index], side) not in exploring \
                    and add_tuple(exploring[index], side) in exterior_points:
                exploring.append(add_tuple(exploring[index], side))
        index += 1
    points = exterior_points.difference(exploring)

result = sum((add_tuple(p, side) not in points) for side in sides for p in points)

print(f"Time: {time.time() - start}")
print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
