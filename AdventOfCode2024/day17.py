# Advent of Code 2024 Day 17
# Author:   Rachael Judy
# Purpose:  alu sim and then find register A value for quine
#           (slow part b with the solver, generalized only for aoc valid inputs not any input register/program format)

from z3 import *
import parseMod

ready = True
day = 17
stage = 'a'  # (2,7,6,5,6,0,2,3,1),  107416870455451
year = 2024

parseMod.createDataFile(year=year, day=day)
registers, program = parseMod.readCSV_chunk("data/" + str(day).zfill(2) + "data.csv")
split_program = list(map(int, program[0].split()[1].split(',')))
regA, regB, regC = int(registers[0].split()[-1]), int(registers[1].split()[-1]), int(registers[2].split()[-1])

# stage a, simple sim
pointer, outputs, constants = 0, list(), list()
while pointer < len(split_program):  # run simulation
    instr, op = split_program[pointer], split_program[pointer+1]
    combo_op = regA if op == 4 else regB if op == 5 else regC if op == 6 else op

    if instr == 0:  # adv
        regA //= 2 ** combo_op
    elif instr == 1:  # bxl
        regB ^= op
        constants.append(op)  # generalizes for the valid aoc inputs since programs are same except constants
    elif instr == 2:  # bst
        regB = combo_op % 8
    elif instr == 3 and regA != 0:  # jnz
        pointer = op - 2
    elif instr == 4:  # bxc
        regB ^= regC
    elif instr == 5:  # out
        outputs.append(str(combo_op % 8))
    elif instr == 6:  # bdv
        regB = regA // 2 ** combo_op
    elif instr == 7:  # cdv
        regC = regA // 2 ** combo_op
    pointer += 2
result = ','.join(outputs)  # part a

upper_limit = 2**(3*len(split_program))-1  # value is between 8**15+1 and 8**16 - 1 so 48 bits by length of the pattern
while True:  # loop until solver fails - ie minimum found
    a = BitVec('a', 3*len(split_program)+1)  # extra bit since solver can't seem to handle 48 with limit
    solver = Solver()
    solver.add(a < upper_limit - 1)  # force to reduce if possible
    for x in split_program:  # same logical operation for everyone except constants
        b = ((a % 8) ^ constants[0]) ^ constants[1] ^ (a / (1 << ((a % 8) ^ constants[0])))
        a /= 8
        solver.add((b % 8) == x)
    solver.add(a == 0)

    if solver.check() == sat:  # if satisfied, try again with lower upper bound
        upper_limit = solver.model()[solver.model().decls()[0]]  # won't let me access a so this is our option
        print(f"Constraints satisfied with A={upper_limit}; attempting to reduce...")
    else:
        break

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
    print(f"RESULT FOR PART B: {upper_limit}.\nPLEASE MANUALLY ENTER SINCE Z3 WON\'T CONVERT")
