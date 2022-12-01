import itertools

with open('2022/01/input.txt') as f: input = f.readlines()

input = [int(x.strip() or -1) for x in input]

elves = [list(y) for x, y in itertools.groupby(input, lambda z: z == -1) if not x]
elf_totals = [sum(e) for e in elves]

print(max(elf_totals))

elf_totals.sort()
print(sum(elf_totals[-3:]))
