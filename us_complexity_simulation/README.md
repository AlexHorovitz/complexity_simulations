# Complexity Simulation with Actor Model

This project simulates the challenges of constructing a Rawlsian-style social contract among the 50 U.S. states, using the **Actor Model** to represent states as independent agents interacting in a dynamic environment. The simulation explores how diversity, the number of agents, and resource disparities affect the ability to form stable and equitable policies.

## Key Features

- **Actor Model Architecture**: Each state operates as an independent actor, processing messages and interacting asynchronously.
- **Real-World Data Integration**: Incorporates demographic and economic data for U.S. states.
- **Dynamic Interactions**: Models policy negotiations, resource exchanges, and coalition formations between states.
- **Evaluation Metrics**: Measures fairness, stability, and satisfaction of the social contract over iterations.
- **Visualization Tools**: Generates maps and charts to visualize simulation outcomes.

## Project Structure

```plaintext
us_complexity_simulation/
├── data/                   # Input data and outputs
│   ├── demographics.csv    # State demographic data
│   ├── policies.json       # Optional: predefined policies
│   ├── results/            # Simulation outputs
│       ├── scenario1.json
│       └── scenario2.json
├── src/                    # Source code
│   ├── main.py             # Entry point of the application
│   ├── config.py           # Configuration settings
│   ├── actors/             # Actor definitions
│   │   ├── state_actor.py  # State-level actor logic
│   │   ├── environment_actor.py  # Environment managing actor
│   │   └── messages.py     # Message types for communication
│   ├── simulation/         # Core simulation logic
│   │   ├── coordinator.py  # Manages simulation lifecycle
│   │   ├── metrics.py      # Evaluation metrics
│   │   └── policy_engine.py # Policy negotiation logic
│   ├── data_processing/    # Data loading and preprocessing
│   │   ├── load_data.py    # Reads and validates input data
│   │   └── preprocess.py   # Cleans and transforms data
│   ├── visualization/      # Visualization tools
│       ├── charts.py       # Plotting tools
│       └── maps.py         # Geographic visualizations
├── tests/                  # Unit and integration tests
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Ignored files for version control

