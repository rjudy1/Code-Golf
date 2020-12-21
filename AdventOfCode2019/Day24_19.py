# Advent of Code 2019 - Day 24

# Author:   Rachael Judy
# Date:     12/12/2020
# Purpose:  Compute the biodiversity at pattern repeat (part 1)
#           Compute the number of bugs in a recursive layout of the grids (part 2)

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# ASSIGN PART HERE
part = 2


# I really hate this function for pure trashiness in if statements and should make it better at some point
# but its late at night now - its inefficiency/overuse is disgusting
def compute_adj_part_2(bug_arrays, adj_arrays):
    for array in range(1, len(bug_arrays)-1):  # check each array (should never use endpoints)
        # iterate over grid
        for row in range(len(bugs)):
            for spot in range(len(bugs[0])):
                adj = 0
                if row == 0:  # top - check below in self and above in recursive
                    adj += (bug_arrays[array-1][1][2] == '#') + (bug_arrays[array][row+1][spot] == '#')
                    if spot == 0:  # top left
                        adj += (bug_arrays[array-1][2][1] =='#') + (bug_arrays[array][row][spot+1] == '#')
                    elif spot == 4:  # top right
                        adj += (bug_arrays[array-1][2][3] =='#') + (bug_arrays[array][row][spot-1] == '#')
                    else: # top none
                        adj += (bug_arrays[array][row][spot-1] == '#') + (bug_arrays[array][row][spot+1] == '#')
                elif row == 4:  # bottom row - check above recursive
                    adj += (bug_arrays[array-1][3][2] == '#') + (bug_arrays[array][row-1][spot] == '#')
                    if spot == 0:  # bottom left
                        adj += (bug_arrays[array-1][2][1] == '#') + (bug_arrays[array][row][spot+1] == '#')
                    elif spot == 4:  # bottom right
                        adj += (bug_arrays[array-1][2][3] == '#') + (bug_arrays[array][row][spot-1] == '#')
                    else:  # bottom none - check left, right
                        adj += (bug_arrays[array][row][spot-1] == '#') + (bug_arrays[array][row][spot+1] == '#')
                elif spot == 0:  # left side
                    adj += (bug_arrays[array-1][2][1] == '#') + (bug_arrays[array][row][spot+1] == '#') \
                           + (bug_arrays[array][row+1][spot] == '#') + (bug_arrays[array][row-1][spot] == '#')
                elif spot == 4:  # right side
                    adj += (bug_arrays[array-1][2][3] == '#') + (bug_arrays[array][row][spot-1] == '#') \
                           + (bug_arrays[array][row+1][spot] == '#') + (bug_arrays[array][row-1][spot] == '#')

                # no recursive adj
                elif (spot == 1 or spot == 3) and (row == 1 or row == 3):
                    adj += (bug_arrays[array][row + 1][spot] == '#') + (bug_arrays[array][row - 1][spot] == '#') \
                           + (bug_arrays[array][row][spot - 1] == '#') + (bug_arrays[array][row][spot + 1] == '#')

                # around center grid
                elif row == 2 and spot == 3:  # right of center
                    adj += (bug_arrays[array][row + 1][spot] == '#') + (bug_arrays[array][row - 1][spot] == '#') \
                           + (bug_arrays[array][row][spot + 1] == '#')
                    for i in range(len(bug_arrays[array+1])):
                        adj += (bug_arrays[array+1][i][4] == '#')
                elif row == 2 and spot == 1:  # left of center
                    adj += (bug_arrays[array][row + 1][spot] == '#') + (bug_arrays[array][row - 1][spot] == '#') \
                           + (bug_arrays[array][row][spot - 1] == '#')
                    for i in range(len(bug_arrays[array+1])):
                        adj += (bug_arrays[array+1][i][0] == '#')
                elif row == 1 and spot == 2:  # top of center
                    adj += (bug_arrays[array][row - 1][spot] == '#') + (bug_arrays[array][row][spot+1] == '#') \
                           + (bug_arrays[array][row][spot - 1] == '#') + (bug_arrays[array+1][0].sea_monster_count('#'))
                elif row == 3 and spot == 2:  # bottom of center
                    adj += (bug_arrays[array][row + 1][spot] == '#') + (bug_arrays[array][row][spot + 1] == '#') \
                           + (bug_arrays[array][row][spot - 1] == '#') + (bug_arrays[array+1][4].sea_monster_count('#'))

                # assign to parallel spot
                adj_arrays[array][row][spot] = adj


# perform the simulation based on adjacencies provided
def simulate(bugs, adjacencies, border=0):
    exponent = 0
    bio_score = 0  # track biodiversity score for part 1

    for row in range(border, len(bugs) - border):
        for spot in range(border, len(bugs[0]) - border):
            if bugs[row][spot] == '#' and adjacencies[row][spot] != 1:
                bugs[row][spot] = '.'  # becomes empty if not one bug
            elif bugs[row][spot] == '.' and (adjacencies[row][spot] == 1 or adjacencies[row][spot] == 2):
                bugs[row][spot] = '#'

            bio_score += (pow(2, exponent) * (bugs[row][spot] == '#'))
            exponent += 1

    return bio_score


# read input into arrays
bugs = parseMod.readCSV_row('data/24bugs.csv')
for row in range(len(bugs)):
    temp = []
    for item in bugs[row]:
        temp.append(item)
    bugs[row] = temp

if part == 1:
    # surround with comma border
    for x in range(len(bugs)):
        bugs[x].insert(0, '|')
        bugs[x].append('|')
    bugs.insert(0, ['|' for i in range(len(bugs[0]))])
    bugs.append(['|' for i in range(len(bugs[0]))])

    # create adj calculations
    adjacencies = [[0 for i in range(len(bugs[0]))] for j in range(len(bugs))]
    saved_scores = []
    while True:  # iterates until finds same diversity score again
        # compute adjacencies
        for row in range(1, len(bugs) - 1):
            for spot in range(1, len(bugs[0]) - 1):
                adjacencies[row][spot] = (bugs[row+1][spot] == '#') + (bugs[row-1][spot] == '#') \
                      + (bugs[row][spot - 1] == '#') + (bugs[row][spot + 1] == '#')

        # run the adjacency changes
        bio_score = simulate(bugs, adjacencies, 1)
        if bio_score in saved_scores:
            break
        else:
            saved_scores.append(bio_score)

    print("Part 1 bio_score: ", bio_score)

else:  # phase 2
    # create the array of bug tile arrays and adjacency arrays
    bug_arrays = [[['.' for i in range(5)] for j in range(5)] for k in range(220)]
    adj_arrays = [[[0 for i in range(5)] for j in range(5)] for k in range(220)]
    bug_arrays[110] = bugs  # start it off with sample in center

    # perform 200 minutes
    for i in range(200):
        # compute adjacencies for all applicable
        compute_adj_part_2(bug_arrays, adj_arrays)

        # simulate on each level
        for j in range(len(bug_arrays)):  # could just zip over both b
            simulate(bug_arrays[j], adj_arrays[j])

    # sea_monster_count bugs at end
    count = 0
    for bug_array in bug_arrays:
        for array in bug_array:
            count += array.count('#')

    print("Part 2 bug sea_monster_count: ", count)