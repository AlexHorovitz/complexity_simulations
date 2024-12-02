#!rps/bin/python3.11
import ray
import numpy as np
from simulation.grid import create_grid, assign_neighbors
from simulation.rounds import simulate_round
from visualization.visualizer import visualize_scores_over_time

def main():
    ray.init()

    # Initialize grid
    grid_size = 8
    grid = create_grid(grid_size)
    assign_neighbors(grid)

    # Simulate 100 rounds and collect round-specific scores
    rounds = 40
    round_scores = []

    for round_num in range(rounds):
        print(f"Simulating Round {round_num + 1}")

        # Simulate the round and collect scores
        simulate_round(grid)
        scores = np.array([[ray.get(agent.get_score.remote()) for agent in row] for row in grid])

        # Reset scores after collecting round-specific data
        for i in range(grid_size):
            for j in range(grid_size):
                ray.get(grid[i, j].update_score.remote(-ray.get(grid[i, j].get_score.remote())))

        round_scores.append(scores)

    # Convert to a 3D array (rounds x grid_size x grid_size)
    round_scores = np.array(round_scores)

    # Visualize all rounds
    visualize_scores_over_time(round_scores)

if __name__ == "__main__":
    main()