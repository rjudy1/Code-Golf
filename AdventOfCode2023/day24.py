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

parseMod.createDataFile(year=year, day=day)
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
#
# hailstones = list()
# for row in data:
#     (x,y,z), (vx, vy, vz) = (c.split(', ') for c in row.split('@ '))
#     hailstones.append(Hailstone(int(x), int(y), int(z), int(vx), int(vy), int(vz)))
#
# result = 0
# for h1, h2 in itertools.combinations(hailstones, 2):
#     x,y = h1.collides(h2)
#     # if x is not None and y is not None and 200000000000000 <= x <= 400000000000000 and 200000000000000 <= x <= 400000000000000:
#     #     result += 1
#
#     if x is not None and y is not None and 7 <= x <= 27 and 7 <= x <= 27:
#         result += 1
import numpy as np
from decimal import Decimal as D, getcontext

getcontext().prec = 50

import re

numParser = re.compile(r"(-?\d+)")
parseNums = lambda inp: [D(x) for x in numParser.findall(inp)]

with open('data/24data.csv') as f:
    d24s = f.read()
d24t = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""


class Hail:
    def __init__(self, inp, debug=False):
        self.debug = debug
        self.px, self.py, self.pz, self.vx, self.vy, self.vz = parseNums(inp)
        self.XYslope = D('inf') if self.vx == 0 else self.vy / self.vx
        self.ax, self.ay, self.az = 0, 0, 0

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'<{self.px}, {self.py}, {self.pz} @ {self.vx}, {self.vy}, {self.vz}>'

    def intersectXY(self, other):
        # returns None, if parallel / intersect in a past
        if self.XYslope == other.XYslope:
            return None
        if self.XYslope == float('inf'):  # self is vertical
            intX = self.px
            intY = other.XYslope * (intX - other.px) + other.py
        elif other.XYslope == float('inf'):  # other is vertical
            intX = other.px
            intY = self.XYslope * (intX - self.px) + self.py
        else:
            # y - y1 = m1 * ( x - x1 ) reduced to solve for x
            intX = (self.py - other.py - self.px * self.XYslope + other.px * other.XYslope) / (
                        other.XYslope - self.XYslope)
            intY = self.py + self.XYslope * (intX - self.px)
        intX, intY = intX.quantize(D(".1")), intY.quantize(D(".1"))
        # intY = round(intY)

        selfFuture = np.sign(intX - self.px) == np.sign(self.vx)
        otherFuture = np.sign(intX - other.px) == np.sign(other.vx)
        if not (selfFuture and otherFuture):
            return None
        return (intX, intY)

    def adjust(self, ax, ay, az):
        self.vx -= ax - self.ax
        self.vy -= ay - self.ay
        self.vz -= az - self.az
        assert type(self.vx) is D
        self.XYslope = D('inf') if self.vx == 0 else self.vy / self.vx
        self.ax, self.ay, self.az = ax, ay, az

    def getT(self, p):  # if both vx and vy are 0... good luck
        if self.vx == 0:
            return (p[1] - self.py) / self.vy
        return (p[0] - self.px) / self.vx

    def getZ(self, other, inter):  # given an intersection point and an other Hail
        # now we KNOW: z = pz_i + t_i*(vz_i-aZ)   [t = (inter[0]-px_i)/(vx_i)]
        #              z = pz_j + t_j*(vz_j-aZ)
        # (pz_i - pz_j + t_i*vz_i - t_j*vz_j)/(t_i - t_j) =  aZ
        tS = self.getT(inter)
        tO = other.getT(inter)
        if tS == tO:
            assert self.pz + tS * self.vz == other.pz + tO * other.vz
            return None
        return (self.pz - other.pz + tS * self.vz - tO * other.vz) / (tS - tO)


def p1(inp, pMin, pMax, debug=False):
    hailstones = []
    for row in inp.strip().splitlines():
        hailstones.append(Hail(row, debug=debug))
    sm = 0
    for idx, H1 in enumerate(hailstones):
        for H2 in hailstones[idx + 1:]:
            p = H1.intersectXY(H2)
            if p is None:
                if debug: print(f'NO INTERSECT : {H1} x {H2}')
            elif p[0] >= pMin and p[0] <= pMax and p[1] >= pMin and p[1] <= pMax:
                if debug: print(f'YES {H1} x {H2} (@ {p})')
                sm += 1
            else:
                if debug: print(f'NO [OUTSIDE] :{H1} x {H2} (@ {p})')
    return sm


print(p1(d24t, 7, 27, debug=True))  # 2

print(p1(d24s, 200000000000000, 400000000000000, debug=False))  # P1 answer


def p2(inp, debug=False):
    hailstones = []
    for row in inp.strip().splitlines():
        hailstones.append(Hail(row, debug=debug))

    N = 0
    while True:
        print('.', end='')
        for X in range(N + 1):
            Y = N - X
            for negX in (-1, 1):
                for negY in (-1, 1):
                    aX = X * negX
                    aY = Y * negY
                    # if debug: print(f'checking v=<{aX},{aY},?>')
                    H1 = hailstones[0]
                    H1.adjust(aX, aY, 0)
                    inter = None
                    # if debug: print(f'comparing v {H1}')
                    for H2 in hailstones[1:]:
                        H2.adjust(aX, aY, 0)
                        p = H1.intersectXY(H2)
                        if p is None:
                            # if debug: print(f'v {H2} — NONEE')
                            break
                        if inter is None:
                            # if debug: print(f'v {H2} — setting to {p}')
                            inter = p
                            continue
                        if p != inter:
                            # if debug: print(f'v {H2} — NOT SAME P {p}')
                            break
                        # if debug: print(f'v {H2} — continuing{p}')
                    if p is None or p != inter:
                        continue
                    # if debug: print(f'FOUND COMMON INTERSECTION {p}')
                    # we escaped intersecting everything with H1 with a single valid XY point!
                    print(f'potential intersector found with v=<{aX},{aY},?>' \
                          + f', p=<{inter[0]},{inter[1]},?>')
                    aZ = None
                    H1 = hailstones[0]
                    # print(f'v {H1}')
                    for H2 in hailstones[1:]:
                        nZ = H1.getZ(H2, inter)
                        if aZ is None:
                            # print(f'first aZ is {aZ} from {H2}')
                            aZ = nZ
                            continue
                        elif nZ != aZ:
                            print(f'invalidated! by {nZ} from {H1}')
                            return
                            break
                    if aZ == nZ:
                        H = hailstones[0]
                        Z = H.pz + H.getT(inter) * (H.vz - aZ)
                        print(
                            f'found solution :) v=<{aX},{aY},{aZ}>, p=<{inter[0]},{inter[1]},{Z}>, s = {Z + inter[0] + inter[1]}')
                        return

        N += 1


p2(d24t, debug=False)  # -3, 1, 2

p2(d24s, debug=False)  # P2 answer
if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)