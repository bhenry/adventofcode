import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input, nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')
puzzleinput = Input(raw)

lines = puzzleinput.lines()
lines = raw.split("\n\n")

sample = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""
# lines = sample.strip().split("\n\n")

part1 = 0

towels = lines[0].strip().split(", ")
patterns = lines[1].strip().split("\n")

for p in patterns:
    tries = {p}
    while tries:
        possible = False
        tri = tries.pop()
        if tri == "":
            possible = True
            break
        for t in towels:
            if tri.startswith(t):
                newt = tri[len(t):]
                tries.add(newt)
                continue
    if possible:
        part1 += 1
        continue

print(part1)

part2 = 0

c = {}
def calc(p):
    if p in c: return c[p]
    if p == "": return 1
    ct = 0
    for t in towels:
        if p.startswith(t):
            newt = p[len(t):]
            ct += calc(newt)
    c[p] = ct
    return ct

for p in patterns:
    part2 += calc(p)
print(part2)
