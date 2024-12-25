# Advent of Code 2024 Day 17
# Author:   Rachael Judy
# Purpose:  intcode computer again, heck yeah

import csv
import parseMod

ready = True
day = 17
stage = 'b'
year = 2024

# parseMod.createDataFile(year=year, day=day)
# registers, program = parseMod.readCSV_chunk("data/" + str(day).zfill(2) + "data.csv")

text_program = '2,4,1,5,7,5,1,6,4,2,5,5,0,3,3,0'

# text_program = program[0].split()[1]
split_program = list(map(int, text_program.split(',')))
# program = split_program
# # program = [(int(program[i]), int(program[i+1])) for i in range(0, len(program), 2)]
# # regA = int(registers[0].split()[-1])
# # regB = int(registers[1].split()[-1])
# # regC = int(registers[2].split()[-1])
#
# longest_match = dict()
# # for i in range(35184372088832,281474976710656):
# import multiprocessing
# def compute(a):
#     #
#     # regA = 35184372088831 #51866868655852
#     if stage == 'b':
#         regA = a
#     outputs = list()
#     result = ''
#     pointer = 0
#     regB, regC = 0, 0
#     while pointer < len(program):
#         instr, op = program[pointer]
#         if op == 4:
#             combo_op = regA
#         elif op == 5:
#             combo_op = regB
#         elif op == 6:
#             combo_op = regC
#         # elif op == 7:
#         #     print("ERRR")
#         else:
#             combo_op = op
#
#         # print(instr,end=',')
#
#         if instr == 0:  # adv
#             regA //= 2 ** combo_op
#         elif instr == 1:  # bxl
#             regB ^= op
#         elif instr == 2:  # bst
#             regB = combo_op % 8
#         elif instr == 3 and regA != 0:  # jnz
#             pointer = op - 1
#         elif instr == 4:  # bxc
#             regB ^= regC
#         elif instr == 5:  # out
#             if stage == 'b' and (split_program[len(outputs)] != str(combo_op % 8) or len(outputs) == len(split_program)):
#                 # print('djk')
#                 break
#             outputs.append(str(combo_op % 8))
#             # print(regB)
#             # result = ','.join([result, str(operand%8)])
#             # print(operand % 8)
#         elif instr == 6:  # bdv
#             regB = regA // 2 ** combo_op
#         elif instr == 7:  # cdv
#             regC = regA // 2 ** combo_op
#         pointer += 1
#         if stage == 'b' and len(outputs) > len(split_program):
#             break
#         # print(','.join(outputs))
#         if  ','.join(outputs) == text_program:
#             return a
#         else:
#             return 'b'
#         # return ','.join(outputs)

# # greater than 85184372088832, less than 185184372088832
# import multiprocessing
# if __name__ == '__main__':
#     with multiprocessing.Pool(100000) as p:
#         print(p.map(compute, [i for i in range(281474976710656, 35184372088832, -1)]))
# # 35184372088832



from z3 import *



# Create symbolic integer variables
a = BitVec('a', 32)  # 32-bit integer
b = BitVec('b', 32)  # 32-bit integer
c = BitVec('c', 32)  # 32-bit integer

# Create a solver instance
solver = Solver()

for x in [2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0]:
    b = a % 8
    b = b ^ 5
    c = a / (1 << b)
    b = b ^ c
    b = b ^ 6
    a = a / (1 << 3)
    solver.add((b % 8) == x)

# for x in split_program:
#     b = (a % 8)
#     b = b ^ 5
#     c = UDiv(a, (1 << b))  # Unsigned division and left shift
#     b = b ^ 6
#     b = b ^ c
#     a = LShR(a, 3)  # Logical shift right by 3
#     solver.add((b % 8) == x)
solver.add(a == 0)

# Check for bitwise solutions first
if solver.check() == sat:
    print("Bitwise constraints satisfied. Checking additional constraints...")
    # Save bitwise solutions
    bitwise_model = solver.model()
    x_val = bitwise_model[a].as_long()

    print(f"Candidate values: x = {x_val}")
else:
    print("No solution exists for the bitwise constraints.")

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
