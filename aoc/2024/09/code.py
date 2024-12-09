import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

line = puzzleinput.lines()[0]

sample = "2333133121414131402"
line = sample

part1 = 0

fs = []

fileorfree = 0
cursize = 0
freespace = 0

if len(line) % 2 == 0:
    fs = zip([int(x) for x in line[::2]], [int(x) for x in line[1::2]])
else:
    line += '0'
    fs = zip([int(x) for x in line[::2]], [int(x) for x in line[1::2]])

mapp = []
for i, f in enumerate(list(fs)):
    mapp.append(f'{i}' * f[0])
    mapp.append('.' * f[1] if f[1] > 0 else '')

print(mapp)
print("".join(mapp))


part2 = 0
