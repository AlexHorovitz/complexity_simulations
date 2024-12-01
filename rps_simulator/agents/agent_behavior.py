def play_round(agent, neighbors):
    results = []
    for neighbor in neighbors:
        neighbor_move = ray.get(neighbor.get_move.remote())
        result = agent.play_game(neighbor_move)
        results.append(result)
        agent.update_score(result)
    return results
