# Advent of Code 2022 Day 21
# Author:   Rachael Judy
# Date:     12/21/22
# Purpose:  given values and operations down tree, compute value of root function, backtrack to humn for b

import parseMod
import time

stage = 'b'
day = 21
year = 2022
parseMod.createDataFile(year=year, day=day)
monkey_list = parseMod.readCSV_rowEl(f"data/{str(day).zfill(2)}data.csv", ' ')
start = time.time()

flip_ops = {'*': '/', '/': '*', '+': '-', '-': '+'}
monkeys = dict()
while monkeys.get('root' if stage == 'a' else 'humn') is None:
    for m in monkey_list:
        if monkeys.get(m[0][:-1]) is None:  # if value unknown
            if m[1].isnumeric() and not (stage == 'b' and m[0][:-1] == 'humn'):  # don't assign human in stage b
                monkeys[m[0][:-1]] = int(m[1])
            elif monkeys.get(m[1]) is not None and monkeys.get(m[3]) is not None:
                monkeys[m[0][:-1]] = int(eval(f'{monkeys[m[1]]}{m[2]}{monkeys[m[3]]}'))
            elif stage == 'b' and m[0][:-1] == 'root' and monkeys.get(m[3]) is not None: # root should be an assign
                monkeys[m[1]] = monkeys[m[3]]
            elif stage == 'b' and m[0][:-1] == 'root' and monkeys.get(m[1]) is not None:
                monkeys[m[3]] = monkeys[m[3]]
        elif len(m) > 2:  # if result is defined but one of the operands is not and not a simple assign, then
            if monkeys.get(m[1]) is None and monkeys.get(m[3]) is not None:  # do the inverse op for each
                monkeys[m[1]] = int(eval(f'{monkeys[m[0][:-1]]}{flip_ops[m[2]]}{monkeys[m[3]]}'))
            elif monkeys.get(m[1]) is not None and monkeys.get(m[3]) is None:
                monkeys[m[3]] = int(eval(f'{monkeys[m[0][:-1]]}{flip_ops[m[2]]}{monkeys[m[1]]}')) \
                    if m[2] == '*' or m[2] == '+' else int(eval(f'{monkeys[m[1]]}{m[2]}{monkeys[m[0][:-1]]}'))

result = monkeys['root'] if stage == 'a' else monkeys['humn']
print(f"Time: {time.time() - start}")
print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
