import itertools

with open('2022/01/input.txt') as f: input = f.readlines()

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
""".splitlines()

sample_answer1 = 24000

def p1(input):
    input = [int(x.strip() or -1) for x in input]
    elves = [list(y) for x, y in itertools.groupby(input, lambda z: z == -1) if not x]
    elf_totals = [sum(e) for e in elves]
    return max(elf_totals)

sample_answer2 = 45000

def p2(input):
    input = [int(x.strip() or -1) for x in input]
    elves = [list(y) for x, y in itertools.groupby(input, lambda z: z == -1) if not x]
    elf_totals = [sum(e) for e in elves]
    elf_totals.sort()
    return sum(elf_totals[-3:])

print("sample test", p1(sample_input) == sample_answer1)
print("Problem1", p1(input))
print("Problem2", p2(input))
