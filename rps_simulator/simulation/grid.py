import ray
from agents.agent import Agent
import numpy as np

def create_grid(grid_size):
    agents = np.empty((grid_size, grid_size), dtype=object)
    for i in range(grid_size):
        for j in range(grid_size):
            agents[i, j] = Agent.remote((i, j), np.random.choice(["R", "P", "S"]))
    return agents

def assign_neighbors(grid):
    """Assigns neighbors to each agent."""
    grid_size = grid.shape[0]
    for i in range(grid_size):
        for j in range(grid_size):
            neighbors = []
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x == 0 and y == 0:
                        continue
                    ni, nj = i + x, j + y
                    if 0 <= ni < grid_size and 0 <= nj < grid_size:
                        neighbors.append(grid[ni, nj])  # Append actor handles
            # Ensure neighbors are added individually, not as a list
            for neighbor in neighbors:
                ray.get(grid[i, j].add_neighbor.remote(neighbor))


