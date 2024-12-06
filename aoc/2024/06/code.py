import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input, Grid
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

lines = puzzleinput.lines()

sample = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
lines = sample.strip().split("\n")
sample_ans = 41

part1 = 0

grid = Grid(len(lines[0]), len(lines))
guard = None
heading = ""
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char in ["^", "v", "<", ">"]:
            guard = (x, y)
            heading = char
        grid.set(x, y, char)

headings = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0),
}

turns = {
    "^": ">",
    "<": "^",
    "v": "<",
    ">": "v",
}

while guard[0] >= 0 and guard[0] < grid.w and guard[1] >= 0 and guard[1] < grid.h:
    move = (guard[0] + headings[heading][0], guard[1] + headings[heading][1])
    if grid.get(*move) == "#":
        heading = turns[heading]
        move = (guard[0] + headings[heading][0], guard[1] + headings[heading][1])
    guard = move
    if grid.get(*guard) != "X":
        part1 += 1
    grid.set(*guard, "X")

print(part1 - 1)


part2 = 0
sample_ans2 = 6

grid2 = Grid(len(lines[0]), len(lines))

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        grid2.set(x, y, char)
