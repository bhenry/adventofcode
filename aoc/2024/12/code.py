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
lines = sample.strip().split("\n")

g = [list(x) for x in lines]
w = len(g[0])
h = len(g)

seen = set()
regions = []

def neighbors(x,y):
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

def oob(x,y):
    return x < 0 or x >= w or y < 0 or y >= h

def get_region(x,y):
    value = g[y][x]
    region = set()
    region.add((x,y))
    edges_to_check = set(neighbors(x,y))

    while edges_to_check:
        edge = edges_to_check.pop()
        if edge in seen: continue
        if oob(*edge): continue
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
        regions.append(get_region(x,y))

part1 = 0

for region in regions:
    perimeter = 0
    area = len(region)
    for x,y in region:
        for nx,ny in neighbors(x,y):
            if (nx,ny) not in region:
                perimeter += 1
    part1 += perimeter * area

print(part1)

part2 = 0

for region in regions:
    pass
