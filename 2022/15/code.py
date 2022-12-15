import os
import re
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""

sample_answer1 = 26
sample_answer2 = 56000011

def process(input):
    return [i.strip() for i in input.strip().split("\n")]

# print(process(sample_input))

def print_grid(grid):
    for y in range(min([y for x,y in grid.keys()]) - 5, max([y for x,y in grid.keys()]) + 5):
        print(f"{y:03}", end=' ')
        for x in range(min([x for x,y in grid.keys()]) - 5, max([x for x,y in grid.keys()]) + 5):
            print(grid.get((x,y), '.'), end='')
        print()

    return grid

def blocked(x, y, sensors, beacons):
    if (x, y) in beacons:
        return False
    for sx, sy, d in sensors:
        if abs(sx - x) + abs(sy - y) <= d:
            return True
    return False

def p1(input, testrow):
    data = process(input)
    sensors = set()
    beacons = set()
    for line in data:
        sx, sy, bx, by = [int(i) for i in re.findall(r'-?\d+', line)]
        distance = abs(bx - sx) + abs(by - sy)
        sensors.add((sx, sy, distance))
        beacons.add((bx, by))

    # grid = {}
    # for x in range(min([x - d for x,_,d in sensors]), max([x + d for x,_,d in sensors]) +1):
    #     for y in range(min([y - d for _,y,d in sensors]), max([y + d for _,y,d in sensors]) +1):
    #         grid[(x,y)] = 'B' if (x,y) in beacons else 'S' if (x,y) in sensors else '#' if blocked(x, y, sensors, beacons) else '.'
    # print_grid(grid)

    ans = 0
    for x in range(min([x - d for x,_,d in sensors]), max([x + d for x,_,d in sensors])):
        ans += 1 if blocked(x, testrow, sensors, beacons) else 0
    return ans

def p2(input, maxsize):
    data = process(input)

    return data

if sample_answer1:
    sample_result = p1(sample_input, 10)
    print("sample1 test", sample_result == sample_answer1)
    print("sample1", sample_result)
    if sample_result == sample_answer1:
        print("\nproblem1", p1(input, 2000000), "\n\n")

if sample_answer2:
    sample_result = p2(sample_input, 20)
    print("sample2 test", sample_result == sample_answer2)
    print("sample2", sample_result)
    if sample_result == sample_answer2:
        print("\nproblem2", p2(input, 4000000), "\n\n")


print("\ndone")
