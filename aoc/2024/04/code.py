import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

lines = puzzleinput.lines()

part1 = 0

sample = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

def xmas(s):
    return s.count("XMAS") + s.count("SAMX")


cols = ["".join([line[i] for line in lines]) for i in range(len(lines[0]))]

def get_diags(lines):
    diags = []
    for i in range(len(lines)):
        diag = ""
        for j in range(len(lines)-i):
            diag += lines[j][j+i]
        diags.append(diag)


    return diags

def p (lines):
    for line in lines:
        print(line)
    print()
# p(lines)
# p([line[::-1] for line in cols])
# p([line[::-1] for line in lines[::-1]])
# p(cols[::-1])

diags = get_diags(lines)
diags += get_diags([line[::-1] for line in cols])
diags += get_diags([line[::-1] for line in lines[::-1]])[1:]
diags += get_diags(cols[::-1])[1:]

for line in lines:
    part1 += xmas(line)

for col in cols:
    part1 += xmas(col)

for diag in diags:
    part1 += xmas(diag)

print(part1)


part2 = 0

# lines = sample.strip().split("\n")
