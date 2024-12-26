# Advent of Code 2024 Day 15
# Author:   Rachael Judy
# Purpose:  lanternfish again, robot pushing single and double wide boxes

import collections
import parseMod

ready = True
day = 15
stage = 'b'  # 1487337, 1521952
year = 2024

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_chunk('data/15data.csv')
warehouse = collections.defaultdict(str)
for i, row in enumerate(data[0]):
    for j, col in enumerate(row):
        if stage == 'a':
            warehouse[complex(i, j)] = col
            if col == '@':
                robot = complex(i, j)
        else:  # part b double width of everything except robot
            warehouse[complex(i, 2 * j)] = col
            warehouse[complex(i, 2 * j + 1)] = col
            if col == '@':
                warehouse[complex(i, 2 * j)] = '.'
                warehouse[complex(i, 2 * j + 1)] = '.'
                robot = complex(i, 2 * j)
            elif col == 'O':
                warehouse[complex(i, 2 * j)] = '['
                warehouse[complex(i, 2 * j + 1)] = ']'

directions = {'>': 1j, '^': -1, '<': -1j, 'v': 1}
for instr in ''.join(data[1]):
    # try to move robot in direction, check blocks and wall
    pos = robot
    relevant_boxes = dict()
    if stage == 'a' or directions[instr].real == 0:  # normal behavior left to right regardless of width
        while warehouse[pos] != '#':  # until wall hit
            pos += directions[instr]
            if warehouse[pos] == 'O' or warehouse[pos] == '[' or warehouse[pos] == ']':  # box
                relevant_boxes[pos] = warehouse[pos]
            elif warehouse[pos] == '.':  # shift the boxes and robot
                for box in relevant_boxes:
                    warehouse[box + directions[instr]] = relevant_boxes[box]
                warehouse[robot] = '.'
                robot += directions[instr]
                break
    else:  # up down, must check above all boxes that will be shifted
        layer_queue = collections.deque([pos])  # check in direction from every position in deque, storing boxes found
        blocked = False
        while layer_queue:
            target = layer_queue.popleft()
            target += directions[instr]
            if warehouse[target] == '[':  # box
                relevant_boxes[target] = warehouse[target]
                relevant_boxes[target + 1j] = warehouse[target + 1j]
                layer_queue.extend({target, target + 1j})
            elif warehouse[target] == ']':
                relevant_boxes[target] = warehouse[target]
                relevant_boxes[target - 1j] = warehouse[target - 1j]
                layer_queue.extend({target, target - 1j})
            elif warehouse[target] == '#':  # wall, can't move, don't update position
                blocked = True
                break
        if not blocked:
            for box in relevant_boxes:  # fill gaps with empty floor
                warehouse[box] = '.'
            for box in relevant_boxes:  # move all boxes up/down
                warehouse[box + directions[instr]] = relevant_boxes[box]
            warehouse[robot] = '.'
            robot += directions[instr]

result = int(sum(sq.real * 100 + sq.imag if warehouse[sq] == '[' or warehouse[sq] == 'O' else 0 for sq in warehouse))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
