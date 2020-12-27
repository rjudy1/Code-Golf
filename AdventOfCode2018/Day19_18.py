# Advent of Code 2018 - Day 16

# Author:   Rachael Judy
# Date:     12/26/2020
# Purpose:  Add a designed instruction pointer register instruction and optimize assembly to prevent long runtime
# Computer copied from Day 16

import copy
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


class Computer:
    def __init__(self, instructions):
        self.instructions = instructions
        self.registers = [0, 0, 0, 0, 0, 0]
        self.pc = 0
        self.ip = -1

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
        halt = False
        while not halt:
            if self.pc >= len(self.instructions):
                halt = True
                continue

            line = self.instructions[self.pc]

            if '#ip' in line[0]:  # convert the register to a special reg
                self.ip = line[1]
                self.instructions.remove(line)
                continue

            if self.ip != -1:  # handle pc
                self.registers[self.ip] = self.pc

            # special for Day 19 part 2, not for normal computer - otherwise loops for hours
            if self.pc == 2 and self.registers[4] != 0:  # handle the loop incrementing - sums all factors of r2
                while self.registers[4] <= self.registers[2]:  # sum the factors, shortcutting, break after all outer
                    if self.registers[2] % self.registers[4] == 0:  # follows innermost loop, watching for equals to add
                        self.registers[0] += self.registers[4]
                    self.registers[4] += 1  # occurs after each outer loop iteration, starts checking against larger
                self.pc = 13  # exit inner loop
                continue

            # execute normal op
            cmd = self.opcode[line[0]] if str(line[0]).isnumeric() else line[0]
            self.registers[line[3]] = self.executions[cmd](line)

            # reassign pc
            if self.ip != -1:
                self.pc = self.registers[self.ip]
            self.pc += 1


instr = parseMod.readCSV_row('data/19program.csv', '\n')
program = []
for i in instr:
    i = i.split()
    program.append([i[0], int(i[1]), int(i[2]), int(i[3])] if len(i) > 2 else [i[0], int(i[1])])

computer = Computer(copy.deepcopy(program))
computer.process()
print("part 1 registers: ", computer.registers)

computer2 = Computer(copy.deepcopy(program))
computer2.registers = [1, 0, 0, 0, 0, 0]
computer2.process()
print("part 2 registers: ", computer2.registers)
