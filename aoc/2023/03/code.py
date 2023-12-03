import os
import re
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""": 4361
}
sample2s = {

}

def process(pz):
    return pz
pzz = process(puzzleinput)

def checker(point):
    return point != "." and not point.isdigit()
'.......262....300...................507.....961..............668.....................189.906...........................624..................'
def problem1(pz):
    grid = pz.grid()
    collect = []
    for i, line in enumerate(pz.lines()):
        nums = re.findall(r'\d+', line)
        for num in nums:
            collected = False
            ix = line.index(num)
            length = len(num)
            check = range(max(0,ix-1), min(len(line),ix+length+1))
            for x in check:
                prevlinepoint = grid.point(x, max(i-1, 0))
                point = grid.point(x, i)
                nextlinepoint = grid.point(x, min(i+1, grid.h-1))
                if checker(prevlinepoint) or checker(point) or checker(nextlinepoint):
                    collect.append(int(num))
                    collected = True
            line = line.replace(num, "0"*length, 1)

    return sum(collect)

def problem2(pz):

    return None

# debug
if sample2s:
    for sample in sample2s:
        sample_result = problem2(process(Input(sample)))
        print("sample2", sample_result)
        if sample_result == sample2s[sample]:
            print("sample2 test pass")

if answer2 := problem2(pzz):
    print("\nproblem2", answer2, "\n\n")

# debug
if samples:
    for sample in samples:
        sample_result = problem1(process(Input(sample)))
        print("sample1", sample_result)
        if sample_result == samples[sample]:
            print("sample1 test pass")

if answer1 := problem1(pzz):
    print("\nproblem1", answer1, "\n\n")


print("\ndone")
