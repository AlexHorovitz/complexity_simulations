
# Rock-Paper-Scissors Grid Simulation

This project simulates a **Rock-Paper-Scissors** game played by agents on an 8x8 grid. Each agent competes against its adjacent neighbors, adapting its moves over multiple rounds to maximize its score. The simulation visualizes scores for each round, highlights top-performing agents, and allows customization of simulation parameters such as the number of rounds and randomness in decision-making.

## Features

- Simulates an **8x8 grid** of agents playing Rock-Paper-Scissors with neighbors.
- Tracks scores per round and highlights top-performing agents.
- Supports configurable **number of rounds** and **randomness** in decision-making.
- Visualizes results as heatmaps with highlights for top scorers.

## Requirements

- Python 3.8 or higher
- Dependencies (install using `pip`):
  - `ray`
  - `numpy`
  - `matplotlib`

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv rps
   source rps/bin/activate  # On Windows: rps\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Simulation

Run the main program using the command:
```bash
python main.py [--rounds <num_rounds>] [--randomness <probability>]
```

#### Options:
- `--rounds`: Number of rounds to simulate (default: 100).
- `--randomness`: Probability of agents making a random move (default: 0.1).

#### Examples:
- Simulate 100 rounds with 10% randomness:
  ```bash
  python main.py --rounds 100 --randomness 0.1
  ```
- Simulate 50 rounds with no randomness:
  ```bash
  python main.py --rounds 50 --randomness 0
  ```

### Output

- **Heatmaps**: Visualize the agents' scores for each round in a 10x10 grid.
- **Highlights**: Top-performing agents for each round are outlined in yellow.

## Project Structure

```
.
├── agents/
│   ├── agent.py               # Agent logic for playing and decision-making
├── simulation/
│   ├── grid.py                # Grid initialization and neighbor assignments
│   ├── rounds.py              # Logic for running a single simulation round
├── visualization/
│   ├── visualizer.py          # Visualization logic (heatmaps and highlights)
├── main.py                    # Main entry point for the simulation
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
```

## How It Works

1. **Agents**:
   - Each agent plays Rock-Paper-Scissors against its neighbors.
   - Scores are calculated per round:
     - Win: +1
     - Loss: -1
     - Draw: 0
   - Decision-making includes randomness to avoid early stabilization.

2. **Grid**:
   - An 8x8 grid of agents is initialized.
   - Each agent interacts with up to 8 adjacent neighbors.

3. **Rounds**:
   - In each round:
     - Agents decide their next move based on their neighbors' previous moves.
     - Scores are calculated for all agents.

4. **Visualization**:
   - Heatmaps show the scores for each round.
   - Top scorers are highlighted with yellow borders.

## Customization

### Modify Agent Behavior
To tweak how agents decide their next move, edit the `decide_next_move` method in `agents/agent.py`.

### Adjust Visualization
To customize heatmaps or layout, edit `visualization/visualizer.py`.

## License

This project is licensed under the [Unlicense](https://unlicense.org/). See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you have ideas or improvements, feel free to open a pull request or issue.
