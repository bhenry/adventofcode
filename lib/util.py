class Grid():
    def __init__(self, w=None, h=None, default=None):
        self.w = w
        self.h = h
        self.default = default
        self.grid = {}
        if w and h:
            for x in range(w):
                for y in range(h):
                    self.grid[(x,y)] = default

    def get(self, x, y):
        return self.grid.get((x,y), self.default)

    def set(self, x, y, val):
        self.grid[(x,y)] = val


class Input():
    def __init__(self, filename):
        if not filename.endswith('.txt'):
            self.filename = None
            self.input = filename
        else:
            self.filename = filename
            with open(filename) as f: self.input = f.read().strip()

    def grid(self, default=None):
        grid = Grid()
        for y, line in enumerate(self.input.splitlines()):
            for x, char in enumerate(line):
                grid.set(x, y, char)
        return grid

    def lines(self):
        return self.input.splitlines()

    def ints(self):
        return [int(i) for i in self.input.splitlines()]

    def ints_by_line(self):
        return [[int(i) for i in re.findall(r'-?\d+', line)] for line in self.input.splitlines()]
