import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """
"""
# lines = sample.strip().split("\n")

part1 = 0



part2 = 0
