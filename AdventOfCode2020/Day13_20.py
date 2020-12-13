# Advent of Code 2020 - Day 13

# Author:   Rachael Judy
# Date:     12/13/2020
# Purpose:  Find the soonest train that is after the start time
#           Find first time with all trains departing at time + index in original read in that matches


import os
import sys
import math

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


# get input
information = parseMod.readCSV_rowEl('data/13loop.csv', ',')

target = int(information[0][0])  # initialize the target value
buses, indices = [], []  # track the spots where a bus actually is
min_bus_departure = 10_000_000  # used to store minimum departure time available
bus_id = 0  # bus to take

# Part 1, setup for part 2
# go through each bus and find first time it can be taken
for element in information[1]:
    if element.isnumeric():  # if not x, store bus
        buses.append(int(element))
        indices.append(information[1].index(element))

        # save closest_possible_departure possible departure time for this bus - calculates first time can leave
        closest_possible_departure = math.ceil(target / float(element)) * int(element)
        if closest_possible_departure < min_bus_departure:  # save bus id and the time
            min_bus_departure = closest_possible_departure
            bus_id = int(element)

print("Part 1: ", (min_bus_departure-target) * bus_id)


# Part 2
# use CRT and Euclidean to determine the x that meets conditions:
#       x % bus_id_i == (-index_i) % bus_id_i for all i in buses
mod = math.prod(buses)
x = 0
for offset, id in zip(indices, buses):  # check each bus
    z = int(mod / id)
    y = pow(z, -1, id)  # python 3.8 method - mod inverse of z mod id
    w = (y * z) % mod  # weight
    x += (-offset) * w

# compute minimum
x %= mod
print("Part 2: ", x)
