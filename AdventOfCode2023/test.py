# Advent of Code 2023 Day 5
# Author:   Rachael Judy
# Date:     12/5/23
# Purpose:

from collections import defaultdict

import parseMod

ready = False
day = 5
stage = 'b'

year = 2023

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_batch("data/" + str(day).zfill(2) + "data.csv", delim='\n')

seeds = [int(i) for i in array[0].strip().split(' ')[1:]]


def split_data_to_map(data, map):
    data = [int(i) for i in data.strip().split(' ')[2:]]
    for i in range(0, len(data), 3):
        dest, source, rangel = data[i], data[i + 1], data[i + 2]
        map[source] = (dest, rangel)


# first is seed to soil
seed_to_soil = defaultdict(lambda i: (i, 1))
split_data_to_map(array[1], seed_to_soil)
soil_to_fertilizer = defaultdict(lambda i: (i, 1))
split_data_to_map(array[2], soil_to_fertilizer)
fertilizer_to_water = defaultdict(lambda i: (i, 1))
split_data_to_map(array[3], fertilizer_to_water)
water_to_light = defaultdict(lambda i: (i, 1))
split_data_to_map(array[4], water_to_light)
light_to_temperature = defaultdict(lambda i: (i, 1))
split_data_to_map(array[5], light_to_temperature)
temperature_to_humidity = defaultdict(lambda i: (i, 1))
split_data_to_map(array[6], temperature_to_humidity)
humidity_to_location = defaultdict(lambda i: (i, 1))
split_data_to_map(array[7], humidity_to_location)


def get_value(source, map):
    for key in map:
        if key <= source < key + map[key][1]:
            return map[key][0] + source - key
    return source


result = 7010000000000000000
for seed in seeds:
    # check each seed
    result = min(
        get_value(get_value(get_value(get_value(get_value(get_value(get_value(seed, seed_to_soil), soil_to_fertilizer),
                                                          fertilizer_to_water), water_to_light), light_to_temperature),
                            temperature_to_humidity), humidity_to_location), result)




def split_data_to_map_rev(data, map):
    data = [int(i) for i in data.strip().split(' ')[2:]]
    for i in range(0, len(data), 3):
        dest, source, rangel = data[i], data[i + 1], data[i + 2]
        map[dest] = (source, rangel)

# first is seed to soil
seed_to_soil = defaultdict(lambda i: (i, 1))
split_data_to_map_rev(array[1], seed_to_soil)
soil_to_fertilizer = defaultdict(lambda i: (i, 1))
split_data_to_map_rev(array[2], soil_to_fertilizer)
fertilizer_to_water = defaultdict(lambda i: (i, 1))
split_data_to_map_rev(array[3], fertilizer_to_water)
water_to_light = defaultdict(lambda i: (i, 1))
split_data_to_map_rev(array[4], water_to_light)
light_to_temperature = defaultdict(lambda i: (i, 1))
split_data_to_map_rev(array[5], light_to_temperature)
temperature_to_humidity = defaultdict(lambda i: (i, 1))
split_data_to_map_rev(array[6], temperature_to_humidity)
humidity_to_location = defaultdict(lambda i: (i, 1))
split_data_to_map_rev(array[7], humidity_to_location)
# 130289921
# 79004094

result = 100000000000000000000
for loc in range(130289921//2, 260579843):
    x = get_value(get_value(get_value(get_value(get_value(get_value(get_value(loc, humidity_to_location), temperature_to_humidity), light_to_temperature), water_to_light),
                                        fertilizer_to_water), soil_to_fertilizer), seed_to_soil)
    for i in range(0, len(seeds), 2):
        if seeds[i] <= x < seeds[i] + seeds[i+1]:
            result = min(loc, result)
            print("change:", result, loc, x)
    if loc % 100000 == 0:
        print(result, loc, x)

# for i in range(0, len(seeds), 2):
#     for ds in range(seeds[i+1]):
#         result = min(
#             get_value(
#                 get_value(get_value(get_value(get_value(get_value(get_value(seeds[i]+ds, seed_to_soil), soil_to_fertilizer),
#                                                         fertilizer_to_water), water_to_light), light_to_temperature),
#                           temperature_to_humidity), humidity_to_location), result)
#     print(result)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
