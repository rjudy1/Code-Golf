# Advent of Code 2023 Day 14
# Author:   Rachael Judy
# Date:     12/14/23
# Purpose:  roll rocks fully in direction based on rotation; look for pattern of states
# not optimal, could improve with clean tilt, rotate pattern and count Os to a # or edge, not doing it today though

import parseMod

ready = True
day = 14
stage = 'a'
year = 2023

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")


def slide(state, direction):  # instead of manually iterating each, count Os to # and stack them to make O(N^2)
    map_copy = [[state[i][j] if state[i][j] == '#' else '.' for j, col in enumerate(row)] for i, row in
                enumerate(state)]
    dirs = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
    for i in range(0 if direction == 'N' else len(data) - 1, len(data) if direction == 'N' else -1,
                   1 if direction == 'N' else -1):  # need to roll closest to direction of pull first
        for j in range(0 if direction == 'W' else len(data[i]) - 1, len(data[i]) if direction == 'W' else -1,
                       1 if direction == 'W' else -1):
            dr, dc = dirs[direction]
            if state[i][j] == 'O':  # O as in Octopus not 0 dollars
                r, c = i, j
                while 0 <= r < len(state) and 0 <= c < len(state[i]) and map_copy[r][c] == '.':
                    r += dr
                    c += dc
                if r != i or c != j:
                    r -= dr
                    c -= dc
                map_copy[r][c] = 'O'
    return map_copy


if stage == 'a':
    final = slide(data, 'N')
else:
    saved_states, cycling = list(), set()
    iterations = 1000000000
    for iteration in range(iterations):
        for direction in ['N', 'W', 'S', 'E']:
            data = slide(data, direction)

        state_str = ''.join(''.join(row) for row in data)
        if state_str in saved_states:
            if saved_states.index(state_str) in cycling:
                break
            else:
                cycling.add(saved_states.index(state_str))
        else:
            saved_states.append(state_str)
    # get index of what will be the final state and convert back to list
    final = [saved_states[(iterations - min(cycling) - 1) % (max(cycling) - min(cycling) + 1) + min(cycling)]
             [i:i+len(data[0])] for i in range(0, len(saved_states[0]), len(data[0]))]

result = sum(sum((len(data) - i) if col == 'O' else 0 for j, col in enumerate(row)) for i, row in enumerate(final))
if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
