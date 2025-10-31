#Implement any one of the Local Search techniques.

import random

def hill_climbing(problem):
    current = problem.initial_state
    while True:
        neighbors = problem.get_neighbors(current)
        if not neighbors:
            break
        next = max(neighbors, key=problem.evaluate)
        if problem.evaluate(next) <= problem.evaluate(current):
            break
        current = next
    return current
class SampleProblem:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def get_neighbors(self, state):
        # Generate neighboring states (for simplicity, just return random states)
        neighbors = []
        for _ in range(5):
            neighbor = state + random.randint(-10, 10)
            neighbors.append(neighbor)
        return neighbors

    def evaluate(self, state):
        # Objective function: we want to maximize this function
        return -1 * (state - 50) ** 2  # Peak at state = 50
    
if __name__ == "__main__":
    problem = SampleProblem(initial_state=random.randint(0, 100))
    solution = hill_climbing(problem)
    print("Best state found:", solution)
    print("Objective value:", problem.evaluate(solution))