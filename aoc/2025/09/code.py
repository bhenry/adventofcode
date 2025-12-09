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
# lines = sample.strip()  .split("\n")

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

part2 = 0
border = set()
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                border.add((x1, y))
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                border.add((x, y1))
border = list(border)
greens = set()
for i in range(len(border)):
    for j in range(i+1, len(border)):
        x1, y1 = border[i]
        x2, y2 = border[j]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                greens.add((x1, y))
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                greens.add((x, y1))

for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        fail = False
        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                if (x, y) not in greens:
                    fail = True
                    continue
        if not fail:
            area = (abs(x1 - x2)+1) * (abs(y1 - y2) +1)
            if area > part2:
                part2 = area
print(part2)
