import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

sample_answer1 = 198
sample_answer2 = None

def process(input):
    return [i.strip() for i in input.splitlines()]

def binary_string_to_decimal(binary_string):
    return int(binary_string, 2)

def p1(input):
    data = process(input)
    first = data.pop()
    g = []
    for i in first:
        g.append(1 if i == "1" else -1)

    for row in data:
        for i, c in enumerate(row):
            g[i] += 1 if c == "1" else -1
    gamma = [1 if i > 0 else 0 for i in g]
    epsilon = [1 if i < 0 else 0 for i in g]
    return binary_string_to_decimal("".join(str(i) for i in gamma)) * binary_string_to_decimal("".join(str(i) for i in epsilon))

def p2(input):
    data = process(input)

if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2", p2(input))
