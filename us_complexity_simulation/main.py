#!uscs/bin/python3

from src.config import *
from src.actors.agent_actor import AgentActor
from src.actors.environment_actor import EnvironmentActor
from src.simulation.coordinator import SimulationCoordinator
import queue
import random

if __name__ == "__main__":
    try:
        # Create agents
        agents = [
            AgentActor(
                agent_id=i,
                attributes={"diversity": random.uniform(0, diversity_level)},
                mailbox=queue.Queue(),
                config={
                    "rule_following_probability": rule_following_probability,
                    "independence_level": independence_level,
                    "adaptability_rate": adaptability_rate
                }
            )
            for i in range(30)  # Example: 10 agents
        ]

        # Create environment
        environment = EnvironmentActor(
            agents=agents,
            config={"network_density": network_density}
        )

        # Coordinate simulation
        coordinator = SimulationCoordinator(agents=agents, environment=environment)

        print("Simulation starting...")
        coordinator.start_simulation(iterations=100000)  # Run for 5 iterations
        
        # Print the payoff summary
        coordinator.get_summary()

        coordinator.stop_simulation()

        # Print the payoff summary
        coordinator.get_summary()

    except KeyboardInterrupt:
        print("\nSimulation interrupted by user.")
        coordinator.stop_simulation()

    except Exception as e:
        print(f"An error occurred: {e}")
        coordinator.stop_simulation()