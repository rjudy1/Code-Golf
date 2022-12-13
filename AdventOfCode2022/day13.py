# Advent of Code 2022 Day 13
# Author:   Rachael Judy
# Date:     12/13/22
# Purpose:  recursive comparison of nested lists

import parseMod
import time

start = time.time()
stage = 'b'
day = 13
year = 2022
parseMod.createDataFile(year=year, day=day)


class Packet:
    def __init__(self, packet):
        self.packet = packet

    # to use sort
    def __lt__(self, other):
        return self.compare(self.packet.copy(), other.packet.copy())

    # to use index
    def __eq__(self, other):
        return self.packet == other.packet

    # to compare contents of Packets
    def compare(self, llist, rlist) -> int:
        for j in range(min(len(llist), len(rlist))):
            if isinstance(llist[j], int) and isinstance(rlist[j], int):
                if llist[j] > rlist[j]: return 0
                elif llist[j] < rlist[j]: return 1
            else:
                if isinstance(llist[j], int) and isinstance(rlist[j], list):
                    llist[j] = [llist[j]]
                elif isinstance(llist[j], list) and isinstance(rlist[j], int):
                    rlist[j] = [rlist[j]]

                if self.compare(llist[j].copy(), rlist[j].copy()) != -1:
                    return self.compare(llist[j].copy(), rlist[j].copy())

        if len(rlist) == len(llist):
            return -1
        else:
            return len(rlist) > len(llist)


packets = [Packet(eval(row)) for row in parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")]
if stage == 'a':
    result = sum(int(i/2+1) if packets[i] < packets[i+1] else 0 for i in range(0, len(packets), 2))
else:
    packets.extend([Packet([[2]]), Packet([[6]])])
    packets.sort()
    result = (packets.index(Packet([[2]])) + 1) * (packets.index(Packet([[6]])) + 1)

print("SUBMITTING RESULT: ", result)
print(f"Time: {time.time()-start}")
parseMod.submit(result, part=stage, day=day, year=year)
