import os
import sys
import re

APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

lines = puzzleinput.lines()

part1 = 0
for line in lines:
    ops = re.findall(r"mul\((.*?)\)", line)
    print(ops)


part2 = 0
