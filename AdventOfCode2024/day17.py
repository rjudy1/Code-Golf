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
split_program = text_program.split(',')
program = split_program
program = [(int(program[i]), int(program[i+1])) for i in range(0, len(program), 2)]
# regA = int(registers[0].split()[-1])
# regB = int(registers[1].split()[-1])
# regC = int(registers[2].split()[-1])

longest_match = dict()
# for i in range(35184372088832,281474976710656):
import multiprocessing
def compute(a):
    #
    # regA = 35184372088831 #51866868655852
    if stage == 'b':
        regA = a
    outputs = list()
    result = ''
    pointer = 0
    regB, regC = 0, 0
    while pointer < len(program):
        instr, op = program[pointer]
        if op == 4:
            combo_op = regA
        elif op == 5:
            combo_op = regB
        elif op == 6:
            combo_op = regC
        # elif op == 7:
        #     print("ERRR")
        else:
            combo_op = op

        # print(instr,end=',')

        if instr == 0:  # adv
            regA //= 2 ** combo_op
        elif instr == 1:  # bxl
            regB ^= op
        elif instr == 2:  # bst
            regB = combo_op % 8
        elif instr == 3 and regA != 0:  # jnz
            pointer = op - 1
        elif instr == 4:  # bxc
            regB ^= regC
        elif instr == 5:  # out
            if stage == 'b' and (split_program[len(outputs)] != str(combo_op % 8) or len(outputs) == len(split_program)):
                # print('djk')
                break
            outputs.append(str(combo_op % 8))
            # print(regB)
            # result = ','.join([result, str(operand%8)])
            # print(operand % 8)
        elif instr == 6:  # bdv
            regB = regA // 2 ** combo_op
        elif instr == 7:  # cdv
            regC = regA // 2 ** combo_op
        pointer += 1
        if stage == 'b' and len(outputs) > len(split_program):
            break
        # print(','.join(outputs))
        if  ','.join(outputs) == text_program:
            return a
        else:
            return 'b'
        # return ','.join(outputs)

# # greater than 85184372088832, less than 185184372088832
# import multiprocessing
# if __name__ == '__main__':
#     with multiprocessing.Pool(100000) as p:
#         print(p.map(compute, [i for i in range(281474976710656, 35184372088832, -1)]))
# # 35184372088832


for i in range(185184372088832, 85184372088832, -1):

    #
    # regA = 35184372088831 #51866868655852
    if stage == 'b':
        regA = i
    outputs = list()
    result = ''
    pointer = 0
    while pointer < len(program):
        instr, op = program[pointer]
        if op == 4:
            combo_op = regA
        elif op == 5:
            combo_op = regB
        elif op == 6:
            combo_op = regC
        # elif op == 7:
        #     print("ERRR")
        else:
            combo_op = op

        # print(instr,end=',')

        if instr == 0:  # adv
            regA //= 2 ** combo_op
        elif instr == 1:  # bxl
            regB ^= op
        elif instr == 2:  # bst
            regB = combo_op % 8
        elif instr == 3 and regA != 0:  # jnz
            pointer = op - 1
        elif instr == 4:  # bxc
            regB ^= regC
        elif instr == 5:  # out
            if stage == 'b' and (
                    split_program[len(outputs)] != str(combo_op % 8) or len(outputs) == len(split_program)):
                # print('djk')
                break
            outputs.append(str(combo_op % 8))
            # print(regB)
            # result = ','.join([result, str(operand%8)])
            # print(operand % 8)
        elif instr == 6:  # bdv
            regB = regA // 2 ** combo_op
        elif instr == 7:  # cdv
            regC = regA // 2 ** combo_op
        pointer += 1
        if stage == 'b' and len(outputs) > len(split_program):
            break
        # print(','.join(outputs))


    result = ','.join(outputs)
    # print()
    # if result not in longest_match:
    #     longest_match[result] = i
    # elif len(result) > 2:
    #     print(longest_match[result] - i, len(result))
    #     longest_match[result] = i
    print(i,  len(outputs), result)
    if stage == 'a':
        break
    elif stage == 'b' and result == text_program:
        result = i
        break





    # if not ready:
    #     print(f'result: \n{result}')
    # elif ready:
    #     print("SUBMITTING RESULT: ", result)
    #     parseMod.submit(result, part=stage, day=day, year=year)
