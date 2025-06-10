import random
from ship import Ship
from board import Board
from ai_learning import AILearning

class HumanPlayer:
    def __init__(self):
        self.board = Board()
        self.setup()

    def setup(self):
        choice = input("Manual setup? (y/n): ").lower()
        ships_sizes = [2, 3, 3]
        for size in ships_sizes:
            ship = Ship(size)
            placed = False
            while not placed:
                if choice == 'y':
                    print(f"Placing ship of size {size}. Example: 1 2")
                    try:
                        x, y = map(int, input("Enter start row column (1-5 1-5): ").split())
                        x -= 1
                        y -= 1
                        direction = input("Horizontal? (y/n): ") == 'y'
                    except:
                        print("⚠️ Invalid input! Please try again.")
                        continue
                else:
                    x, y = random.randint(0, 4), random.randint(0, 4)
                    direction = random.choice([True, False])
                ship.place(x, y, direction)
                placed = self.board.place_ship(ship)
                if not placed and choice == 'y':
                    print("⚠️ Invalid placement. Try again.")

    def take_turn(self, enemy_board):
        while True:
            try:
                x, y = map(int, input("Enter attack coordinates (1-5 1-5): ").split())
                x -= 1
                y -= 1
                result = enemy_board.receive_attack(x, y)
                print(result)
                if "Invalid" not in result and "Already" not in result:
                    return result
                else:
                    print("⚠️ Please enter valid coordinates you haven't attacked before.")
            except:
                print("⚠️ Invalid input! Please enter two numbers between 1 and 5.")


class AIPlayer:
    def __init__(self):
        self.board = Board()
        self.memory = AILearning()
        self.setup()

    def setup(self):
        ships_sizes = [2, 3, 3]
        for size in ships_sizes:
            ship = Ship(size)
            placed = False
            while not placed:
                x, y = random.randint(0, 4), random.randint(0, 4)
                direction = random.choice([True, False])
                ship.place(x, y, direction)
                placed = self.board.place_ship(ship)

    def take_turn(self, enemy_board):
        probs = self.memory.get_probabilities()
        possible = [(i, j) for i in range(5) for j in range(5)
                    if (i, j) not in enemy_board.hits | enemy_board.misses]
        if probs:
            target = max(possible, key=lambda k: probs.get(f"{k[0]},{k[1]}", 0))
        else:
            target = random.choice(possible)
        result = enemy_board.receive_attack(*target)
        self.memory.update(target, result)
        self.memory.save()
        print(f"🤖 AI attacks ({target[0]+1}, {target[1]+1}) -> {result}")
        return result
