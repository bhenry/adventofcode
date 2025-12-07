import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""
# lines = sample.strip().split("\n")

part1 = 0
start = lines[0].find("S")
beams = [start]
for i in range(len(lines)):
    hit = beams
    for beam in beams:
        if lines[i][beam] == "^":
            part1 += 1
            hit = hit[:hit.index(beam)] + hit[hit.index(beam)+1:]
            if beam-1 not in hit:
                hit.append(beam-1)
            if beam+1 not in hit:
                hit.append(beam+1)
    beams = hit
print(part1)

part2 = 1
start = lines[0].find("S")
beams = [start]
paths = [beams]

while lines:
    line = lines[0]
    lines = lines[1:]
    new_paths = []
    for path in paths:
        if line[path[-1]] == "^":
            new_paths.append(path + [path[-1]-1])
            new_paths.append(path + [path[-1]+1])
        else:
            new_paths.append(path + [path[-1]])
    paths = new_paths

print(len(paths))
