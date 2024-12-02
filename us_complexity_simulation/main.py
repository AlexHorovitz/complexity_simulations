#!uscs/bin/python3

from src.config import *
from src.actors.agent_actor import AgentActor
from src.actors.environment_actor import EnvironmentActor
from src.simulation.coordinator import SimulationCoordinator
import queue
import random

if __name__ == "__main__":
    # Create agents
    agents = [
        AgentActor(agent_id=i, 
                   attributes={"diversity": random.uniform(0, diversity_level)}, 
                   mailbox=queue.Queue(), 
                   config={
                       "rule_following_probability": rule_following_probability,
                       "independence_level": independence_level,
                       "adaptability_rate": adaptability_rate
                   })
        for i in range(10)  # Example with 10 agents
    ]

    # Create environment
    environment = EnvironmentActor(agents, config={
        "network_density": network_density
    })

    # Coordinate simulation
    coordinator = SimulationCoordinator(agents, environment)
    try:
        coordinator.start_simulation(iterations=100)
    except KeyboardInterrupt:
        print("Stopping simulation.")
        coordinator.stop_simulation()