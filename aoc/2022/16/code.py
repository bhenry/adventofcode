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

"""
minute 0
AA

minute 1
AAAA (open AA)
AAII (move to II)
AADD (move to DD)
AABB (move to BB)

minute 2
AAAADD (move to DD)
AAAABB (move to BB)
AAAAII (move to II)
AAIIJJ (move to JJ)
--AAIIAA (move to AA)-- # only backtrack if there's nowhere new to go

minute 3 explodes to ~100 paths
"""
STORE = dict() # (pos, open_valves, time_remaining): flowscore
VALVES = {}
def calc(opens, t):
    flow = 0
    for v in opens:
        flow += VALVES[v].flow_rate*t
    return flow


def recur(v, t, opens):
    if (v, t, tuple(opens)) in STORE:
        return STORE[(v, t, tuple(opens))]
    # given a valve and time remaining, calculate all the moves left
    valve = VALVES[v]
    if t <= 1: # no moves left, but one more minute of flow
        ans = calc(opens, t)
        STORE[(v, t, tuple(opens))] = ans
        return ans
    moves = [(tunnel, t-1, opens) for tunnel in valve.tunnels]
    if v not in opens and valve.flow_rate > 0:
        # we can open this valve
        # total_flow_on_path += valve.flow_rate*(t-1)
        moves.append((v, t-1, opens | {v}))
    ans = max([calc(os, tr) for _,tr,os in moves])
    STORE[(v, t, tuple(opens))] = ans
    return ans

def key(v, t, opens):
    return (v, t, "".join(sorted(opens)))

# def compute(v, t, opens):
#     # given a valve and time remaining, calculate all the moves left
#     if key(v, t, opens) in STORE:
#         return STORE[key(v, t, opens)]
#     maximum = 0
#     valve = VALVES[v]
#     if t <= 1: # no moves left, but one more minute of flow
#         ans = calc(opens, t)
#         STORE[key(v, t, opens)] = ans
#         return ans
#     moves = [(tunnel, t-1, opens) for tunnel in valve.tunnels]
#     if v not in opens and valve.flow_rate > 0:
#         # we can open this valve
#         # total_flow_on_path += valve.flow_rate*(t-1)
#         moves.append((v, t-1, opens & {v}))
#     ans = max([calc(os, tr) for _,tr,os in moves])
#     STORE[key(v, t, opens)] = ans
#     return ans

def compute(v, time, opened):
    if key(v, time, opened) in STORE:
        return STORE[key(v, time, opened)]
    if time <= 0:
        return 0
    highest = 0
    valve = VALVES[v]
    if v not in opened:
        flow = valve.flow_rate * (time - 1)
        for tunnel in valve.tunnels:
            if flow:
                highest = max(highest, flow + compute(tunnel, time - 2, opened | set([v])))
            highest = max(highest, compute(tunnel, time-1, opened))
    STORE[key(v, time, opened)] = highest
    return highest

def process(input):
    for i in input.strip().splitlines():
        VALVES[i.split(" ")[1]] = Valve(i)
    return compute('AA', 30, set())

# print(process(sample_input))

def p1(input):
    data = process(input)
    return data

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
