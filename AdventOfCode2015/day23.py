# Advent of Code 2015 Day 23
# Author:   Rachael Judy
# Purpose:  super basic cpu

import parseMod

ready = False
day = 23
stage = 'b'
year = 2015

parseMod.createDataFile(year=year, day=day)
program = parseMod.readCSV_rowEl(f'data/{day:02d}data.csv', ' ')

regs, pc = {'a': stage=='b', 'b': 0}, 0
while 0 <= pc < len(program):
    op, *args = program[pc]
    args = [a.strip(',') for a in args]
    match op:
        case 'hlf': regs[args[0]] //= 2
        case 'tpl': regs[args[0]] *= 3
        case 'inc': regs[args[0]] += 1
        case 'jmp': pc += int(args[0]) - 1
        case 'jie' if regs[args[0]] % 2 == 0: pc += int(args[1]) - 1
        case 'jio' if regs[args[0]] == 1:     pc += int(args[1]) - 1
    pc += 1
result = regs['b']

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
