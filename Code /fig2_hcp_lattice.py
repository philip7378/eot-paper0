#!/usr/bin/env python3
"""
fig2_hcp_lattice.py

Draw a 2D projection of the HCP lattice with layers colored by parity.
Shows three layers (k=0,1,2) with nodes colored according to state (alternating).
"""

import matplotlib.pyplot as plt
import numpy as np

def layer_nodes(k, shift, size=2):
    """Return x,y positions for a triangular layer k, with a given shift."""
    positions = []
    for i in range(-size, size+1):
        for j in range(-size, size+1):
            if abs(i) + abs(j) + abs(i+j) <= 2*size:  # hexagonal shape
                x = i + 0.5*j + shift
                y = (np.sqrt(3)/2) * j
                positions.append((x, y))
    return positions

def main():
    fig, ax = plt.subplots(figsize=(10,8))
    colors = ['red', 'blue']  # colors for two states (layer parity)
    layers = [0,1,2]
    shifts = [0.0, 0.5, 0.0]  # ABAB stacking: shift every other layer

    for k, shift in zip(layers, shifts):
        nodes = layer_nodes(k, shift, size=3)
        color = colors[k % 2]
        for (x,y) in nodes:
            ax.plot(x, y, 'o', color=color, markersize=10, markeredgecolor='black')

    ax.set_aspect('equal')
    ax.set_title("Figure 2: HCP lattice with alternating layers\n(red: even layers, blue: odd layers)")
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('fig2_hcp_lattice.png', dpi=300, bbox_inches='tight')
    plt.savefig('fig2_hcp_lattice.pdf', bbox_inches='tight')
    print("Generated fig2_hcp_lattice.png and fig2_hcp_lattice.pdf")

if __name__ == "__main__":
    main()
