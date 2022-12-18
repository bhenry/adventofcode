import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

sample_answer1 = 3068
sample_answer2 = None

rocks = """####

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
##""".strip().split("\n\n")


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
        # print("r\n",f"|{rock}|")
        self.rock = "\n" + "\n".join(f"  {l}" for l in rock.replace("#", "@").splitlines()) + "\n"*4
        # print("R\n",self.rock)

    def __repr__(self):
        return self.rock

class Cave():
    def __init__(self, wind):
        self.wind = wind
        self.cave = "\n-------"

    @property
    def height(self):
        return len(self.cave.splitlines())

    def __repr__(self):
        return self.cave

    def add_rock(self, rock):
        self.cave = rock + self.cave[1:]

    def shiftl(self):
        fr = self.falling_rock()[:-1]
        newrock = []
        for l in fr:
            if l.find("@") == 0:
                return False
            if l[l.find("@")-1] == "#":
                return False
            lpiece = l.find("@")
            rpiece = l.rfind("@")
            newl = l[:lpiece-1] + l[lpiece:rpiece+1] + " " + l[rpiece+1:]
            newrock.append(newl.rstrip())
        # print("leftold\n", self.cave)
        self.cave = self.cave.replace("\n".join(fr), "\n".join(newrock))
        # print("new\n", self.cave)
        return True

    def shiftr(self):
        fr = self.falling_rock()[:-1]
        newrock = []
        for l in fr:
            newl = ""
            for i in range(len(l)-1, 1, -1):
                if i == 6 and l[i] == "@":
                    return False
                if l[i] == "#" and l[i-1] == "@":
                    return False
            lpiece = l.find("@")
            rpiece = l.rfind("@")
            newl = l[:lpiece] + " " + l[lpiece:rpiece+1] + l[rpiece+1:]
            # print("l\n",l,"\nnewl\n",newl,"\n")
            newrock.append(newl)
        # print("fr\n","\n".join(fr), "\nnr\n", "\n".join(newrock), "\n")
        # print("===right===oldcave\n", self.cave, "\n=======")
        self.cave = self.cave.replace("\n".join(fr), "\n".join(newrock))
        # print("======newcave\n", self.cave, "\n=======")
        return True

    def falling_rock(self):
        found_rock = False
        moving_rows = []
        for l in self.cave.splitlines():
            if l.find("@") != -1:
                found_rock = True
                moving_rows.append(l)
            if found_rock and l.find("@") == -1:
                moving_rows.append(l)
                return moving_rows
        return []

    def drop(self):
        if len(self.cave.split("\n\n")) > 1:
            self.cave = self.cave.replace("\n\n", "\n", 1)
            return True
        newrocklines = []
        falling_rock = self.falling_rock() or []
        for l, l2 in zip(falling_rock, falling_rock[1:]):
            if l.find('@') != -1:
                for i in range(min(len(l), len(l2))):
                    if l[i] == "@" and l2[i] in ["#", "-"]:
                        return False
        for i in range(len(falling_rock)-1):
            old_above = falling_rock[i].ljust(7)
            old_line = falling_rock[i+1].ljust(7)
            newline = ""
            for t,b in zip(old_above, old_line):
                if t == "@":
                    newline += "@"
                else:
                    newline += " " if b == "@" else b
            newrocklines.append(newline.rstrip())
        # print("==dr====oldcave\n", self.cave, "\n=======")
        self.cave = self.cave.replace("\n".join(falling_rock), "\n".join(sorted(newrocklines)))
        # print("======newcave\n", self.cave, "\n=======")
        return True

    def settle(self):
        self.cave = self.cave.replace("@", "#")

    def fill(self):
        cycles = 0
        for r in range(2022):
            rock = Rock(rocks[r % len(rocks)]).rock
            self.add_rock(rock)
            while True:
                # print("======cave\n", self.cave, "\n=======")
                w = self.wind[cycles % len(self.wind)]
                cycles += 1
                self.shiftl() if w == "<" else self.shiftr()
                # print(f"={w}=====cave\n", self.cave, "\n=======")

                if not self.drop():
                    self.settle()
                    print(f"==settle====cave\n", self.cave, "\n=======")
                    break
                # print(f"==drop====cave\n", self.cave, "\n=======")



def process(input):
    return input.strip()

# print(process(sample_input))

def p1(input):
    wind = process(input)
    cave = Cave(wind)
    cave.fill()
    print(cave.cave)

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
