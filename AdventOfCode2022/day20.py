# Advent of Code 2022 Day 20
# Author:   Rachael Judy
# Date:     12/20/22
# Purpose:  circular list of numbers shifting

import parseMod
import time

stage = 'b'
day = 20
year = 2022
parseMod.createDataFile(year=year, day=day)
numbers = parseMod.readCSVInts(f"data/{str(day).zfill(2)}data.csv")
start = time.time()


def mix_numbers(nums, times=1, decryption_key=1):
    def render_state():
        final_state = []
        index = list(shifts.keys())[list(shifts.values()).index(0)]
        while len(final_state) != len(nums):
            final_state.append(shifts[index])
            index = neighbor[index]
        return final_state

    shifts = {k: v * decryption_key for k, v in enumerate(nums)}
    neighbor = {n: (n + 1) % len(nums) for n in range(len(nums))}
    for _ in range(times):
        for n in range(len(neighbor)):
            ptr = n
            for i in range(shifts[n] % (len(nums) - 1)):  # - 1 to not include self in wraparound
                ptr = neighbor[ptr]
            if ptr != n:
                neighbor[list(neighbor.keys())[list(neighbor.values()).index(n)] % len(nums)] = neighbor[n]
                neighbor[n], neighbor[ptr] = neighbor[ptr], n
    return render_state()


if stage == 'a':
    mixed = mix_numbers(numbers, 1)
else:
    mixed = mix_numbers(numbers, 10, 811589153)
result = mixed[1000 % len(numbers)] + mixed[2000 % len(numbers)] + mixed[3000 % len(numbers)]

print(f"Time: {time.time() - start}")
print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
