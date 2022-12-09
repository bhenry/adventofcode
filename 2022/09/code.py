import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

sample_answer1 = 13
sample_answer2 = None

def process(input):
    return [i.strip() for i in input.splitlines()]

def move(dir, dist):
    if dir == 'R':
        return (dist, 0)
    if dir == 'L':
        return (-dist, 0)
    if dir == 'U':
        return (0, dist)
    if dir == 'D':
        return (0, -dist)



def p1(input):
    data = process(input)
    h = (0,0)
    t = (0,0)
    tspots = set((0,0))
    for m in data:
        dir, dist = m.split()
        for d in range(int(dist)):
            mv = move(dir, 1)
            h = (h[0] + mv[0], h[1] + mv[1])
            if abs(t[0] - h[0]) > 1 or abs(t[1] - h[1]) > 1:
                if dir == 'R':
                    t = (h[0] - 1, h[1])
                if dir == 'L':
                    t = (h[0] + 1, h[1])
                if dir == 'U':
                    t = (h[0], h[1] - 1)
                if dir == 'D':
                    t = (h[0], h[1] + 1)
                tspots.add(t)
    return (len(tspots))


def p2(input):
    data = process(input)

if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2", p2(input))
