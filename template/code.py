import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """
"""

sample_answer1 = None
sample_answer2 = None

def process(input):
    return [i.strip() for i in input.splitlines()]

print(process(sample_input))

def p1(input):
    data = process(input)

def p2(input):
    data = process(input)

if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2", p2(input))
