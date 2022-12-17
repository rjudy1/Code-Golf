# Advent of Code 2022 Day 15
# Author:   Rachael Judy
# Date:     12/15/22
# Purpose:  optimizing iterations and structures - still 30s-ish  slow

import parseMod
import time

stage = 'b'
day = 15
year = 2022
parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")
start = time.time()


class Range:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.left == other.left:
            return self.right > other.right
        return self.left < other.left

    def __getitem__(self, key):
        return self.right if key else self.left

    def __setitem__(self, key, value):
        if key == 0:
            self.left = value
        else:
            self.right = value


sensors = []
beacons = dict()
for row in data:
    sensorx, sensory = int(row.split(' ')[2][2:-1]), int(row.split(' ')[3][2:-1])
    beaconx, beacony = int(row.split(' ')[-2][2:-1]), int(row.split(' ')[-1][2:])
    distance = abs(sensorx - beaconx) + abs(sensory - beacony)
    beacons[beacony] = beaconx
    sensors.append((sensorx, sensory, distance))


def check_captured(sensors, beacons, target, minimum_point=-100000000, maximum_point=100000000):
    captured = []
    for sensor in sensors:
        if sensor[2] >= abs(target-sensor[1]):
            xbounds = (max(sensor[0] - sensor[2] + abs(target - sensor[1]), minimum_point),
                       min(sensor[0] + sensor[2] - abs(target - sensor[1]), maximum_point))
            captured.append(Range(xbounds[0], xbounds[1]))

    # clean ranges
    captured.sort()
    index = 0
    while index < len(captured):
        x = captured[index][1]
        while index+1 < len(captured) and captured[index+1][1] <= x:
            captured.pop(index+1)
        if index < len(captured) - 1:
            if captured[index][1] >= captured[index+1][0]:
                captured[index][1] = captured[index + 1][0] - 1
        index += 1

    total = 0
    for c in captured:
        total += c[1]-c[0] + 1
    if beacons.get(target) is not None:
        total -= 1
    return total, captured


if stage == 'a':
    result = check_captured(sensors, beacons, 2000000)
else:
    b_range = 4000000
    for i in range(b_range + 1):
        count, captured_space = check_captured(sensors, beacons, i, 0, b_range)
        found_solution = False

        if i % 500000 == 0: print(i)
        if count != b_range + 1 and beacons.get(i) is None:
            # skipping endpoints currently 0 and b_range+1 or b_range
            for j in range(len(captured_space)-1):
                if captured_space[j+1][0] - captured_space[j][1] != 1:
                    answer = (captured_space[j+1][0]-1, i)
                    found_solution = True
                    break
        if found_solution: break
    result = 4000000 * answer[0] + answer[1]

print(f"Time: {time.time() - start}")
print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
