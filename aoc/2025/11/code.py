import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""
# lines = sample.strip().split("\n")

part1 = 0
paths = {}
for line in lines:
    stuff = line.split(" ")
    paths[stuff[0][:-1]] = stuff[1:]

cxs = paths["you"]
while True:
    new_cxs = []
    for cx in cxs:
        if cx == "out":
            part1 += 1
        else:
            new_cxs.extend(paths[cx])
    cxs = new_cxs
    if not cxs:
        break

print(part1)

sample2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty svr
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""
lines = sample2.strip().split("\n")
part2 = 0
paths = {}
for line in lines:
    stuff = line.split(" ")
    paths[stuff[0][:-1]] = stuff[1:]
cxs = [["svr"] + [p] for p in paths["svr"]]
while True:
    new_cxs = []
    for cx in cxs:
        if cx[-1] == "out":
            if "fft" in cx and "dac" in cx:
                part2 += 1
        else:
            new_cxs.extend([cx + [p] for p in paths[cx[-1]] if p not in cx])
    cxs = new_cxs
    if not cxs:
        break
print(part2)
