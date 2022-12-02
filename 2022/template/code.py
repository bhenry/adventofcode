import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()
print(input)
input_lines = input.splitlines()

sample_input = """
""".splitlines()

sample_answer1 = None
sample_answer2 = None

def process(input):
    pass

def p1(input):
    data = process(input)
    pass


def p2(input):
    data = process(input)
    pass

if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2", p2(input))
