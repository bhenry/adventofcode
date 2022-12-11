import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """3,4,3,1,2
"""

sample_answer1 = 5934
sample_answer2 = 26984457539

def process(input):
    return [i.strip() for i in input.splitlines()]

def p1(input):
    data = process(input)[0]
    fishes = [int(i) for i in data.split(",")]

    for _ in range(80):
        fishes = [f - 1 for f in fishes]
        fishes = fishes + [6 for f in fishes if f < 0] + [8 for f in fishes if f < 0]
        fishes = [f for f in fishes if f >= 0]
    return len(fishes)

def p2(input):
    data = process(input)[0]
    # fishes = [int(i) for i in data.split(",")]
    # fishes = [0,1,2,3,4,5,6]
    fishes = [3,1,2]
    # a 0 has a baby on the first day
    # a 6 has a baby on the seventh day

    totes = 1
    births_by_fish = []
    for f in fishes:
        times_at_zero = 0
        for day in range(256):
            if (f - day) % 7 == 0:
                times_at_zero += 1
        births_by_fish.append(times_at_zero)
    print(births_by_fish)
    return totes

# if sample_answer1:
#     print("sample test", p1(sample_input) == sample_answer1)
#     print("Problem1", p1(sample_input))
#     print("Problem1", p1(input))
if sample_answer2:
    ans2 = p2(sample_input)
    print("sample test2", ans2 == sample_answer2)
    print("Problem2", ans2)
    # print("Problem2", p2(input))
