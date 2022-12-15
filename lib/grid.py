class Grid():
    def __init__(self, w=None, h=None, default=None):
        self.w = w
        self.h = h
        self.default = default
        self.grid = []

    def get(self, x, y):
        return self.grid[y][x]
