import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""

sample_answer1 = 1651
sample_answer2 = None

class Valve():
    def __init__(self, line):
        self.name = line.split(" ")[1]
        self.flow_rate = int(line.split("=")[1].split(";")[0])
        self.tunnels = [t.strip(',') for t in line.split(' ')[line.split(' ').index('to') + 2:]]
        self.open = False

    def open(self):
        self.open = True

    def __repr__(self):
        return f"Valve {self.name} rate={self.flow_rate}; tunnels {', '.join(self.tunnels)}\n"

    def moves(self, m, tally, opens):
        if self.name not in opens:
            ms = [(self.name, m, tally + self.flow_rate*(m-1), opens + [self.name])]
        else:
            ms = [] # don't waste time if already open
        for t in self.tunnels:
            ms.append((t, 0, tally, opens))
        return ms


def process(input):
    return [Valve(i.strip()) for i in input.strip().splitlines()]

def p1(input):
    data = process(input)
    valves = {v.name: v for v in data}
    highest = 0
    cur = 'AA'
    v = valves[cur]
    initial_moves = v.moves(30, 0, [])
    possible_moves_at_minute = {0: [initial_moves]} # first possible moves minute1
    for m in range(30):
        remainingm = 29 - m
        possible_moves_at_minute[m+1] = []
        for set_of_moves in possible_moves_at_minute[m]:
            for cur,_,tally,opens in set_of_moves:
                # print(m, len(set_of_moves), cur, tally, opens)
                v = valves[cur]
                possible_moves_at_minute[m+1].append((v.moves(remainingm, tally, opens)))
                if tally > highest:
                    highest = tally

    return highest

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
