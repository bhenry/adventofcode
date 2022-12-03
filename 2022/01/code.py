import os
import itertools
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

sample_answer1 = 24000
sample_answer2 = 45000

def process(input):
    input = [int(x.strip() or -1) for x in input.splitlines()]
    elves = [list(y) for x, y in itertools.groupby(input, lambda z: z == -1) if not x]
    return [sum(e) for e in elves]

def p1(input):
    elf_totals = process(input)
    return max(elf_totals)

def p2(input):
    elf_totals = process(input)
    elf_totals.sort()
    return sum(elf_totals[-3:])

if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2", p2(input))
