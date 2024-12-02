import random
import ray

@ray.remote
class Agent:
    def __init__(self, position, initial_move):
        self.position = position
        self.current_move = initial_move
        self.neighbors = []  # List to store neighbors
        self.score = 0
        self.randomness = 0.1  # Default randomness probability

    def add_neighbor(self, neighbor):
        """Adds a neighboring agent to the agent's list of neighbors."""
        self.neighbors.append(neighbor)

    def get_neighbors(self):
        """Returns the list of neighbors."""
        return self.neighbors

    def set_randomness(self, randomness):
        """Sets the probability of choosing a random move."""
        self.randomness = randomness

    def decide_next_move(self, neighbors_moves):
        """
        Decides the agent's next move based on neighbors' past moves.
        Adds randomness to prevent stabilization.
        """
        # Count how often each move was played
        counts = {"R": neighbors_moves.count("R"),
                  "P": neighbors_moves.count("P"),
                  "S": neighbors_moves.count("S")}

        # Choose the move that counters the most frequent move
        if counts["R"] > counts["P"] and counts["R"] > counts["S"]:
            best_move = "P"  # Paper beats Rock
        elif counts["P"] > counts["S"]:
            best_move = "S"  # Scissors beat Paper
        else:
            best_move = "R"  # Rock beats Scissors

        # Add randomness: occasionally pick a random move
        if random.random() < self.randomness:
            self.current_move = random.choice(["R", "P", "S"])
        else:
            self.current_move = best_move

    def get_move(self):
        """Returns the current move of the agent."""
        return self.current_move

    def play_game(self, neighbor_move):
        """
        Plays a game against a neighbor's move and returns the result.
        Args:
            neighbor_move: The move of the neighbor ("R", "P", or "S").
        Returns:
            1 if this agent wins, -1 if the neighbor wins, 0 for a draw.
        """
        if self.current_move == neighbor_move:
            return 0  # Draw
        elif (self.current_move == "R" and neighbor_move == "S") or \
             (self.current_move == "P" and neighbor_move == "R") or \
             (self.current_move == "S" and neighbor_move == "P"):
            return 1  # Win
        else:
            return -1  # Loss

    def update_score(self, result):
        """Updates the agent's cumulative score."""
        self.score += result

    def get_score(self):
        """Returns the cumulative score of the agent."""
        return self.score

