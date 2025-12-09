import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

def print_(*args, **kwargs):
    print("\n")
    print(*args, **kwargs)

lines = raw.split("\n")
shortest_n = 1000

sample = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""
lines = sample.strip().split("\n")
shortest_n = 10

part1 = 0
distances = {}
for line in lines:
    x,y,z = nums(line)
    distances[(x,y,z)] = (None, None)
    for l in lines:
        a,b,c = nums(l)
        if x == a and y == b and z == c:
            continue
        if (a,b,c) in distances and distances[(a,b,c)][0] == (x,y,z):
            continue
        dist = (x - a)**2 + (y - b)**2 + (z - c)**2
        if distances[(x,y,z)][1] is None or dist < distances[(x,y,z)][1]:
            distances[(x,y,z)] = (a,b,c), dist

connections = []
closests = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1][1])[:shortest_n]}
print_(len(closests))

for d in closests:
    cxs = [c for c in connections if d in c or closests[d][0] in c]
    if len(cxs) > 1:
        connections.append(cxs[0] | cxs[1])
        connections.remove(cxs[0])
        connections.remove(cxs[1])
    elif len(cxs) == 1:
        connections.append(cxs[0] | {d, closests[d][0]})
        connections.remove(cxs[0])
    else:
        connections.append({d, closests[d][0]})

cs = sorted(connections, key=lambda x: len(x), reverse=True)[:3]
print(cs)
part1 = len(cs[0]) * len(cs[1]) * len(cs[2])
print_(part1)

part2 = 0


"""
21600 is too low
"""
