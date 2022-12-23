# Advent of Code 2022 Day 19
# Author:   Rachael Judy
# Date:     12/19/22
# Purpose:  maximize geode collection with linear programming (learning about Z3 solver)

import parseMod
import time
from z3 import *

stage = 'a'
day = 19
year = 2022
parseMod.createDataFile(year=year, day=day)
blueprints = parseMod.readCSV_rowEl(f"data/{str(day).zfill(2)}data.csv", ' ')
start = time.time()


def solve(clk, blueprint):
    # amount of each resource at each time
    ore = [Int("ore_{}".format(i)) for i in range(clk + 1)]
    clay = [Int("clay_{}".format(i)) for i in range(clk + 1)]
    obsidian = [Int("obsidian_{}".format(i)) for i in range(clk + 1)]
    geode = [Int("geode_{}".format(i)) for i in range(clk + 1)]

    # robots at each time step
    ore_robots = [Int("ore_r_{}".format(i)) for i in range(clk + 1)]
    clay_robots = [Int("clay_r_{}".format(i)) for i in range(clk + 1)]
    obsidian_robots = [Int("obsidian_r_{}".format(i)) for i in range(clk + 1)]
    geode_robots = [Int("geode_r_{}".format(i)) for i in range(clk + 1)]

    # robots to buy that produce resources at each step
    ore_robots_tobuy = [Int("buy_ore_r_{}".format(i)) for i in range(clk + 1)]
    clay_robots_tobuy = [Int("buy_clay_r_{}".format(i)) for i in range(clk + 1)]
    obsidian_robots_tobuy = [Int("buy_obsidian_r_{}".format(i)) for i in range(clk + 1)]
    geode_robots_tobuy = [Int("buy_geode_r_{}".format(i)) for i in range(clk + 1)]

    # constraints - initially no resources, will populate for all time
    constraints = list()
    constraints.append(ore[0] == 0)
    constraints.append(clay[0] == 0)
    constraints.append(obsidian[0] == 0)
    constraints.append(geode[0] == 0)

    # starts with one ore robot, nothing to buy, and no resources
    constraints.append(ore_robots[0] == 1)
    constraints.append(clay_robots[0] == 0)
    constraints.append(obsidian_robots[0] == 0)
    constraints.append(geode_robots[0] == 0)

    constraints.append(ore_robots_tobuy[0] == 0)
    constraints.append(clay_robots_tobuy[0] == 0)
    constraints.append(obsidian_robots_tobuy[0] == 0)
    constraints.append(geode_robots_tobuy[0] == 0)

    constraints.append(ore[0] == 0)
    constraints.append(clay[0] == 0)
    constraints.append(obsidian[0] == 0)
    constraints.append(geode[0] == 0)

    # at each clock, resource = previous + robots available - cost of new purchase for ore, clay, obs, geode
    for i in range(1, clk + 1):
        constraints.append(ore[i] == ore[i - 1] + ore_robots[i - 1]
                           - (ore_robots_tobuy[i - 1]) * blueprint[0][0]
                           - (clay_robots_tobuy[i - 1]) * blueprint[1][0]
                           - (obsidian_robots_tobuy[i - 1]) * blueprint[2][0]
                           - (geode_robots_tobuy[i - 1]) * blueprint[3][0])
        constraints.append(clay[i] == clay[i - 1] + clay_robots[i - 1]
                           - (ore_robots_tobuy[i - 1]) * blueprint[0][1]
                           - (clay_robots_tobuy[i - 1]) * blueprint[1][1]
                           - (obsidian_robots_tobuy[i - 1]) * blueprint[2][1]
                           - (geode_robots_tobuy[i - 1]) * blueprint[3][1])
        constraints.append(obsidian[i] == obsidian[i - 1] + obsidian_robots[i - 1]
                           - (ore_robots_tobuy[i - 1]) * blueprint[0][2]
                           - (clay_robots_tobuy[i - 1]) * blueprint[1][2]
                           - (obsidian_robots_tobuy[i - 1]) * blueprint[2][2]
                           - (geode_robots_tobuy[i - 1]) * blueprint[3][2])
        constraints.append(geode[i] == geode[i - 1] + geode_robots[i - 1])

    # check if affordable
    for i in range(1, clk + 1):
        constraints.append(ore_robots_tobuy[i] * blueprint[0][0] <= ore[i])
        constraints.append(clay_robots_tobuy[i] * blueprint[1][0] <= ore[i])
        constraints.append(obsidian_robots_tobuy[i] * blueprint[2][0] <= ore[i])
        constraints.append(geode_robots_tobuy[i] * blueprint[3][0] <= ore[i])

        constraints.append(ore_robots_tobuy[i] * blueprint[0][1] <= clay[i])
        constraints.append(clay_robots_tobuy[i] * blueprint[1][1] <= clay[i])
        constraints.append(obsidian_robots_tobuy[i] * blueprint[2][1] <= clay[i])
        constraints.append(geode_robots_tobuy[i] * blueprint[3][1] <= clay[i])

        constraints.append(ore_robots_tobuy[i] * blueprint[0][2] <= obsidian[i])
        constraints.append(clay_robots_tobuy[i] * blueprint[1][2] <= obsidian[i])
        constraints.append(obsidian_robots_tobuy[i] * blueprint[2][2] <= obsidian[i])
        constraints.append(geode_robots_tobuy[i] * blueprint[3][2] <= obsidian[i])

    # build the new robot if affordable
    for i in range(1, clk + 1):
        constraints.append(ore_robots[i] == ore_robots[i - 1] + ore_robots_tobuy[i - 1])
        constraints.append(clay_robots[i] == clay_robots[i - 1] + clay_robots_tobuy[i - 1])
        constraints.append(obsidian_robots[i] == obsidian_robots[i - 1] + obsidian_robots_tobuy[i - 1])
        constraints.append(geode_robots[i] == geode_robots[i - 1] + geode_robots_tobuy[i - 1])

    # constrain robots to buy as one per turn
    for i in range(1, clk + 1):
        constraints.append(ore_robots_tobuy[i] <= 1)
        constraints.append(clay_robots_tobuy[i] <= 1)
        constraints.append(obsidian_robots_tobuy[i] <= 1)
        constraints.append(geode_robots_tobuy[i] <= 1)

        constraints.append(ore_robots_tobuy[i] >= 0)
        constraints.append(clay_robots_tobuy[i] >= 0)
        constraints.append(obsidian_robots_tobuy[i] >= 0)
        constraints.append(geode_robots_tobuy[i] >= 0)

        # buy max of one robot per turn
        constraints.append(
            ore_robots_tobuy[i] + clay_robots_tobuy[i] + obsidian_robots_tobuy[i] + geode_robots_tobuy[i] <= 1)

    # Objective is to maximize the amount of geode[t] at time t=100
    objective = geode[clk]
    solver = Optimize()
    solver.add(constraints)
    solver.maximize(objective)
    if solver.check() == sat:
        model = solver.model()
        return model[geode[clk]].as_long()


resources = [[[int(bp[6]), 0, 0], [int(bp[12]), 0, 0],
              [int(bp[18]), int(bp[21]), 0],
              [int(bp[27]), 0, int(bp[30])]]
             for bp in blueprints]

if stage == 'a':
    result = sum([solve(24, resources[i]) * (i + 1) for i in range(len(resources))])
else:
    result = solve(32, resources[0]) * solve(32, resources[1]) * solve(32, resources[2])

print(f"Time: {time.time() - start}")
print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
