#!rps/bin/python3

import ray
import numpy as np
import argparse
from simulation.grid import create_grid, assign_neighbors
from simulation.rounds import simulate_round
from visualization.visualizer import visualize_scores_over_time

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run the Rock-Paper-Scissors simulation.")
    parser.add_argument("--grid-size", type=int, default=8, help="Size of the grid (NxN)")
    parser.add_argument("--rounds", type=int, default=100, help="Number of rounds to simulate")
    parser.add_argument("--randomness", type=float, default=0.1, 
                        help="Probability of choosing a random move (0 to 1)")
    args = parser.parse_args()

    # Initialize Ray
    ray.init()

    # Initialize grid
    grid_size = args.grid_size
    grid = create_grid(grid_size)
    assign_neighbors(grid)

    # Pass randomness probability to agents
    for i in range(grid_size):
        for j in range(grid_size):
            grid[i, j].set_randomness.remote(args.randomness)

    # Simulate rounds and collect round-specific scores
    rounds = args.rounds
    round_scores = []

    for round_num in range(rounds):
        print(f"Simulating Round {round_num + 1}")
        simulate_round(grid)

        # Collect scores for the round
        scores = np.array([[ray.get(agent.get_score.remote()) for agent in row] for row in grid])

        # Reset scores after collecting round-specific data
        for i in range(grid_size):
            for j in range(grid_size):
                ray.get(grid[i, j].update_score.remote(-ray.get(grid[i, j].get_score.remote())))

        round_scores.append(scores)

    # Convert to a 3D array (rounds x grid_size x grid_size)
    round_scores = np.array(round_scores)

    # Visualize results
    visualize_scores_over_time(round_scores)

if __name__ == "__main__":
    main()
