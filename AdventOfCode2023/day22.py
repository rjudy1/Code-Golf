# Advent of Code 2023 Day 22
# Author:   Rachael Judy
# Date:     12/22/23
# Purpose:  drop straight blocks at various 3D orientations and determine which blocks can be removed and cost of removing

from collections import deque, defaultdict
import math
import parseMod

ready = True
day = 22
stage = 'a'
year = 2023

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")


class Brick:
    def __init__(self, label, x0, y0, z0, x1, y1, z1):
        self.label = label
        width = abs(x1-x0) + abs(y1-y0) + abs(z1-z0) + 1
        self.zs = [z for z in range(min(z0, z1), max(z0, z1)+1)] if z0 != z1 else [z0 for _ in range(width)]
        self.coords = [tuple((x, y, z)) for x, y, z in
                       zip([x for x in range(min(x0, x1), max(x0, x1)+1)] if x0 != x1 else [x0 for _ in range(width)],
                           [y for y in range(min(y0, y1), max(y0, y1)+1)] if y0 != y1 else [y0 for _ in range(width)],
                           self.zs)]

    def drop(self, layer_dictionary):
        # drop this block to lowest level based on layers
        tops = max(layer_dictionary[(x, y)] for i, (x, y, _) in enumerate(self.coords))
        for i, (x, y, z) in enumerate(self.coords):
            self.zs = [z - (min(self.zs) - tops) + 1 for z in self.zs]
            layer_dictionary[(x, y)] = max(self.zs)

    def supports(self, bricks):
        # return bricks supported by this
        slots = defaultdict(lambda: 0)
        for i, (x, y, z) in enumerate(self.coords):
            slots[(x, y)] = max(self.zs[i], slots[(x, y)])
        supports = set()
        for brick in bricks:
            brick_slots = defaultdict(lambda: math.inf)
            for i, (x, y, z) in enumerate(brick.coords):
                brick_slots[(x, y)] = min(brick.zs[i], brick_slots[(x, y)])
            for slot in slots:
                if slot in brick_slots and brick_slots[slot] == slots[slot] + 1:
                    supports.add(brick)
        return supports

    def is_supported_by(self, bricks):
        # return blocks directly supporting this
        slots = defaultdict(lambda: math.inf)
        for i, (x, y, z) in enumerate(self.coords):
            slots[(x, y)] = min(self.zs[i], slots[(x, y)])
        supported_by = set()
        for brick in bricks:
            brick_slots = defaultdict(lambda: 0)
            for i, (x, y, z) in enumerate(brick.coords):
                brick_slots[(x, y)] = max(brick.zs[i], brick_slots[(x, y)])
            for slot in slots:
                if slot in brick_slots and brick_slots[slot] == slots[slot] - 1:
                    supported_by.add(brick)
        return supported_by

    def __lt__(self, other):
        return min(self.zs) < min(other.zs)


# parse data into bricks
bricks = list()
for idx, row in enumerate(data):
    start, end = [r.split(',') for r in row.split('~')]
    bricks.append(Brick(idx, int(start[0]), int(start[1]), int(start[2]), int(end[0]), int(end[1]), int(end[2])))
bricks.sort()  # sorted by lowest z drops first
bottom_layer = defaultdict(lambda: 0)
for i in range(len(bricks)):
    bricks[i].drop(bottom_layer)


# build dictionaries for who supports who and who is supported by who
supports_dict = dict()
supported_by_dict = dict()
# check who falls if brick X disintegrates
for brick in bricks:
    supports_dict[brick] = brick.supports(bricks)
    supported_by_dict[brick] = brick.is_supported_by(bricks)

supports, single_supporter = set(), set()
for brick in bricks:
    if len(supports_dict[brick]) == 0:
        supports.add(brick)
    if len(supported_by_dict[brick]) > 1:
        supports.update(supported_by_dict[brick])
for brick in bricks:
    if len(supported_by_dict[brick]) == 1:
        single_supporter.add(next(iter(supported_by_dict[brick])))
if stage == 'a':
    result = len(supports.difference(single_supporter))
else:
    result = 0
    for brick in set(bricks).difference(supports.difference(single_supporter)):
        # get the blocks dependent on this block
        dependencies = set()
        queue = deque([brick])
        while queue:
            x = queue.popleft()
            queue.extend(supports_dict[x].difference(dependencies))
            dependencies.update(supports_dict[x])

        # remove blocks that have a backup plan; ie still have route to ground
        dep_copy = dependencies.copy()
        for dep in dependencies:
            sources = set()
            queue = deque([dep])
            while queue:
                x = queue.popleft()
                if min(x.zs) == 1:
                    dep_copy.discard(dep)
                    break
                queue.extend(supported_by_dict[x].difference(sources).difference({brick}))  # exclude removed block
                sources.update(supported_by_dict[x])
        result += len(dep_copy)


if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)