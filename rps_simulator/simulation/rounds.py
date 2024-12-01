import ray

def simulate_round(grid):
    """Simulates a single round of the game."""
    grid_size = grid.shape[0]
    all_results = []

    # Fetch neighbors for all agents
    neighbors_dict = {}
    for i in range(grid_size):
        for j in range(grid_size):
            neighbors_dict[(i, j)] = ray.get(grid[i, j].get_neighbors.remote())

    # Simulate games and collect results
    for i in range(grid_size):
        for j in range(grid_size):
            neighbors = neighbors_dict[(i, j)]
            neighbor_moves = ray.get([neighbor.get_move.remote() for neighbor in neighbors])
            
            # Play games against each neighbor
            results = [ray.get(grid[i, j].play_game.remote(move)) for move in neighbor_moves]
            ray.get(grid[i, j].update_score.remote(sum(results)))
            all_results.append(results)
            
            # Pass neighbor moves to decide the next move
            grid[i, j].decide_next_move.remote(neighbor_moves)

    return all_results
