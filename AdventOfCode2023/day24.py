# Advent of Code 2023 Day 24
# Author:   Rachael Judy
# Date:     12/24/23
# Purpose:

from collections import deque, defaultdict
import itertools
import math
import parseMod

ready = False
day = 24
stage = 'a'
year = 2023

# parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

# look for when vx * t + x0, vy * t + y0, vz * t + z0 equal someone else's
# for a, check for all pairs of intersections to see if slopes(velocities) are parallal but not touching
# if not, check if they are in the test area (t when xs intercept, t when ys intercept, which mean reversing
# and setting equal
# at+b=x => (x-b)/a = (x-d)/c => x/a - x/c = -d/c + b/a => x = (-d/c + b/a) / (1/a - 1/c)
# ct+d=x
#

default_value = 8#200000000000001
class Hailstone:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def collides(self, other, stage='a'):
        # return coordinates of collision
        # if at+b = ct+d => (a-c) t = d - b => t = (d-b) / (a-c)
        # unless the start and velocities are identical, both are guarenteed to intercept but the question is at the same time
        if self.vx == other.vx and self.x != other.vx:
            return None, None
        if self.vy == other.vy and self.y != other.vy:
            return None, None
        if self.vx == other.vx and self.x == other.x and self.vy == other.vy and self.y == other.y:
            return 200000000000001, 200000000000001

        # must throw out the negative times too
        elif self.vx == other.vx and self.x == other.x:
            if (other.y - self.y) / (self.vy - other.vy) >= 0:
                return 200000000000001,  self.vy * (other.y - self.y) / (self.vy - other.vy) + self.y
        elif self.vy == other.vy and self.y == other.y:
            if (other.x - self.x) / (self.vx - other.vx) >= 0:
                return self.vx * (other.x - self.x) / (self.vx - other.vx) + self.x, 200000000000001
        elif (other.x - self.x) * (self.vy - other.vy)  == (self.vx - other.vx) * (other.y - self.y) and (other.y - self.y) / (self.vy - other.vy) >= 0:
            return self.vx * (other.x - self.x) / (self.vx - other.vx) + self.x, self.vy * (other.y - self.y) / (self.vy - other.vy) + self.y
        return None, None

hailstones = list()
for row in data:
    (x,y,z), (vx, vy, vz) = (c.split(', ') for c in row.split('@ '))
    hailstones.append(Hailstone(int(x), int(y), int(z), int(vx), int(vy), int(vz)))

result = 0
for h1, h2 in itertools.combinations(hailstones, 2):
    x,y = h1.collides(h2)
    # if x is not None and y is not None and 200000000000000 <= x <= 400000000000000 and 200000000000000 <= x <= 400000000000000:
    #     result += 1

    if x is not None and y is not None and 7 <= x <= 27 and 7 <= x <= 27:
        result += 1


if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)