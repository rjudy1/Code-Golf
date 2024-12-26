# Advent of Code 2024 Day 22
# Author:   Rachael Judy
# Purpose:  find secret numbers from series of operations (lsfr option), locate change series leading to highest payout

import collections
import csv
import parseMod

ready = False
day = 22
stage = 'a'  # 14691757043, 1831
year = 2024

parseMod.createDataFile(year=year, day=day)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    secret_numbers = [int(row[0]) for row in csv.reader(file)]

sequence_values = collections.defaultdict(int)
for i, num in enumerate(secret_numbers):
    change_queue, assessed = collections.deque(), set()
    for _ in range(2000):  # could collapse the process to single layer 24 bit lsfr
        stage1 = ((secret_numbers[i] << 6) ^ secret_numbers[i]) % 2**24  # shifts left by 6 bits, mix, prune
        stage2 = ((stage1 >> 5) ^ stage1) % 2**24  # shifts right by 5, mix, prune
        stage3 = ((stage2 << 11) ^ stage2) % 2**24  # shift left by 11, mix, prune
        change_queue.append(stage3 % 10 - secret_numbers[i] % 10)
        secret_numbers[i] = stage3
        if len(change_queue) > 4:
            change_queue.popleft()
            if tuple(change_queue) not in assessed:
                sequence_values[tuple(change_queue)] += stage3 % 10
            assessed.add(tuple(change_queue))

result = sum(secret_numbers) if stage == 'a' else max(sequence_values.values())

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
