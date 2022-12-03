import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

sample_answer1 = 157
sample_answer2 = 70

def process(input):
    lines = [i.strip() for i in input.splitlines()]
    return lines

print(process(sample_input))

priority = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

def p1(input):
    sax = process(input)
    s = 0
    for sac in sax:
        c1, c2 = sac[:len(sac)//2], sac[len(sac)//2:]
        repeat = set(c1).intersection(set(c2))
        s += priority[repeat.pop()]
    return s

def p2(input):
    sax = process(input)
    s = 0
    groups = [sax[i:i + 3] for i in range(0, len(sax), 3)]
    for group in groups:
        common = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        s += priority[common.pop()]
    return s

if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2", p2(input))
