# Advent of Code 2018 - Day 18

# Author:   Rachael Judy
# Date:     12/26/2020
# Purpose:  Use checks to determine opcodes and build computer with 16 instruction ISA

import copy
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


def parse_check(inp, ptr, checks):  # process each check, converting to int each argument and putting in array form
    if 'Before' not in inp[ptr]:
        return False

    before = inp[ptr].split()
    for i,x in enumerate(before[1:]):
        x = x.strip('[,]')
        before[i] = int(x)
    before = before[:-1]

    line = inp[ptr+1].split()
    instructions = [int(line[0]), int(line[1]), int(line[2]), int(line[3])]

    after = inp[ptr+2].split()
    for i,x in enumerate(after[1:]):
        x = x.strip('[,]')
        after[i] = int(x)
    after = after[:-1]

    checks.append([instructions, before, after])  # checks will have tuples (instructions, before state, after state)
    return True


class Computer:
    def __init__(self, instructions):
        self.instructions = instructions
        self.registers = [0, 0, 0, 0]

        # opcode to name pairing - dict is number : name - initially empty, but set for next time use
        self.opcode = {0: 'eqir', 7: 'eqri', 11: 'eqrr', 13: 'gtri', 10: 'gtrr', 2: 'gtir', 3: 'setr',
                       9: 'bani', 15: 'banr', 5: 'seti', 4: 'mulr', 14: 'borr', 8: 'bori', 1: 'addi',
                       12: 'addr', 6: 'muli'}
        self.executions = {  # used by process()
            'addr' : lambda line: self.registers[line[1]] + self.registers[line[2]],
            'addi' : lambda line: self.registers[line[1]] + line[2],
            'mulr' : lambda line: self.registers[line[1]] * self.registers[line[2]],
            'muli' : lambda line: self.registers[line[1]] * line[2],
            'banr' : lambda line: self.registers[line[1]] & self.registers[line[2]],
            'bani' : lambda line: self.registers[line[1]] & line[2],
            'borr' : lambda line: self.registers[line[1]] | self.registers[line[2]],
            'bori' : lambda line: self.registers[line[1]] | line[2],
            'setr' : lambda line: self.registers[line[1]],
            'seti' : lambda line: line[1],
            'gtir' : lambda line: int(line[1] > self.registers[line[2]]),
            'gtri' : lambda line: int(self.registers[line[1]] > line[2]),
            'gtrr' : lambda line: int(self.registers[line[1]] > self.registers[line[2]]),
            'eqir' : lambda line: int(line[1] == self.registers[line[2]]),
            'eqri' : lambda line: int(self.registers[line[1]] == line[2]),
            'eqrr' : lambda line: int(self.registers[line[1]] == self.registers[line[2]])
        }

    def process(self):
        for line in self.instructions:
            cmd = self.opcode[line[0]] if str(line[0]).isnumeric() else line[0]
            self.registers[line[3]] = self.executions[cmd](line)


# process input
inp = parseMod.readCSV_row('data/16data.csv', '\n')
line_ptr = 0

checks = []  # contains a list with (opcode, before registers, after conditions)
while parse_check(inp, line_ptr, checks):  # gets all the checks
    line_ptr += 3

program = []  # tuple of op code, A, B, C
for line in inp[line_ptr:]:  # collects the actual program
    line = line.split()
    program.append((int(line[0]), int(line[1]), int(line[2]), int(line[3])))


# create a computer, process the checks and keep lists of ones being used by each opcode
computer = Computer([])
opcode_options = {'addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori',
                'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr'}
opcode_list = [copy.deepcopy(opcode_options) for _ in range(16)]
for check in checks:
    possibilities = []
    opcode_num = check[0][0]
    for name in opcode_options:
        check[0][0] = name  # try each operation

        computer.instructions, computer.registers = [check[0]], copy.deepcopy(check[1])
        computer.process()
        if computer.registers == check[2]:  # keep the options that match
            possibilities.append(name)

    opcode_list[opcode_num] &= set(copy.deepcopy(possibilities))  # reduce set to include only possibilities with opcode
    check.append(copy.deepcopy(possibilities))

print('part 1: ', sum(len(ch[3]) >= 3 for ch in checks))  # count the tests with more than or equal to three opcodes

for _ in range(16):  # go through and assign opcodes by elimination
    for index, op in enumerate(opcode_list):
        if len(op) == 1:
            computer.opcode[index] = op.pop()  # assign to computer
            for i, other_op in enumerate(opcode_list):  # remove from other opcode options
                if computer.opcode[index] in other_op:
                    opcode_list[i].remove(computer.opcode[index])
            break  # find the next set with only one

computer.registers = [0, 0, 0, 0]
computer.instructions = program
computer.process()
print('part 2:', computer.registers[0])
