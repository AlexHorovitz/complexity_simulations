import random
import queue
import threading

class AgentActor(threading.Thread):
    def __init__(self, agent_id, attributes, mailbox, config):
        """
        Initializes an AgentActor instance.

        :param agent_id: Unique identifier for the agent.
        :param attributes: Dictionary of agent-specific attributes (e.g., diversity).
        :param mailbox: Queue for inter-thread communication.
        :param config: Configuration settings (rule-following, independence, adaptability).
        """
        super().__init__()
        self.agent_id = agent_id
        self.attributes = attributes
        self.mailbox = mailbox
        self.config = config
        self.running = True
        self.payoff = 0
        self.reputation = 50  # Starting reputation score (0-100)

    def run(self):
        """
        The main loop for the agent thread. Processes messages from the mailbox.
        """
        while self.running:
            try:
                message = self.mailbox.get(timeout=1)  # Wait for messages
                self.handle_message(message)
            except queue.Empty:
                continue

    def handle_message(self, message):
        """
        Processes messages sent to the agent.

        :param message: Dictionary containing message type and data.
        """
        if message["type"] == "INTERACT":
            self.interact(message["data"])
        elif message["type"] == "ADAPT":
            self.adapt(message["outcome"])
        elif message["type"] == "SHUTDOWN":
            self.running = False

    def interact(self, neighbor):
        """
        Handles interaction with a neighbor.

        :param neighbor: Another AgentActor instance.
        """
        if random.random() < self.config["rule_following_probability"]:
            # Follow rules (e.g., cooperation)
            self.payoff += 10
            neighbor.payoff += 10  # Directly access neighbor's payoff
            print(f"Agent {self.agent_id} cooperated with Agent {neighbor.agent_id}. +10 each.")
        else:
            # Independent behavior
            if random.random() < self.config["independence_level"]:
                self.payoff += 15  # Compete
                print(f"Agent {self.agent_id} competed with Agent {neighbor.agent_id}. +15 for Agent {self.agent_id}.")
            else:
                self.payoff += 5  # Neutral
                print(f"Agent {self.agent_id} acted neutrally with Agent {neighbor.agent_id}. +5 for Agent {self.agent_id}.")

    def adapt(self, outcome):
        """
        Adjusts the agent's attributes based on the outcome of an interaction.

        :param outcome: Numeric outcome from an interaction (e.g., success or failure).
        """
        adjustment = outcome * self.config["adaptability_rate"]
        self.attributes["diversity"] += adjustment
        print(f"Agent {self.agent_id} adapted. Diversity now {self.attributes['diversity']}.")

    def stop(self):
        """
        Signals the agent to stop running.
        """
        self.running = False

    def __str__(self):
        """
        String representation of the agent's current state.
        """
        return f"Agent({self.agent_id}, Payoff: {self.payoff}, Reputation: {self.reputation})"
