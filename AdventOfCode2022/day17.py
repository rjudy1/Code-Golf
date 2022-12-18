# Advent of Code 2022 Day 17
# Author:   Rachael Judy
# Date:     12/17/22
# Purpose:  straight simulate tetris placement until repetition with bfs hash, then finish after repeats

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
is_open = lambda x, y, occupied: 0 <= x < 7 and y >= 0 and (x, y) not in occupied


def place_block(jet, piece, max_height, occupied):
    x, y = 2, max_height + 4
    can_move = lambda piece_i, x, y: all(is_open(x + dx, y + dy, occupied) for dx, dy in blocks[piece_i])
    while True:
        # jet fueled movement and vertical drop if possible
        x += jets[jet] if can_move(piece, x+jets[jet], y) else 0
        jet = (jet + 1) % len(jets)
        if can_move(piece, x, y-1):
            y -= 1
        else:
            occupied.update([(x+dx, y+dy) for (dx, dy) in blocks[piece]])
            break
    # return new position in jets and max_height to save running through old data
    return jet % len(jets), max(max_height, max(y for _, y in [(x+dx, y+dy) for (dx, dy) in blocks[piece]]))


def hash_view(occupied, maxy, max_hash_size=25):
    exp, ind = [(0, 0)], 0
    while ind != len(exp):
        for p in ((exp[ind][0], exp[ind][1]-1), (exp[ind][0]-1, exp[ind][1]), (exp[ind][0]+1, exp[ind][1])):
            if 0 <= p[0] < 7 and p[1]+maxy+1 >= 0 and (p[0], maxy+1+p[1]) not in occupied and (p[0], p[1]) not in exp:
                exp.append(p)
        if len(exp) > max_hash_size: break
        ind += 1
    return tuple(exp) if len(exp) <= max_hash_size else None


def solve(count):
    occupied, cycles = set(), dict()
    jet, maxy, piece, additional = 0, -1, 0, 0
    while count > 0:
        # simulate
        jet, maxy = place_block(jet, piece % len(blocks), maxy, occupied)
        count -= 1
        piece = (piece + 1) % len(blocks)

        # hash and cache
        ground = hash_view(occupied, maxy, 12)  # must at least hash 7 around peak for my input
        if ground is None: continue
        elif (jet, piece, ground) in cycles:
            old_maxy, old_count = cycles[jet, piece, ground]
            additional += (maxy - old_maxy) * (count // (old_count - count))  # height increase caught in cycles
            count %= cycles[jet, piece, ground][1] - count  # takes to end of this cycle as we're counting down
        cycles[jet, piece, ground] = (maxy, count)

    return maxy + additional


if stage == 'a':
    result = solve(2022) + 1
else:
    result = solve(1000000000000) + 1

print(f"Time: {time.time() - start}")
print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
