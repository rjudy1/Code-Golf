
import json
from datetime import datetime
import requests


def printMember(member):
    if member["name"] == None:
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


cookie = {'session': "53616c7465645f5f5bb83a61626d763169fd6291066972ad0a8815efdc0495ad90319c5f17495f97c183f42e69644dd0800b82fab928656da9e4afb9b959a846"}
r = requests.get(
    'https://adventofcode.com/2021/leaderboard/private/view/1027137.json', cookies=cookie)
data = r.content
response = json.loads(data)

members = []

for user in response["members"]:
    member = response["members"][user]
    members.append(member)

members.sort(key=lambda m: m["local_score"], reverse=True)
print("")
for member in members:
    printMember(member)

input()
