import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """1
10
100
2024
"""
lines = sample.strip().split("\n")

part1 = 0

"""
1: 8685429
10: 4700978
100: 15273692
2024: 8667524
Adding up the 2000th new secret number for each buyer produces 37327623.
"""

def mix(a, b):
    return a ^ b

def prune(x):
    return x % 16777216


part2 = 0
