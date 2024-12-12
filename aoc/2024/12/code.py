import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input, nums
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

lines = puzzleinput.lines()

sample = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
# lines = sample.strip().split("\n")

g = [list(x) for x in lines]
w = len(g[0])
h = len(g)

part1 = 0

seen = set()
regions = {}

def neighbors(x,y):
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

def get_region(x,y):
    value = g[y][x]
    region = set()
    region.add((x,y))
    edges_to_check = set(neighbors(x,y))

    while edges_to_check:
        edge = edges_to_check.pop()
        if edge in seen:
            continue
        if edge[0] < 0 or edge[0] >= w or edge[1] < 0 or edge[1] >= h:
            continue
        if g[edge[1]][edge[0]] == value:
            region.add(edge)
            seen.add(edge)
            edges_to_check.update(neighbors(*edge))
    return region

for y in range(h):
    for x in range(w):
        value = g[y][x]
        if (x,y) in seen:
            continue
        seen.add((x,y))
        regions[(x,y)] = get_region(x,y)

for region in regions.values():
    perimeter = 0
    area = len(region)
    for x,y in region:
        for nx,ny in neighbors(x,y):
            if (nx,ny) not in region:
                perimeter += 1
    part1 += perimeter * area

print(part1)

part2 = 0
