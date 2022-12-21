import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """1
2
-3
3
-2
0
4
"""

sample_answer1 = 3
sample_answer2 = None

def process(input):
    return [int(i.strip()) for i in input.splitlines()]

# print(process(sample_input))

class item():
    def __init__(self, i, v, l):
        self.index = i
        self.value = v
        self.left = None
        self.right = None

    def __repr__(self):
        return f"item({self.value}),loc({self.index})"

def p1(input):
    data = process(input)
    d = []
    for i, v in enumerate(data):
        d[i] = item(i, v, data)
    zeroth = data.index(0)

    # return cd[(zeroth+1000)%len(cd)] + cd[(zeroth+2000)%len(cd)] + cd[(zeroth+3000)%len(cd)]

def p2(input):
    data = process(input)
    return data

if sample_answer1:
    sample_result = p1(sample_input)
    print("sample1", sample_result)
    if sample_result == sample_answer1:
        print("sample1 test pass")
        print("\nproblem1", p1(input), "\n\n")

if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2", sample_result)
    if sample_result == sample_answer2:
        print("sample2 test pass")
        print("\nproblem2", p2(input), "\n\n")


print("\ndone")
