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
sample_answer2 = 230

def process(input):
    return [i.strip() for i in input.splitlines()]

def binary_string_to_decimal(binary_string):
    return int(binary_string, 2)

def ge(data):
    first = data.pop()
    g = []
    for i in first:
        g.append(1 if i == "1" else -1)

    for row in data:
        for i, c in enumerate(row):
            g[i] += 1 if c == "1" else -1
    gamma = [1 if i > 0 else 0 for i in g]
    epsilon = [1 if i < 0 else 0 for i in g]
    return (gamma, epsilon)

def p1(input):
    data = process(input)
    gamma, epsilon = ge(data)
    gamma = binary_string_to_decimal("".join(str(i) for i in gamma))
    epsilon = binary_string_to_decimal("".join(str(i) for i in epsilon))
    return gamma * epsilon

def getnext(data, z):
    gamma, epsilon = ge(data)
    g = [i for i in data if i[:z] == gamma[:z]]
    e = [i for i in data if i[:z] == epsilon[:z]]
    return (g, e)

def p2(input):
    data = process(input)
    return

if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    # print("Problem2", p2(input))
