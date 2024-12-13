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
# sample="""AAAAAA
# AAABBA
# AAABBA
# ABBAAA
# ABBAAA
# AAAAAA"""
# sample="""EEEEE
# EXXXX
# EEEEE
# EXXXX
# EEEEE"""
# sample="""AAAA
# BBCD
# BBCC
# EEEC"""
# sample="""
# CCJJRJJ
# CJJYJJJ
# CCNJJJJ"""
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
    edges = 0
    for x,y in region:
        value = g[y][x]
        edges += len(set(neighbors(x,y)) - region)
    part1 += edges*len(region)

print(part1)

part2 = 0

for region in regions:
    x,y = next(iter(region))
    value = g[y][x]
    area = len(region)
    outers = {}
    inners = {}
    for x,y in region:
        for nx,ny in neighbors(x,y):
            if (nx,ny) not in region:
                if (x,y) in outers:
                    outers[(x,y)].append((nx,ny))
                else:
                    outers[(x,y)] = [(nx,ny)]
                if (nx,ny) in inners:
                    inners[(nx,ny)].append((x,y))
                else:
                    inners[(nx,ny)] = [(x,y)]
    print(region)
    corners = set()
    for outer in outers:
        if len(outers[outer]) == 4:
            cs = [(outer[0]+a, outer[1]+b) for a,b in [(0,0.5),(0.5,0),(-0.5,0),(0,-0.5)]]
            corners.update(cs)
            continue
        if len(outers[outer]) == 3:
            connecting_side = set(neighbors(*outer)) - set(outers[outer])
            x1,y1 = next(iter(connecting_side))
            x0,y0 = outer
            dx,dy = x1-x0, y1-y0
            corners.add((x0-dx/2, y0-dy/2))
            corners.add((x0+dx/2, y0+dy/2))
            continue
        if len(outers[outer]) == 2:
            x0,y0 = outers[outer][0]
            x1,y1 = outers[outer][1]
            if abs(x0-x1) == 1 and abs(y0-y1) == 1:
                cs = ((x0+x1)/2, (y0+y1)/2)
                if cs not in corners:
                    corners.add(cs)
                else:
                    print("duped", value, outer, cs)
                    corners.remove(cs)
    corners = len(corners)
    for inner in inners:
        if len(inners[inner]) == 4:
            corners += 4
            continue
        if len(inners[inner]) == 3:
            corners += 2
            continue
        if len(inners[inner]) == 2:
            x0,y0 = inners[inner][0]
            x1,y1 = inners[inner][1]
            if abs(x0-x1) == 1 and abs(y0-y1) == 1:
                corners += 1
    print(region, "===\n\n\n", area, corners, area*corners)
    part2 += area * corners
print(part2)
