
#!/usr/bin/env python3
"""
fig3_prism_motif.py

Draw the six-node triangular prism motif in the HCP lattice,
highlighting an external node with three connections (odd boundary degree).
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def main():
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, projection='3d')

    # Coordinates for the six motif nodes (two triangles)
    # Bottom triangle (layer z=0)
    bottom = np.array([[0,0,0], [1,0,0], [0.5, np.sqrt(3)/2, 0]])
    # Top triangle (layer z=1), shifted for AB stacking
    top = bottom + np.array([0.5, 0.0, 1.0])

    # External node above, with three connections to the top triangle
    external = np.array([0.5, 0.5, 2.0])

    # Plot nodes
    ax.scatter(*bottom.T, color='blue', s=100, label='Bottom layer (even)')
    ax.scatter(*top.T, color='red', s=100, label='Top layer (odd)')
    ax.scatter(*external, color='green', s=200, marker='^', label='External node (k=3)')

    # Connect edges within motif
    for i in range(3):
        # bottom edges
        ax.plot([bottom[i][0], bottom[(i+1)%3][0]],
                [bottom[i][1], bottom[(i+1)%3][1]],
                [bottom[i][2], bottom[(i+1)%3][2]], color='gray', linestyle='--')
        # top edges
        ax.plot([top[i][0], top[(i+1)%3][0]],
                [top[i][1], top[(i+1)%3][1]],
                [top[i][2], top[(i+1)%3][2]], color='gray', linestyle='--')
        # vertical edges
        ax.plot([bottom[i][0], top[i][0]],
                [bottom[i][1], top[i][1]],
                [bottom[i][2], top[i][2]], color='gray', linestyle='--')

    # Connect external node to top triangle
    for i in range(3):
        ax.plot([external[0], top[i][0]],
                [external[1], top[i][1]],
                [external[2], top[i][2]], color='green', linewidth=3, alpha=0.7)

    # Annotate
    ax.text(0.5, 0.5, 2.2, "k=3", color='green', fontsize=14)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title("Figure 3: Triangular prism motif and odd boundary connection")
    ax.legend()

    plt.tight_layout()
    plt.savefig('fig3_prism_motif.png', dpi=300, bbox_inches='tight')
    plt.savefig('fig3_prism_motif.pdf', bbox_inches='tight')
    print("Generated fig3_prism_motif.png and fig3_prism_motif.pdf")

if __name__ == "__main__":
    main()
