# Advent of Code 2025 Day 9
# Author:   Rachael Judy
# Purpose:  find largest rectangle with opposite corners in input and then rectangle within polygon formed from input

from itertools import combinations
from shapely import Polygon

import aocd
from mycookie import cookie

ready = True
day = 9
stage = 'b'

poly = Polygon([tuple([*map(int, ln.split(','))]) for ln in aocd.get_data(cookie, day, 2025).splitlines()])
result = max((abs((y0:=c[0][1])-(y1:=c[1][1]))+1) * (abs((x0:=c[0][0])-(x1:=c[1][0]))+1) * (stage=='a' or poly.covers(Polygon(((x0,y0),(x0,y1),(x1,y1),(x1,y0))))) for c in combinations(poly.exterior.coords, 2))

print(f'stage {stage} result (ready={ready}): \n{result}')
if ready:
    aocd.submit(result, part=stage, day=day, year=2025, session=cookie)
