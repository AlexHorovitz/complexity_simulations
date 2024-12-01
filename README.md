# Complexity Simulations

This repository contains simulations that explore the principles of complexity and emergent behavior in multi-agent systems. The simulations draw inspiration from Scott Page's complexity lectures and are designed to model dynamic interactions, adaptation, and negotiation in diverse settings.

## Simulations Included

### 1. **Complexity Simulation with Actor Model**
   - **Directory**: [`us_complexity_simulation/`](us_complexity_simulation)
   - **Description**: 
     - Models the challenges of constructing a Rawlsian-style social contract among the 50 U.S. states using the **Actor Model**.
     - Each state is an independent actor that interacts asynchronously through message passing.
   - **Key Features**:
     - Actor-based architecture for parallelism.
     - Incorporates real-world U.S. state demographic and economic data.
     - Explores the impact of diversity, resources, and negotiation on stability.
   - **Metrics**:
     - Fairness, stability, and satisfaction of the social contract.
   - **Run Instructions**:
     See the [local README](complexity_simulation_actor_model/README.md).

---

### 2. **Rock-Paper-Scissors Simulator**
   - **Directory**: [`rps_simulator/`](rps_simulator)
   - **Description**:
     - Simulates the evolution of strategies in a **Rock-Paper-Scissors game** on an 8x8 checkers board.
     - Agents interact only with adjacent neighbors, updating their strategy based on the outcomes of past games.
     - Explores emergent patterns and cyclical dynamics.
   - **Key Features**:
     - Grid-based agent interactions.
     - Strategy evolution using reinforcement learning or simple heuristics.
     - Visual representation of agent strategies over time.
   - **Metrics**:
     - Stability of strategies and emergent spatial patterns.
   - **Run Instructions**:
     See the [local README](rps_simulator/README.md).

---

