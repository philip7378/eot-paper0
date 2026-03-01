#!/usr/bin/env python3
"""
fig1_conceptual.py

Generate a conceptual diagram of the EOT structure:
- A set of vertices (configurations)
- A subset marked as "admissible"
- Directed arrows between admissible vertices representing successor steps
- One highlighted infinite path
"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def main():
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes: 12 nodes in a rough circle, plus a few extra
    n_nodes = 15
    pos = nx.circular_layout(range(n_nodes))  # circular positions

    # Add edges to create a DAG-like structure with branching and merging
    edges = [
        (0,1), (0,2), (1,3), (1,4), (2,5), (2,6), (3,7), (4,7), (5,8), (6,8),
        (7,9), (8,9), (9,10), (10,11), (11,12), (12,13), (13,14), (14,0)  # long path
    ]
    G.add_edges_from(edges)

    # Define admissible nodes (some subset)
    admissible = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]  # all for simplicity; we can highlight path

    # Path to highlight (infinite realization)
    path = [0,1,3,7,9,10,11,12,13,14,0]  # a cycle; we'll show as path by repeating
    # But to avoid clutter, just show a sequence
    path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]

    # Plot
    plt.figure(figsize=(8,8))
    nx.draw_networkx_nodes(G, pos, nodelist=admissible, node_color='lightblue', node_size=500, alpha=0.8)
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red', node_size=600, alpha=1.0)
    nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='->', arrowsize=20, edge_color='gray', width=1.5)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, arrowstyle='->', arrowsize=20, edge_color='red', width=3)
    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

    plt.title("Figure 1: Conceptual structure of EOT\n(Red nodes and edges show an infinite realization)")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('fig1_conceptual.png', dpi=300, bbox_inches='tight')
    plt.savefig('fig1_conceptual.pdf', bbox_inches='tight')
    print("Generated fig1_conceptual.png and fig1_conceptual.pdf")

if __name__ == "__main__":
    main()
