import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """987654321111111
811111111111119
234234234234278
818181911112111
"""
# lines = sample.strip().split("\n")

part1 = 0
for line in lines:
    digits = [int(d) for d in line]
    first_digit = max(digits[:-1])
    digloc = digits.index(first_digit)
    second_digit = max(digits[digloc+1:])
    print(first_digit, second_digit)
    part1 += 10*first_digit + second_digit
print(part1)

part2 = 0
for line in lines:
    digits = [int(d) for d in line]
    first_digit = max(digits[:-11])
    digloc = digits.index(first_digit)
    digits = digits[digloc+1:]
    second_digit = max(digits[:-10])
    digloc = digits.index(second_digit)
    digits = digits[digloc+1:]
    third_digit = max(digits[:-9])
    digloc = digits.index(third_digit)
    digits = digits[digloc+1:]
    fourth_digit = max(digits[:-8])
    digloc = digits.index(fourth_digit)
    digits = digits[digloc+1:]
    fifth_digit = max(digits[:-7])
    digloc = digits.index(fifth_digit)
    digits = digits[digloc+1:]
    sixth_digit = max(digits[:-6])
    digloc = digits.index(sixth_digit)
    digits = digits[digloc+1:]
    seventh_digit = max(digits[:-5])
    digloc = digits.index(seventh_digit)
    digits = digits[digloc+1:]
    eighth_digit = max(digits[:-4])
    digloc = digits.index(eighth_digit)
    digits = digits[digloc+1:]
    ninth_digit = max(digits[:-3])
    digloc = digits.index(ninth_digit)
    digits = digits[digloc+1:]
    tenth_digit = max(digits[:-2])
    digloc = digits.index(tenth_digit)
    digits = digits[digloc+1:]
    eleventh_digit = max(digits[:-1])
    digloc = digits.index(eleventh_digit)
    digits = digits[digloc+1:]
    twelfth_digit = max(digits)

    strnum = f"{first_digit}{second_digit}{third_digit}{fourth_digit}{fifth_digit}{sixth_digit}{seventh_digit}{eighth_digit}{ninth_digit}{tenth_digit}{eleventh_digit}{twelfth_digit}"
    print(strnum)
    part2 += int(strnum)

print(part2)
