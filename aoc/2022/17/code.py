import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

sample_answer1 = 3068
sample_answer2 = None

rocks = """
####

 #
###
 #

  #
  #
###

#
#
#
#

##
##
""".strip().split("\n\n")


"""
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|..####.|
+-------+
"""

class Rock():
    def __init__(self, rock):
        self.rock = "\n".join(f"  {l}" for l in rock.replace("#", "@").splitlines()) + "\n"*4

    def __repr__(self):
        return self.rock

    def shift(self, w):
        if w == ">":
            self.lines = "\n".join(f" {l}" for l in self.lines) if all(len(l) < 7 for l in self.lines) else self.lines
        elif w == "<":
            self.lines = "\n".join(l[1:] if l else l for l in self.lines) if all(l[0] == " " for l in self.lines if l) else self.lines


class Cave():
    def __init__(self, wind):
        self.wind = wind
        self.cave = "-------"

    @property
    def height(self):
        return len(self.cave.splitlines())

    def __repr__(self):
        return self.cave

    def add_rock(self, rock):
        self.cave = rock + self.cave

    def shiftl(self):
        rel = [line for line in self.cave.splitlines() if "@" in line]

        pixels = {i: c for i,c in enumerate(self.cave)}
        for i, c in pixels.items():
            if c == "@" and pixels[i-1] == "#":
                return
        self.cave = self.cave.replace(" @", "@ ")

    def shiftr(self):
        rel = [line for line in self.cave.splitlines() if "@" in line]
        for r in rel:
            idx = {i: c for i,c in enumerate(r)}
            if r.rfind("@") == len(r) - 1:
                return
            if idx[r.rfind("@") + 1] == "#":
                return
        self.cave = self.cave.replace("@ ", " @")

    def rock_bottom(self):
        self.cave.find("@")

    def drop(self):
        if len(self.cave.split("\n\n")) > 1:
            self.cave = self.cave.replace("\n\n", "\n", 1)
            return True
        for l, l2 in zip(self.cave.splitlines(), self.cave.splitlines()[1:]):
            if l.find('@'):
                for i in range(min(len(l), len(l2))):
                    if l[i] == "@" and l2[i] == "#":
                        return False

        rel = [line for line in self.cave.splitlines() if "@" in line]


    def settle(self):
        self.cave = self.cave.replace("@", "#")

    def fill(self):
        cycles = 0
        for r in range(10):
            rock = Rock(rocks[r % len(rocks)]).rock
            self.add_rock(rock)
            print(self.cave)
            while True:
                w = self.wind[cycles % len(self.wind)]
                # self.shift(w)
                if not self.drop():
                    self.settle()
                    break



def process(input):
    return input.strip()

# print(process(sample_input))

def p1(input):
    wind = process(input)
    cave = Cave(wind)
    print(cave.cave)
    cave.fill()

    return cave.height

def p2(input):
    data = process(input)
    return data

if sample_answer1:
    sample_result = p1(sample_input)
    print("sample1", sample_result)
    if sample_result == sample_answer1:
        print("sample1 test pass")
        print("\nproblem1", p1(input), "\n\n")

if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2", sample_result)
    if sample_result == sample_answer2:
        print("sample2 test pass")
        print("\nproblem2", p2(input), "\n\n")


print("\ndone")
