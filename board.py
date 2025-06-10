class Board:
    def __init__(self, size=5):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.ships = []
        self.hits = set()
        self.misses = set()

    def place_ship(self, ship):
        for (x, y) in ship.coordinates:
            if not (0 <= x < self.size and 0 <= y < self.size):
                return False
            for other in self.ships:
                if (x, y) in other.coordinates:
                    return False
        self.ships.append(ship)
        for (x, y) in ship.coordinates:
            self.grid[x][y] = 'S'
        return True

    def receive_attack(self, x, y):
        if not (0 <= x < self.size and 0 <= y < self.size):
            return "⚠️ Invalid coordinates! Please enter numbers between 1 and 5."
        if (x, y) in self.hits or (x, y) in self.misses:
            return "⚠️ Already attacked this position."
        for ship in self.ships:
            if (x, y) in ship.coordinates:
                ship.hit(x, y)
                self.hits.add((x, y))
                self.grid[x][y] = 'X'
                if ship.is_sunk():
                    print(f"💥 Ship of size {ship.size} has been destroyed!")
                    return "🎯 Hit and sunk!"
                else:
                    return "🎯 Hit!"
        self.misses.add((x, y))
        self.grid[x][y] = 'O'
        return "💨 Miss!"

    def all_sunk(self):
        return all(ship.is_sunk() for ship in self.ships)

    def display(self, reveal=False):
        print("  " + " ".join(str(i+1) for i in range(self.size)))
        for i in range(self.size):
            row = []
            for j in range(self.size):
                val = self.grid[i][j]
                row.append(val if reveal or val in ('X', 'O') else '.')
            print(f"{i+1} " + " ".join(row))
