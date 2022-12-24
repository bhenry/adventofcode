import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""

sample_answer2 = 301

def process(input):
    return [i.strip() for i in input.splitlines()]

# print(process(sample_input))
MONKEYS = {}
class monkey():
    def __init__(self, inputt):
        self.id = inputt.split(":")[0]
        v = inputt.split(":")[1].strip()
        self.value = v


    def do(self):
        parts = self.value.split(" ")
        if len(parts) == 1:
            value = int(self.value)
        else:
            if self.id == "root":
                p1 = MONKEYS[parts[0]].do()
                p2 = MONKEYS[parts[2]].do()
            if self.id == "humn":
                pass
            if parts[1] == "+":
                value = p1[0] + p2[0]
            elif parts[1] == "-":
                value = p1[0] - p2[0]
            elif parts[1] == "*":
                value = p1[0] * p2[0]
            elif parts[1] == "/":
                value = p1[0] / p2[0]
        return value, parts


def p1(input):
    data = process(input)
    for i in data:
        MONKEYS[i.split(":")[0]] = monkey(i)
    return MONKEYS['root'].do()[0]

def p2(input):
    data = process(input)
    for i in data:
        MONKEYS[i.split(":")[0]] = monkey(i)
    return MONKEYS['root'].do()[0]

if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2", sample_result)
    if sample_result == sample_answer2:
        print("sample2 test pass")
        print("\nproblem2", p2(input), "\n\n")


print("\ndone")
