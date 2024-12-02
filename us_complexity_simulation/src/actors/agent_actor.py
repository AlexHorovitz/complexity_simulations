import random
import queue
import threading

class AgentActor(threading.Thread):
    def __init__(self, agent_id, attributes, mailbox, config):
        super().__init__()
        self.agent_id = agent_id
        self.attributes = attributes
        self.mailbox = mailbox  # Message queue for communication
        self.config = config  # Dial settings
        self.running = True
        self.payoff = 0
        self.reputation = 50  # Starting reputation score (0-100)

    def run(self):
        while self.running:
            try:
                message = self.mailbox.get(timeout=1)  # Wait for a message
                self.handle_message(message)
            except queue.Empty:
                continue

    def handle_message(self, message):
        if message["type"] == "INTERACT":
            self.interact(message["data"])
        elif message["type"] == "ADAPT":
            self.adapt(message["outcome"])
        elif message["type"] == "SHUTDOWN":
            self.running = False

    def interact(self, neighbor):
        """Interaction logic based on rule-following and independence."""
        if random.random() < self.config["rule_following_probability"]:
            # Follow rules (e.g., cooperation)
            self.payoff += 10
            neighbor.payoff += 10  # Directly access neighbor's payoff
            print(f"{self.agent_id} cooperated with {neighbor.agent_id}. +10 each.")
        else:
            # Independent behavior
            if random.random() < self.config["independence_level"]:
                self.payoff += 15  # Compete
                print(f"{self.agent_id} competed with {neighbor.agent_id}. +15 for {self.agent_id}.")
            else:
                self.payoff += 5  # Neutral
                print(f"{self.agent_id} acted neutrally with {neighbor.agent_id}. +5 for {self.agent_id}.")


    def adapt(self, outcome):
        """Adjust behavior based on adaptability."""
        adjustment = outcome * self.config["adaptability_rate"]
        self.attributes["diversity"] += adjustment

    def __str__(self):
        return f"Agent({self.agent_id}, Payoff: {self.payoff}, Reputation: {self.reputation})"
