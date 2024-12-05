class SimulationCoordinator:
    def __init__(self, agents, environment):
        """
        Initializes the simulation coordinator with agents and an environment.

        :param agents: List of AgentActor instances
        :param environment: An instance of EnvironmentActor
        """
        self.agents = agents
        self.environment = environment

    def start_simulation(self, iterations):
        """
        Starts the simulation for a specified number of iterations.

        :param iterations: Number of iterations to run the simulation
        """
        print(f"Starting simulation with {len(self.agents)} agents for {iterations} iterations.")
        self.environment.start()  # Start the environment thread
        for agent in self.agents:
            agent.start()  # Start each agent thread

        for iteration in range(iterations):
            print(f"\n--- Iteration {iteration + 1} ---")

        print("\nSimulation complete.")

    def stop_simulation(self):
        """
        Stops the simulation by signaling all threads to terminate.
        """
        print("\nStopping simulation...")
        self.environment.stop()  # Signal environment to stop
        for agent in self.agents:
            agent.stop()  # Signal each agent to stop

        self.environment.join()  # Wait for the environment thread to stop
        for agent in self.agents:
            agent.join()  # Wait for each agent thread to stop

        print("\nSimulation stopped.")

    def is_stable(self):
        """
        Example method to check if the simulation has reached a stable state.

        :return: True if stable, False otherwise
        """
        payoffs = [agent.payoff for agent in self.agents]
        return max(payoffs) - min(payoffs) < 5  # Example: Stable if payoff range is small

    def get_summary(self):
        """
        Collects and prints the payoff summary for all agents.
        """
        print("\n--- Payoff Summary ---")
        for agent in self.agents:
            print(f"Agent {agent.agent_id}: Payoff = {agent.payoff}, Reputation = {agent.reputation}")

