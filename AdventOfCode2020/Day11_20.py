# Advent of Code 2020 - Day 11

# Author:   Rachael Judy
# Date:     12/11/2020
# Purpose:  Find arrangement of seats after changes stop, changes based on occupied seats around the seat in focus
#           For phase 1, direct adj, for phase 2, line of sight adjacent - set phase at comment

import copy
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# SET PHASE HERE
phase = 2


# get adjacencies based on phase
def count_adj(row, col, seating, phase=1):
    if phase == 1:  # check only direct adj
        adj = 0 + (seating[row - 1][col - 1] == '#') + (seating[row - 1][col] == '#') + (seating[row - 1][col + 1] == '#') \
              + (seating[row][col - 1] == '#') + (seating[row][col + 1] == '#') \
              + (seating[row + 1][col - 1] == '#') + (seating[row + 1][col] == '#') + (seating[row + 1][col + 1] == '#')
    elif phase == 2:  # check line of sight adj
        adj = 0 + check_direction(-1, -1, row, col, seating) + check_direction(-1, 0, row, col, seating) + \
              check_direction(-1, 1, row, col, seating) + check_direction(0, 1, row, col, seating) + \
              check_direction(1, 1, row, col, seating) + check_direction(1, 0, row, col, seating) + \
              check_direction(1, -1, row, col, seating) + check_direction(0, -1, row, col, seating)

    return adj


# check for adjacent by line of sight -  i is x shift, j is y shift
def check_direction(i, j, row, col, seating):
    not_seen = True
    inci, incj = i, j
    adj = 0

    # iterate through until finds seat or runs out of spots to look at
    while not_seen and 0 <= row+j < len(seating) and 0 <= col+i < len(seating[0]):
        # if a seat is found, add an adjacency if occupied
        if seating[row + j][col + i] == 'L' or seating[row + j][col + i] == '#':
            not_seen = False
            adj = seating[row + j][col + i] == '#'

        i += inci
        j += incj

    return adj


# get input
seating = parseMod.readCSV_row('data/11seats.csv')

# add a border of "floor" around so to eliminate corner adj complications
for row in range(len(seating)):
    seating[row] += '.'
    seating[row] = '.' + seating[row]
seating.insert(0, '')
seating.append('')
for i in range(len(seating[1])):
    seating[0] += '.'
    seating[len(seating)-1] += '.'

# display initial arrangement
for row in seating:
    print(row)

# determine how many seats are occupied after change stops
not_changed = False
while not not_changed:
    not_changed = True
    seating_new = [['.' for _ in range(len(seating[0]))] for j in range(len(seating))]  # reset

    # adjust each seat in the grid
    for row in range(1, len(seating)-1):
        for col in range(1, len(seating[0]) - 1):
            adj = count_adj(row, col, seating, phase)

            # adjust based on adj
            if seating[row][col] == 'L' and adj == 0:
                seating_new[row][col] = '#'
                not_changed = False
            elif seating[row][col] == '#' and adj >= 3+phase:  # 4 seats for phase 1, 5 for 2
                seating_new[row][col] = 'L'
                not_changed = False
            else:
                seating_new[row][col] = seating[row][col]
    seating = copy.deepcopy(seating_new)

# determine number of occupied seats at end
occupied_count = 0
for row in seating:
    for seat in row:
        occupied_count += (seat == '#')

# display
print("Phase", phase, ": ", occupied_count)
