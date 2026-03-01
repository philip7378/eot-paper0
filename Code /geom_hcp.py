
#!/usr/bin/env python3
"""
geom_hcp.py

Build an HCP patch using real‑space coordinates and a distance cutoff.
Useful as an independent verification of the combinatorial builder.
"""

import math
from collections import defaultdict

def make_hcp_positions(R=6, L=10, a=1.0):
    """
    Generate node coordinates for an HCP patch.
    Returns a dict: node label (i,j,k) -> (x,y,z).
    """
    positions = {}
    dz = math.sqrt(2.0/3.0) * a   # layer spacing
    for k in range(L):
        z = k * dz
        # ABAB stacking: shift every other layer by a/2 in x
        layer_shift = 0.0 if (k % 2 == 0) else a * 0.5
        for i in range(-R, R+1):
            for j in range(-R, R+1):
                # approximate hexagonal shape in plane (optional pruning)
                x = a * (i + 0.5*j) + layer_shift
                y = a * (math.sqrt(3)/2) * j
                positions[(i,j,k)] = (x,y,z)
    return positions

def build_adj_from_positions(posdict, cutoff=1.05):
    """
    Build adjacency from Euclidean distances.
    cutoff should be slightly larger than nearest‑neighbour distance (1.0).
    """
    nodes = list(posdict.keys())
    coords = posdict
    adj = {n: set() for n in nodes}
    cutoff2 = cutoff * cutoff
    for i, n1 in enumerate(nodes):
        x1, y1, z1 = coords[n1]
        for j in range(i+1, len(nodes)):
            n2 = nodes[j]
            x2, y2, z2 = coords[n2]
            dx, dy, dz = x1-x2, y1-y2, z1-z2
            if dx*dx + dy*dy + dz*dz <= cutoff2:
                adj[n1].add(n2)
                adj[n2].add(n1)
    return adj

# Example usage (commented out)
# if __name__ == "__main__":
#     pos = make_hcp_positions(R=5, L=6, a=1.0)
#     adj = build_adj_from_positions(pos, cutoff=1.05)
#     print(f"Built graph with {len(adj)} nodes.")
