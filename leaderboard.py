import json
from datetime import datetime
import requests
import sys


year = 2024
board = 1027137
cookie_string = "53616c7465645f5f1974654587f84dac73952178aa2cd98dbda4716900978a2ba52114079f31bb1aed7e9fb4d867e4f39b6d15a52b618d620ace9157c6d2ced5"


def print_member(member):
    if member["name"] is None:
        print(f'Anonymous User #{member["id"]}', member["local_score"])
    else:
        print(member["name"], member["local_score"])

    days = []
    for day in member["completion_day_level"]:
        days.append((day, member["completion_day_level"][day]))

    days.sort(key=lambda d: int(d[0]))

    for day in days:
        print("{:02d}".format(int(day[0])) + " ", end='')
        try:
            print(datetime.utcfromtimestamp(
                int(day[1]["1"]["get_star_ts"]) - 18000).strftime('%b %d %H:%M:%S'), " ", end='')
            print(datetime.utcfromtimestamp(
                int(day[1]["2"]["get_star_ts"]) - 18000).strftime('%b %d %H:%M:%S'), " ")
        except:
            print("")
    print("")


if len(sys.argv) > 1:
    for i in range(1, len(sys.argv), 2):
        if sys.argv[i] == '--cookie':
            cookie_string = sys.argv[i + 1]
        elif sys.argv[i] == '--year' or sys.argv[i] == '-y':
            year = sys.argv[i + 1]
            print(year)
        elif sys.argv[i] == '--board' or sys.argv[i] == '-b':
            board = sys.argv[i + 1]
        else:
            print("Usage: python leaderboard.py [args]\n"
                  "-y, --year \t 2020, 2021, 2022, etc.\n"
                  "-b, --board\t board number when accessed, ie 1501977\n"
                  "--cookie   \t your session cookie; see screenshot "
                  "exampleCookieRetrieval.png for help with retrieval \n")
            quit(0)

cookie = {'session': f"{cookie_string}"}
r = requests.get(
    f'https://adventofcode.com/{year}/leaderboard/private/view/{board}.json', cookies=cookie)
data = r.content
response = json.loads(data)

members = []

for user in response["members"]:
    member = response["members"][user]
    members.append(member)

members.sort(key=lambda m: m["local_score"], reverse=True)
print("")
for member in members:
    print_member(member)

# input()
