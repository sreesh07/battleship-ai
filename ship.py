class Ship:
    def __init__(self, size):
        self.size = size
        self.coordinates = []
        self.hits = set()

    def place(self, start_x, start_y, horizontal=True):
        self.coordinates = []
        for i in range(self.size):
            x = start_x + (i if not horizontal else 0)
            y = start_y + (i if horizontal else 0)
            self.coordinates.append((x, y))

    def hit(self, x, y):
        if (x, y) in self.coordinates:
            self.hits.add((x, y))

    def is_sunk(self):
        return set(self.coordinates) == self.hits