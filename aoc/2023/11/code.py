import os
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""": """....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#......."""
}
sample2s = {

}

def process(pz):
    return pz

def problem1(pz):
    new = []
    lines = pz.lines()
    for i in range(len(lines)):
        line = lines[i]
        new.append(line)
        if all([c == "." for c in line]):
            new.append(line)

    new2 = ["" for i in range(len(new))]
    for i in range(len(new)):
        line = new[i]
        for j in range(len(line)):
            new2[i] += line[j]
            if all([new[c][j] == "." for c in range(len(new))]):
                new2[i] += line[j]
    return "\n".join(new2)

def problem2(pz):
    grid = process(pz)

# debug
if sample2s:
    for sample in sample2s:
        sample_result = problem2(Input(sample))
        print("sample2", sample_result)
        if sample_result == sample2s[sample]:
            print("sample2 test pass")

if answer2 := problem2(puzzleinput):
    print("\nproblem2", answer2, "\n\n")

# debug
if samples:
    for sample in samples:
        sample_result = problem1(Input(sample))
        print("sample1", sample_result)
        if sample_result == samples[sample]:
            print("sample1 test pass")

# if answer1 := problem1(puzzleinput):
#     print("\nproblem1", answer1, "\n\n")


print("\ndone")
