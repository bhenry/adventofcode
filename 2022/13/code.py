from curses.ascii import isdigit
import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

sample_answer1 = 13
sample_answer2 = None

def process(input):
    return input.split("\n\n")

# print(process(sample_input))

def compare(a, b):
    if isinstance(a, list) and isinstance(b, list):
        if not a and not b:
            return True
        if not a and b:
            return True
        if not b and a:
            return False
        if compare(a[0], b[0]):
            return compare(a[1:], b[1:])
        else:
            return False
    if not isinstance(a, list) and isinstance(b, list):
        return compare([a], b)
    if isinstance(a, list) and not isinstance(b, list):
        return compare(a, [b])
    return a <= b

def p1(input):
    pairs = process(input)
    inorder = []
    for i, pair in enumerate(pairs):
        l,r = [eval(x) for x in pair.strip().split("\n")]
        if compare(l,r):
            inorder.append(i)
    return inorder

def p2(input):
    data = process(input)
    return data

if sample_answer1:
    sample_result = p1(sample_input)
    print("sample1 test", sample_result == sample_answer1)
    print("sample1", sample_result)
    if sample_result == sample_answer1:
        print("\nproblem1", p1(input), "\n\n")
if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2 test", sample_result == sample_answer2)
    print("sample2", p2(sample_input))
    if sample_result == sample_answer2:
        print("\nproblem2", p2(input), "\n\n")
