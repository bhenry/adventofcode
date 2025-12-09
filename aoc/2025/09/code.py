from datetime import datetime
import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
# lines = sample.strip().split("\n")
starttime = datetime.now()
part1 = 0
coords = [nums(line) for line in lines]
areas = set()
for x,y in coords:
    for a,b in coords:
        if (x,y) == (a,b):
            continue
        areas.add((abs(x - a)+1) * (abs(y - b) +1))
part1 = max(areas)
print(part1)
endtime = datetime.now()
print("Time:", endtime - starttime)
part2 = 0

max_x = max([x for x,y in coords])
max_y = max([y for x,y in coords])
min_x = min([x for x,y in coords])
min_y = min([y for x,y in coords])

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        # if x,y between greens or coords then add to greens
        if (x,y) in coords:
            # greens.add((x,y))
            continue
        if (x,y) in greens:
            continue
        for g in gs:
            # if x,y is between any two greens in same row or column
            if x == g[0]:
                if (x, min(y, g[1]) + 1) in gs and (x, max(y, g[1]) - 1) in gs:
                    greens.add((x,y))
                    break
            if y == g[1]:
                if (min(x, g[0]) + 1, y) in gs and (max(x, g[0]) - 1, y) in gs:
                    greens.add((x,y))
                    break

# for (x,y) in greens.copy():
#     for (a,b) in greens.copy():
#         if x == a:
#             for i in range(1,abs(y - b)):
#                 greens.add((x,y+i if y < b else y - i))
#         if y == b:
#             for i in range(1,abs(x - a)):
#                 greens.add((x+i if x < a else x - i,y))
areas = set()
greens = list(greens)
print("coords:", coords)
print("greens:", greens)
for x,y in coords:
    for a,b in coords:
        valid = True
        if (x,y) == (a,b):
            continue
        for i in range(1,abs(y - b)):
            if (x,y+i if y < b else y - i) not in greens + coords:
                # if (x,y) == (9,5) and (a,b) == (2,3):
                #     print("i",x,y,a,b,i)
                valid = False
                break
        if not valid:
            continue
        for j in range(1,abs(x - a)):
            if (x+j if x < a else x - j,y) not in greens + coords:
                # if (x,y) == (9,5) and (a,b) == (2,3):
                #     print("j",x,y,a,b,j)
                valid = False
                break
        if valid:
            # print((x,y), (a,b))
            areas.add((abs(x - a)+1) * (abs(y - b)+1))

part2 = max(areas)
print(part2)
