import itertools
import os
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141""":605
}
sample2s = {

}

def process(pz):
    return pz.lines()
pzz = process(puzzleinput)

def problem1(pz):
    shortest = None
    trips = {}
    for line in pz:
        cities, distance = line.split(" = ")
        cities = cities.split(" to ")
        distance = int(distance)
        trips[cities[0]] = trips.get(cities[0], {})
        trips[cities[0]][cities[1]] = distance
        trips[cities[1]] = trips.get(cities[1], {})
        trips[cities[1]][cities[0]] = distance
    cache = {}
    trip = []
    td = 0
    start = list(trips.keys())[0]
    while set(trip) != set(trips.keys()):
        nxts = [t for t in trips[start].keys() if t not in trip]
        nxt = min(nxts, key=trips[start].get)
        td += trips[start][nxt]
        trip.append(nxt)
        start = nxt

    print(td)


    return td

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
