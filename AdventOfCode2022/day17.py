# Advent of Code 2022 Day 17
# Author:   Rachael Judy
# Date:     12/17/22
# Purpose:  tetris with compute where repetition starts (length jets * blocks?)

import parseMod
import time

stage = 'b'
day = 17
year = 2022
parseMod.createDataFile(year=year, day=day)
jets = [1 if x == '>' else -1 for x in parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")[0]]
start = time.time()

blocks = [((0, 0), (1, 0), (2, 0), (3, 0)),
          ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),
          ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
          ((0, 0), (0, 1), (0, 2), (0, 3)),
          ((0, 0), (0, 1), (1, 0), (1, 1))]
open = lambda x, y, occupied: 0 <= x < 7 and y >= 0 and (x, y) not in occupied


def place(occupied, jet, piece, max_height):
    def can_move(piece_i, x, y):
        return all(open(x+dx, y+dy, occupied) for dx, dy in blocks[piece_i])

    x, y = 2, max_height + 4
    while True:
        if can_move(piece, x+jets[jet], y): x += jets[jet]
        jet = (jet + 1) % len(jets)
        if can_move(piece, x, y-1):
            y -= 1
        else:
            occupied.update([(x+dx, y+dy) for (dx, dy) in blocks[piece]])
            break
    return jet%len(jets), max(max_height, max(y for _, y in [(x+dx, y+dy) for (dx, dy) in blocks[piece]]))


def hash_view(occupied, maxy):
    def dfs(x, y, visited):
        # if space is not open or visited already or larger than worth hashing
        if not open(x, maxy+y, occupied) or (x, y) in visited or len(visited) > 1: return
        visited.add((x, y))
        for nx, ny in ((x-1, y), (x+1, y), (x, y-1)):
            dfs(nx, ny, visited)
    state = set()
    for x in range(7):
        dfs(x, 0, state)
    return tuple(state) if len(state) <= 1 else None


def solve(count):
    T, cycles = set(), dict()
    jet, maxy, piece, additional = 0, -1, 0, 0

    while count > 0:
        jet, maxy = place(T, jet, piece % len(blocks), maxy)
        count -= 1
        piece = (piece + 1) % len(blocks)

        ground = hash_view(T, maxy)
        if ground is None: continue
        if (jet, piece, ground) in cycles:
            old_maxy, oldcount = cycles[jet, piece, ground]
            additional += (maxy - old_maxy) * (count // (oldcount - count))
            count %= oldcount - count
        cycles[jet, piece, ground] = (maxy, count)

    return maxy + additional


if stage == 'a':
    result = solve(2022) + 1
else:
    result = solve(1000000000000) + 1

print(f"Time: {time.time() - start}")
print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
