import os
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#""":94
}
sample2s = {

}

def process(pz):
    return pz.lines()

def problem1(pz):
    lines = process(pz)
    g = [[x for x in y] for y in lines]
    s = (1,0)
    paths = [[s]]
    while True:
        newpaths = []
        for path in paths:
            l = path[-1]
            ns = [(l[0], l[1]-1), (l[0]+1, l[1]), (l[0], l[1]+1), (l[0]-1, l[1])]
            for n in ns:
                if n[0] < 0 or n[1] < 0 or n[0] >= len(g[0]) or n[1] >= len(g):
                    continue
                if g[n[1]][n[0]] == "#":
                    continue
                if n in path:
                    continue
                if g[n[1]][n[0]] == ">":
                    if (n[0]+1, n[1]) != l:
                        newpaths.append(path + [n, (n[0]+1, n[1])])
                    continue
                if g[n[1]][n[0]] == "v":
                    if (n[0], n[1]+1) != l:
                        newpaths.append(path + [n, (n[0], n[1]+1)])
                    continue
                newpaths.append(path + [n])
        if not newpaths:
            break
        paths = newpaths
    print("\n\n".join([str(p) for p in paths]))
    return max([len(x) for x in paths]) - 1


def problem2(pz):
    lines = process(pz)

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

if answer1 := problem1(puzzleinput):
    print("\nproblem1", answer1, "\n\n")


print("\ndone")
