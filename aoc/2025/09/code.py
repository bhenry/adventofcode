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

part1 = 0
coords = [nums(line) for line in lines]
areas = set()
greens = set()
for x,y in coords:
    for a,b in coords:
        if (x,y) == (a,b):
            continue
        areas.add((abs(x - a)+1) * (abs(y - b) +1))
        if x == a:
            for i in range(1,abs(y - b)):
                greens.add((x,y+i if y < b else y - i))
        if y == b:
            for i in range(1,abs(x - a)):
                greens.add((x+i if x < a else x - i,y))
part1 = max(areas)
print(part1)
part2 = 0

max_x = max([x for x,y in coords])
max_y = max([y for x,y in coords])
min_x = min([x for x,y in coords])
min_y = min([y for x,y in coords])

gs = greens.copy()
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        # if x,y between greens or coords then add to greens
        valid = True
        if x in [a for a,_ in gs]:

        for a,b in gs:



for (x,y) in greens.copy():
    for (a,b) in greens.copy():
        if x == a:
            for i in range(1,abs(y - b)):
                greens.add((x,y+i if y < b else y - i))
        if y == b:
            for i in range(1,abs(x - a)):
                greens.add((x+i if x < a else x - i,y))
areas = set()
greens = list(greens)
# print("coords:", coords)
# print("greens:", greens)
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
