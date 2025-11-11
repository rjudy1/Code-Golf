# Advent of Code 2017 Day 20
# Author:   Rachael Judy
# Purpose:

import aocd
cookie = "53616c7465645f5f7df37d5a46729ceb401f8df250b10bd89afd30d3af863f3a75562dee1baf1789cdee18196cb7eec992ca4d14fd8bc1e488cf55a2d20cb9b9"

import parseMod

ready = True
day = 20
stage = 'a'
year = 2017

# parseMod.createDataFile(year=year, day=day)
# data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")
data = aocd.get_data(cookie, day, year)



if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
