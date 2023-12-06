# Advent of Code 2023 Day 5
# Author:   Rachael Judy
# Date:     12/5/23
# Purpose:  multiple dictionary mappings, divide into groupings for efficiency, not the most efficent, could collapse
#           and iteratively fill but idc anymore

import parseMod

ready = True
day = 5
stage = 'b'

year = 2023

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_batch("data/" + str(day).zfill(2) + "data.csv", delim='\n')
seeds = [int(i) for i in array[0].strip().split(' ')[1:]]


def split_data_to_map(data):
    map = dict()
    for i in range(0, len(data), 3):
        map[data[i + 1]] = (data[i], data[i + 2])
    # map entire range
    if 0 not in map:  # add zero to lowest in map
        map[0] = (0, min(map))
    if max(map) < 2 * max(seeds):  # add max map to max possible seed
        map[max(map)+map[max(map)][1]] = (max(map)+map[max(map)][1], 2 * max(seeds) - (max(map)+map[max(map)][1]) + 1)
    keys = sorted(map.keys())
    for i, key in enumerate(keys[:-1]):  # fill in gaps
        if key + map[key][1] != keys[i+1]:
            map[key + map[key][1]] = (key + map[key][1], keys[i+1] - map[key][1] + 1)
    return map


def get_value(source, map):
    for key in map:
        if key <= source < key + map[key][1]:
            return map[key][0] + source - key
    return source


# group regions from 0 to 2 * max(seeds) to sections of locations (inclusive at both ends for each group)
seed_groupings = {(0, 2*max(seeds))}
maps = list()
for data in range(1, len(array)):  # go over rest, building maps
    queue = list(seed_groupings)
    seed_groupings.clear()
    maps.append(split_data_to_map([int(i) for i in array[data].strip().split(' ')[2:]]))  # build next layer of maps
    while len(queue):  # go through, regrouping based on new map split
        start, end = queue.pop(0)
        start1, end1 = start, end
        # more efficient would be to store seed to each new stage instead of just seed groups to avoid propagate but
        # more annoying an im done with this for now
        for map in maps[:-1]:  # propagate seed groupings through map - not the most efficient but cleaner for tracking
            start1 = get_value(start1, map)
            end1 = get_value(end1, map)
        # take new map and split based on edges
        for source in maps[-1]:  # split groupings further based on matches
            if source <= start1 < source + maps[-1][source][1]:  # start in range
                if source + maps[-1][source][1] > end1:  # fully in range
                    seed_groupings.add((start, end))
                else:  # end out of range
                    seed_groupings.add((start, start + maps[-1][source][1] - (start1 - source) - 1))
                    queue.append((start + maps[-1][source][1] - (start1 - source), end))  # still need to group this

result = 10e10
if stage == 'a':
    for seed in seeds:
        result = min(result, get_value(get_value(get_value(get_value(get_value(get_value(get_value(seed, maps[0]),
                                       maps[1]), maps[2]), maps[3]), maps[4]), maps[5]), maps[6]))
else:
    for group in seed_groupings:
        for i in range(0, len(seeds), 2):
            if seeds[i] <= group[0] < seeds[i] + seeds[i+1]:  # case 1: group minimum is contained in seed range
                result = min(result, get_value(get_value(get_value(get_value(get_value(get_value(get_value(group[0],
                                               maps[0]), maps[1]), maps[2]), maps[3]), maps[4]), maps[5]), maps[6]))
            elif seeds[i] <= group[1] < seeds[i] + seeds[i+1] or group[0] < seeds[i] < group[1]\
                    or group[0] < seeds[i] < group[1]:
                result = min(result, get_value(get_value(get_value(get_value(get_value(get_value(get_value(seeds[i],
                                               maps[0]), maps[1]), maps[2]), maps[3]), maps[4]), maps[5]), maps[6]))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
