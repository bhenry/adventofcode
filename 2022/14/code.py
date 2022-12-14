import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

sample_answer1 = 24
sample_answer2 = None

def process(input):
    return [i.strip() for i in input.splitlines()]

# print(process(sample_input))

def fallzones(loc):
    return [(loc[0]+dx, loc[1]+dy) for dx, dy in [[0, 1], [-1, 1], [1, 1]]]

def step(g):
    sand = g['sandloc']
    for loc in fallzones(sand):
        if g.get(loc) not in ['#', 'o']:
            g['sandloc'] = loc
            if loc[1] > g['deepest']:
                return
            # drop falling sand
            step(g)
            return
    g[g['sandloc']] = 'o'
    g['sandcount'] += 1
    return

def p1(input):
    g = {'sandcount': 0, 'deepest': 0}
    data = process(input)
    for line in data:
        segs = []
        for seg in [seg.strip() for seg in line.split("->")]:
            segs.append([int(i) for i in seg.split(",")])
        for i in range(len(segs)-1):
            seg = segs[i]
            next_seg = segs[i+1]
            if seg[0] == next_seg[0]:
                for y in range(min(seg[1], next_seg[1]), max(seg[1], next_seg[1])+1):
                    g[(seg[0], y)] = '#'
                    g['deepest'] = max(g['deepest'], y)
            else:
                for x in range(min(seg[0], next_seg[0]), max(seg[0], next_seg[0])+1):
                    g[(x, seg[1])] = '#'
                    g['deepest'] = max(g['deepest'], seg[1])
    sandstart = (500, 0)
    for _ in range(1000):
        g['sandloc'] = sandstart
        # drop new sand
        step(g)

    print(g['sandcount'])

    return g['sandcount']

def p2(input):
    data = process(input)
    return data

if sample_answer1:
    sample_result = p1(sample_input)
    print("sample1", sample_result)
    if sample_result == sample_answer1:
        print("sample1 test", True)
        print("\nproblem1", p1(input), "\n\n")

if sample_answer2:
    sample_result2 = p2(sample_input)
    print("sample2", sample_result2)
    if sample_result2 == sample_answer2:
        print("sample2 test", True)
        print("\nproblem2", p2(input), "\n\n")
