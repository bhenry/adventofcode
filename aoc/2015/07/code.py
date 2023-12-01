import os
import sys
APP_DIR = os.path.dirname(os.path.abspath(__file__).split("aoc")[0])
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i""": 65412,
}
sample2s = {

}

def process(pz):
    return pz.lines()

RECURSION = {}

def parse(vals, data):
    RECURSION[data] = RECURSION.get(data, 0) + 1
    RECURSION["parser"] = RECURSION.get("parser", "") + data + ", "
    if data.isnumeric():
        return int(data)
    elif v := vals.get(data.strip()):
        if v.isnumeric():
            return int(v)
        else:
            return parse(vals, v)
    elif " AND " in data:
        a, b = data.split(" AND ")
        return parse(vals, a) & parse(vals, b)
    elif " OR " in data:
        a, b = data.split(" OR ")
        return parse(vals, a) | parse(vals, b)
    elif " LSHIFT " in data:
        a, b = data.split(" LSHIFT ")
        return parse(vals, a) << parse(vals, b)
    elif " RSHIFT " in data:
        a, b = data.split(" RSHIFT ")
        return parse(vals, a) >> parse(vals, b)
    elif "NOT " in data:
        a = data.split("NOT ")[1]
        return 65535 - parse(vals, a)
    else:
        print("WTF", data)
        return None

def p1(pz):
    vals = {}
    for line in pz:
        data, target = line.split(" -> ")
        vals[target.strip()] = data.strip()

    for k in vals:
        if k != "a":
            print(k, parse(vals, vals[k]))


    return parse(vals, "a")

def p2(pz):

    return None

pzz = process(puzzleinput)

# if answer2 := p2(pzz):
#     print("\nproblem2", answer2, "\n\n")

#     # debug
#     if sample2s:
#         for sample in sample2s:
#             sample_result = p2(process(Input(sample)))
#             print("sample2", sample_result)
#             if sample_result == sample2s[sample]:
#                 print("sample2 test pass")

if answer1 := p1(pzz):
    print("\nproblem1", answer1, "\n\n")

# debug
if samples:
    for sample in samples:
        sample_result = p1(process(Input(sample)))
        print("sample1", sample_result)
        if sample_result == samples[sample]:
            print("sample1 test pass")



print("\ndone")
