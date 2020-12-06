# Advent of Code 2019

# Author:   Rachael Judy
# Date:     12/4/2020
# Purpose:  Intcode program - overall computer useful to be used as package


import queue

class Computer:
    def __init__(self, instr):
        self.array = instr + [0 for i in range(1000)]
        self.base = 0
        self.index = 0
        self.halt = 0

    def isDone(self):
        return self.halt

    # returns address of value that should be used
    def setParams(self):
        # absolute
        x = self.index + 1
        y = self.index + 2
        z = self.index + 3

        if self.array[self.index] % 1000 < 100:  # position addressing
            x = self.array[x]
        elif self.array[self.index] % 1000 >= 200:  # relative addressing
            x = self.array[x] + self.base

        if self.array[self.index] % 10000 < 1000:
            y = self.array[y]
        elif self.array[self.index] % 10000 >= 2000:
            y = self.array[y] + self.base

        if self.array[self.index] % 100000 < 10000:
            z = self.array[z]
        elif self.array[self.index] % 100000 >= 20000:
            z = self.array[z] + self.base

        return x, y, z

    # inputQ needs parameter at front and input at back
    def processInput(self, inputQ):
        output = []

        while self.index < len(self.array):
            x, y, z = self.setParams()
            if self.array[self.index] % 100 == 1:  # add next two params to third
                self.array[z] = self.array[x] + self.array[y]
                self.index += 3

            elif self.array[self.index] % 100 == 2:  # multiply next two params to third
                self.array[z] = self.array[x] * self.array[y]
                self.index += 3

            elif self.array[self.index] % 100 == 3:  # take input to next param
                if inputQ.empty():
                    return output
                self.array[x] = inputQ.get()  # int(input('Enter num: '))
                self.index += 1

            elif self.array[self.index] % 100 == 4:  # print next param
                output.append(self.array[x])
#                print("Output: ", output)  # commented out for cleanness when running
                self.index += 1

            elif self.array[self.index] % 100 == 5:  # jump if true
                if self.array[x]:
                    self.index = self.array[y]
                    self.index -= 1
                else:
                    self.index += 2

            elif self.array[self.index] % 100 == 6:  # jump if false
                if not self.array[x]:
                    self.index = self.array[y]
                    self.index -= 1
                else:
                    self.index += 2

            elif self.array[self.index] % 100 == 7:  # less than
                if self.array[x] < self.array[y]:
                    self.array[z] = 1
                else:
                    self.array[z] = 0
                self.index += 3

            elif self.array[self.index] % 100 == 8:  # equals
                if self.array[x] == self.array[y]:
                    self.array[z] = 1
                else:
                    self.array[z] = 0
                self.index += 3

            elif self.array[self.index] % 100 == 9:  # base + parameter
                self.base += self.array[x]
                self.index += 1

            elif self.array[self.index] % 100 == 99:  # end program
                self.halt = -1
                break

            self.index += 1  # separate in case of garbage numbers
        return output
