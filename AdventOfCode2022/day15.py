# Advent of Code 2022 Day 15
# Author:   Rachael Judy
# Date:     12/15/22
# Purpose:

import parseMod
import time

stage = 'a'
day = 15
year = 2022
parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

# sensors will be a list of dictionaries representing the end points for each sensor
sensors = []
beacons = dict()
for row in data:
    sensor = dict()
    sensorx, sensory = int(row.split(' ')[2][2:-1]), int(row.split(' ')[3][2:-1])
    beaconx, beacony = int(row.split(' ')[-2][2:-1]), int(row.split(' ')[-1][2:])
    distance = abs(sensorx-beaconx) + abs(sensory-beacony)
    for i in range(-1*distance, distance+1):
        sensor[sensory + i] = (sensorx + -1 * (distance - abs(i)), sensorx + distance - abs(i))
    beacons[beacony] = beaconx
    sensors.append(sensor)

start = time.time()

def check_captured(sensors, beacons, target, maximum_point=100000000, minimum_point=-100000000):
    range_captured = []
    for sensor in sensors:
        if sensor.get(target) is not None:
            sensor[target] = (max(sensor[target][0], minimum_point), min(sensor[target][1], maximum_point))
            captured = False
            to_add = True
            to_trash = []
            for i in range(len(range_captured)):
                # completely or partially contains the range
                if range_captured[i][0] > sensor[target][0] and range_captured[i][1] < sensor[target][1]:
                    to_trash.append(i)
                    captured = True

                # starts in the middle of range but ends after
                elif range_captured[i][0] <= sensor[target][0] <= range_captured[i][1] and range_captured[i][1] < sensor[target][1]:
                    range_captured[i] = (range_captured[i][0], sensor[target][0]-1)
                    captured = True

                # ends in the middle of range but starts before
                elif range_captured[i][0] > sensor[target][0] and range_captured[i][1] >= sensor[target][1] >= range_captured[i][0]:
                    range_captured[i] = (sensor[target][1]+1, range_captured[i][1])
                    captured = True

                # completely contains the sensor range
                elif range_captured[i][0] <= sensor[target][0] and range_captured[i][1] >= sensor[target][1]:
                    to_add = False
                    captured = True

            to_trash.sort()
            to_trash.reverse()
            for k in to_trash:
                range_captured.pop(k)
            if to_add:
                range_captured.append(sensor[target])

    total = 0
    for (a, b) in range_captured:
        total += b - a + 1
    if beacons.get(target) is not None:
        total -= 1
    return total, range_captured

print(f"part 1 {check_captured(sensors,beacons,2000000)}")

b_range = 4000000
for i in range(b_range+1):
    x = check_captured(sensors, beacons, i)
    exit = False

    if x[0] != b_range:
        for j in range(b_range+1):
            for r in x[1]:
                if x
            if exit:
                break



result = check_captured()
print("SUBMITTING RESULT: ", result)
print(f"Time: {time.time() - start}")
parseMod.submit(result, part=stage, day=day, year=year)
