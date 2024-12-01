import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

def visualize_scores_over_time(scores_over_time):
    """
    Visualizes agent scores for each round in a 10x10 grid with top scorers outlined.
    Args:
        scores_over_time: A 3D NumPy array (rounds x grid_size x grid_size).
    """
    num_rounds = scores_over_time.shape[0]
    grid_size = scores_over_time.shape[1]

    # Set up a 10xN grid for N rounds
    n_cols = 10
    n_rows = 4
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(20, 20), constrained_layout=True)
    axes = axes.flatten()

    for round_num in range(num_rounds):
        scores = scores_over_time[round_num]
        ax = axes[round_num]

        # Find the top score and corresponding agent positions
        top_score = np.max(scores)
        top_agents = np.argwhere(scores == top_score)

        # Display the scores as a heatmap
        im = ax.matshow(scores, cmap="coolwarm")
        ax.set_title(f"R{round_num + 1}\nTS: {top_score}", fontsize=6)
        ax.axis("off")

        # Highlight top-scoring agents
        for (row, col) in top_agents:
            ax.add_patch(Rectangle((col - 0.5, row - 0.5), 1, 1, fill=False,
                                    edgecolor="yellow", linewidth=1))

    # Hide any unused subplots (in case of fewer rounds)
    for ax in axes[num_rounds:]:
        ax.axis("off")

    # Add a single colorbar for reference
    fig.colorbar(im, ax=axes[-1], orientation='horizontal', fraction=0.02, pad=0.1)

    plt.show()
