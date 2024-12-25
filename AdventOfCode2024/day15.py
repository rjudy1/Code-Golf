# Advent of Code 2024 Day 15
# Author:   Rachael Judy
# Purpose:  lanternfish again, part 2 kind of gross so we'll get back to that

import collections
import copy
import csv
import parseMod

ready = True
day = 15
stage = 'b'  # 1487337, 1521952
year = 2024

filename = parseMod.createDataFile(year=year, day=day)
# data = parseMod.readCSV_chunk(filename)
data = parseMod.readCSV_chunk('data/15data.csv')
instructions = ''.join(data[1])
map = collections.defaultdict(str)
bmap = collections.defaultdict(str)
for i, row in enumerate(data[0]):
    for j, col in enumerate(row):
        map[complex(i,j)] = col
        bmap[complex(i, 2*j)] = col
        bmap[complex(i, 2*j + 1)] = col
        if col == '@':
            robot = complex(i,j)
            bmap[complex(i,2*j+1)] = '.'
            brobot = complex(i, 2*j)
        elif col == 'O':
            bmap[complex(i,2*j)] = '['
            bmap[complex(i,2*j+1)] = ']'

# with open("data/" + str(day).zfill(2) + "data.csv") as file:
#     reader = csv.reader(file)
#     # TODO: parse the input into walls, boxes, robot
#     map = [row[0] for row in reader][0]
#     # TODO add walls around border, find max and min positions
directions = {'>': 1j, '^': -1, '<': -1j, 'v': 1}

for instr in instructions:
    # try to move robot in direction, add wall check
    # check blocks in this direction
    pos = robot
    relevant_boxes = set()
    while 0 <= pos.real < len(data[0]) and 0 <= pos.imag <= len(data[0][0]):
        pos += directions[instr]
        if map[pos] == 'O':  # box
            relevant_boxes.add(pos)
        elif map[pos] == '#':  # wall
            # can't move, don't update position
            break
        else:
            for box in relevant_boxes:
                map[box+directions[instr]] = 'O'

            map[robot] = '.'
            robot += directions[instr]
            map[robot] = '@'
            break

result = int(sum(box.real*100+box.imag if map[box] == 'O' else 0 for box in map))
print('a', result)

# part b
directions = {'>': 1j, '^': -1, '<': -1j, 'v': 1}

for instr in instructions:
    # try to move robot in direction, add wall check
    # check blocks in this direction
    pos = brobot
    relevant_boxes = set()
    if directions[instr].real == 0:  #normal behavior left to right
        while 0 <= pos.real < len(data[0]) and 0 <= pos.imag <= len(data[0][0]*2):
            pos += directions[instr]
            if bmap[pos] == '[' or bmap[pos] == ']':  # box
                relevant_boxes.add(pos)
            elif bmap[pos] == '#':  # wall
                # can't move, don't update position
                break
            else:
                bmap_copy = copy.deepcopy(bmap)
                for box in relevant_boxes:
                    bmap[box] = '.'
                for box in relevant_boxes:
                    if bmap_copy[box] == '[':
                        bmap[box+directions[instr]] = '['
                    elif bmap_copy[box] == ']':
                        bmap[box+directions[instr]] = ']'
                    # else:
                    #     bmap[box+directions[instr]] = '@'
                    # bmap[box + directions[instr]] = bmap[box]
                bmap[brobot] = '.'
                brobot += directions[instr]
                bmap[brobot] = '@'
                break
    else:  # up down more extensive check needed
        layer_queue = collections.deque([pos])  # check in direction from every position in deque, storing boxes found
        failure = False
        while layer_queue:
            target = layer_queue.popleft()
            target += directions[instr]
            if bmap[target] == '[':  # box
                relevant_boxes.update({target, target+1j})
                layer_queue.extend({target, target+1j})
            elif bmap[target] == ']':
                relevant_boxes.update({target, target-1j})
                layer_queue.extend({target, target-1j})
            elif bmap[target] == '#':  # wall
                # can't move, don't update position
                failure = True
                break
        if not failure:
            bmap_copy = copy.deepcopy(bmap)
            for box in relevant_boxes:
                bmap[box] = '.'
            for box in relevant_boxes:
                if bmap_copy[box] == '[':
                    bmap[box + directions[instr]] = '['
                elif bmap_copy[box] == ']':
                    bmap[box + directions[instr]] = ']'
                else:
                    bmap[box + directions[instr]] = '@'
                # bmap[box + directions[instr]] = bmap[box]
            bmap[brobot] = '.'
            brobot += directions[instr]
            bmap[brobot] = '@'


    # print(instr)
    # for i in range(len(data[0])):
    #     for j in range(len(data[0][1]*2)):
    #         print(bmap[complex(i,j)], end='')
    #     print()
    # print()
result = int(sum(box.real*100+box.imag if bmap[box] == '[' else 0 for box in bmap))


if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
