import threading  # Import threading module
import networkx as nx  # For managing the network of agents

class EnvironmentActor(threading.Thread):
    def __init__(self, agents, config):
        super().__init__()
        self.agents = agents  # List of agent actors
        self.config = config  # Simulation configuration
        self.network = self.create_network(len(agents), config["network_density"])
        self.running = True

    def run(self):
        while self.running:
            self.broadcast_interactions()

    def create_network(self, num_agents, density):
        """Generate a network with adjustable density."""
        return nx.erdos_renyi_graph(num_agents, density)

    def broadcast_interactions(self):
        """Send interaction messages to connected agents."""
        for agent in self.agents:
            neighbors = list(self.network.neighbors(agent.agent_id))
            for neighbor_id in neighbors:
                neighbor = self.agents[neighbor_id]
                print(f"Agent {agent.agent_id} interacting with Agent {neighbor.agent_id}")
                agent.mailbox.put({"type": "INTERACT", "data": neighbor})  # Pass the neighbor as an object



    def stop(self):
        for agent in self.agents:
            agent.mailbox.put({"type": "SHUTDOWN"})
        self.running = False
