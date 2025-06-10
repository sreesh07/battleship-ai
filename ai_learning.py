import json
import os

class AILearning:
    def __init__(self, filename="ai_memory.json"):
        self.filename = filename
        self.memory = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return {}

    def update(self, coord, result):
        key = f"{coord[0]},{coord[1]}"
        if key not in self.memory:
            self.memory[key] = {"hit": 0, "miss": 0}
        if result.startswith("🎯"):
            self.memory[key]["hit"] += 1
        elif result.startswith("💨"):
            self.memory[key]["miss"] += 1

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.memory, f)

    def get_probabilities(self):
        probs = {}
        for key, value in self.memory.items():
            total = value["hit"] + value["miss"]
            if total:
                probs[key] = value["hit"] / total
        return probs

    def get_evolution_percentage(self):
        learned = sum(1 for v in self.memory.values() if v['hit'] or v['miss'])
        total_possible = 25  # 5x5 grid
        return min(100, int((learned / total_possible) * 100))
