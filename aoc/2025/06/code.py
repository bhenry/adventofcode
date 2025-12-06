import os
import re
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""
# lines = sample.strip().split("\n")

part1 = 0
problems = [nums(lines[0])]
for line in lines[1:]:
    if (line.split(" ")[0] in ["*", "+"]):
        break
    problems.append(nums(line))

def ops(line):
    return [x for x in re.findall(r'-?\S+', line)]

operations = ops(lines[-1])
print(problems, operations)

for i in range(len(problems[0])):
    if operations[i] == "*":
        problemtotal = 1
        for p in problems:
            problemtotal *= p[i]
        part1 += problemtotal
    elif operations[i] == "+":
        part1 += sum(p[i] for p in problems)

print(part1)
part2 = 0
