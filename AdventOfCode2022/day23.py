# Advent of Code 2022 Day 23
# Author:   Rachael Judy
# Date:     12/23/22
# Purpose:  keep spreading out elves until sufficiently spaced given scatter rules

import parseMod
import time

stage = 'b'
day = 23
year = 2022
parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row(f"data/{str(day).zfill(2)}data.csv")
start = time.time()

elves = set()
for x in range(len(data)):
    for y in range(len(data[0])):
        if data[x][y] == '#':
            elves.add((x, y))


def move(positions: set, rounds: int) -> int:
    # elf to check, offset to know where to start in the NSWE checks
    def check_positions(elf: tuple[int, int], offset: int):
        if len(positions.intersection({(elf[0] - 1, elf[1] - 1), (elf[0] - 1, elf[1]), (elf[0] - 1, elf[1] + 1),
                                       (elf[0], elf[1] - 1), (elf[0], elf[1] + 1), (elf[0] + 1, elf[1] - 1),
                                       (elf[0] + 1, elf[1]), (elf[0] + 1, elf[1] + 1)})):
            checks = [  # N, S, W, E
                lambda elf: (elf[0] - 1, elf[1]) if not len(positions.intersection(
                    {(elf[0] - 1, elf[1] - 1), (elf[0] - 1, elf[1]), (elf[0] - 1, elf[1] + 1)})) else elf,
                lambda elf: (elf[0] + 1, elf[1]) if not len(positions.intersection(
                    {(elf[0] + 1, elf[1] - 1), (elf[0] + 1, elf[1]), (elf[0] + 1, elf[1] + 1)})) else elf,
                lambda elf: (elf[0], elf[1] - 1) if not len(positions.intersection(
                    {(elf[0] - 1, elf[1] - 1), (elf[0], elf[1] - 1), (elf[0] + 1, elf[1] - 1)})) else elf,
                lambda elf: (elf[0], elf[1] + 1) if not len(positions.intersection(
                    {(elf[0] - 1, elf[1] + 1), (elf[0], elf[1] + 1), (elf[0] + 1, elf[1] + 1)})) else elf]
            for i in range(4):
                if checks[(i + offset) % 4](elf) != elf:
                    return checks[(i + offset) % 4](elf)
        return elf

    for r in range(rounds):
        proposed, multiple = dict(), set()
        for elf_pos in positions:
            elf_proposed = check_positions(elf_pos, r)
            if elf_proposed in proposed:
                multiple.add(elf_proposed)
            elif elf_proposed != elf_pos:
                proposed[elf_proposed] = elf_pos
        if len(proposed) == 0:
            break
        for new_pos in proposed:
            if new_pos not in multiple:
                positions.remove(proposed[new_pos])
                positions.add(new_pos)

    return r


if stage == 'a':
    move(elves, 10)
    min_x, max_x = min(x for x, _ in elves), max(x for x, _ in elves)
    min_y, max_y = min(y for _, y in elves), max(y for _, y in elves)
    result = (max_y - min_y + 1) * (max_x - min_x + 1) - len(elves)
else:
    result = move(elves, 10000) + 1

print(f"Time: {time.time() - start}")
print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
