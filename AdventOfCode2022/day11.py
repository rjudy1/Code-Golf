# Advent of Code 2022 Day 11
# Author:   Rachael Judy
# Date:     12/11/22
# Purpose:  passing numbers, have to reduce scale by mod of LCM of moduli (chinese remainder theorem ftw)

import math
import parseMod
import time

start = time.time()
stage = 'b'
day = 11
year = 2022
parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")


class Monkey:
    def __init__(self, op='*', operand=0, mod=0, target_true=0, target_false=0, items=None):
        if items is None:
            items = []
        self.items = items
        self.op = op
        self.operand = operand
        self.mod = mod
        self.target = [target_true, target_false]
        self.count = 0

    # return map of target, item to be passed to
    def select_targets(self, divisor=1, common_mod=1000000000000000000):
        target_item_map = []
        for j in range(len(self.items)):
            if self.op == '*':
                new_value = int((self.items[j] * self.operand) / divisor)
            elif self.op == '+':
                new_value = int((self.items[j] + self.operand) / divisor)
            else:
                new_value = int(pow(self.items[j], self.operand) / divisor)
            # add new_value, adjusted downward through modulus at provided target based on test
            target_item_map.append((self.target[bool(new_value % self.mod)], new_value % common_mod))

        self.count += len(self.items)
        self.items.clear()
        return target_item_map


# parsing
monkeys = []
for i in range(0, len(data), 6):
    op = data[i + 2].strip().split(' ')[4] if data[i+2].strip().split(' ')[5] != 'old' else 's'
    operand = int(data[i+2].strip().split(' ')[5]) if data[i+2].strip().split(' ')[5] != 'old' else 2
    start_state = [int(num.strip(',')) for num in data[i+1].strip().split(' ')[2:]]
    monkeys.append(Monkey(op=op, operand=operand,
                          mod=int(data[i + 3].strip().split(' ')[3]),
                          target_true=int(data[i+4].strip().split(' ')[5]),
                          target_false=int(data[i+5].strip().split(' ')[5]),
                          items=start_state
                          ))

mod = math.prod(m.mod for m in monkeys)
if stage == 'a':
    rounds, div, = 20, 3
else:
    rounds, div = 10000, 1

for _ in range(rounds):
    # go through monkeys, selecting target for each item and assigning to targets
    for monkey in monkeys:
        targets = monkey.select_targets(divisor=div, common_mod=mod)
        for (target, value) in targets:
            monkeys[target].items.append(value)

counts = [m.count for m in monkeys]
counts.sort()
result = counts[-1] * counts[-2]

print("SUBMITTING RESULT: ", result)
print(f"Time: {time.time()-start}")
parseMod.submit(result, part=stage, day=day, year=year)
