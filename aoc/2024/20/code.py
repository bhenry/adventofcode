import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""
# lines = sample.strip().split("\n")
g = [list(l) for l in lines]

walls = set()
for y in range(len(g)):
    for x in range(len(g[y])):
        if g[y][x] == "S":
            start = (x, y)
        if g[y][x] == "E":
            end = (x, y)
        if g[y][x] == "#":
            walls.add((x, y))

paths = {}

def get_next(p,f):
    x,y = p
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) in walls: continue
        if (nx, ny) == f: continue
        return (nx, ny)

startdir = (1, 0) if not sample.strip() else (0, -1)

f = end
p = get_next((end[0]-1,end[1]),f)
c = 1
while True:
    c += 1
    if p == start: break
    newp = get_next(p,f)
    f, p = p, newp

target = c - 100

print(target) # 9352
print(c) # 9452

def calc_shortest_path(start, end):
    paths = {start: 0}
    q = [start]
    while q:
        x, y = q.pop(0)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in walls: continue
            if (nx, ny) in paths: continue
            paths[(nx, ny)] = paths[(x, y)] + 1
            q.append((nx, ny))
    return paths[end]

part1 = 0

for w in walls:
    x, y = w
    g[y][x] = "."

    g[y][x] = "#"

part2 = 0
