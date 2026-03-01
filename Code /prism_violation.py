#!/usr/bin/env python3
"""
prism_violation.py (parity‑corrected)

Test the six‑node triangular prism flip on a true HCP lattice with ABAB stacking.
Implements a combinatorial builder that alternates vertical offsets depending
on layer parity.
"""

# Offsets for HCP neighbours (same for all layers)
SAME_OFFSETS = [(1,0), (-1,0), (0,1), (0,-1), (1,-1), (-1,1)]

# For a layer k, the connections to the layer above (k+1) depend on parity.
# Even layer (k even):   up offsets = [(0,0), (-1,0), (0,-1)]
# Odd layer  (k odd):    up offsets = [(0,0), (1,0), (0,1)]
UP_EVEN = [(0,0), (-1,0), (0,-1)]
UP_ODD  = [(0,0), (1,0), (0,1)]

# Down offsets are the opposite of up offsets of the other layer.
# They will be derived automatically from up offsets when building.

def build_hcp_patch(R=5, L=6):
    """
    Build a finite HCP patch with horizontal radius R and L layers.
    Correct ABAB stacking: vertical neighbours depend on layer parity.
    Returns adjacency dict: node -> set of neighbours.
    Nodes are tuples (i,j,k).
    """
    nodes = [(i,j,k) for k in range(L)
             for i in range(-R, R+1)
             for j in range(-R, R+1)]
    nodeset = set(nodes)
    adj = {n: set() for n in nodes}
    for (i,j,k) in nodes:
        # same layer neighbours (always present)
        for di,dj in SAME_OFFSETS:
            nb = (i+di, j+dj, k)
            if nb in nodeset:
                adj[(i,j,k)].add(nb)

        # up neighbours (layer k+1)
        if k+1 < L:
            # choose offsets based on parity of current layer
            up_offs = UP_EVEN if (k % 2 == 0) else UP_ODD
            for di,dj in up_offs:
                nb = (i+di, j+dj, k+1)
                if nb in nodeset:
                    adj[(i,j,k)].add(nb)

        # down neighbours (layer k-1)
        if k-1 >= 0:
            # down offsets are the same as the up offsets of the layer below
            # but we can derive them by symmetry: the down offsets for layer k
            # are the up offsets of layer k-1.
            down_offs = UP_EVEN if ((k-1) % 2 == 0) else UP_ODD
            for di,dj in down_offs:
                nb = (i+di, j+dj, k-1)
                if nb in nodeset:
                    adj[(i,j,k)].add(nb)
    return adj

def alt_state(v):
    """Alternating‑layer state: parity of layer index."""
    return v[2] % 2

def count_opposite(adj, state, v):
    """Number of neighbours of v with opposite state."""
    return sum(1 for nb in adj[v] if state[nb] != state[v])

if __name__ == "__main__":
    adj = build_hcp_patch(R=5, L=6)
    state = {v: alt_state(v) for v in adj}

    # Triangular prism motif: three nodes in layer 2 and three in layer 3
    M = [(0,0,2), (1,0,2), (0,1,2), (0,0,3), (1,0,3), (0,1,3)]
    motif = {v for v in M if v in adj}
    affected = set(motif)
    for v in motif:
        affected.update(adj[v])
    interior = [v for v in affected if len(adj[v]) == 12]

    # pre‑flip check
    init_viol = sum(1 for v in interior if count_opposite(adj, state, v) != 6)
    print("Initial violations:", init_viol)

    # flip motif
    state2 = dict(state)
    for v in motif:
        state2[v] = 1 - state2[v]

    motif_viol, boundary_viol = [], []
    for v in interior:
        c = count_opposite(adj, state2, v)
        if c != 6:
            if v in motif:
                motif_viol.append((v, c))
            else:
                boundary_viol.append((v, c))

    print("Post‑flip violations:", len(motif_viol) + len(boundary_viol))
    if motif_viol:
        print("Sample motif nodes (node -> opposite count):")
        for v,c in motif_viol[:3]:
            print(f"   {v} -> {c}")
    if boundary_viol:
        print("Sample boundary nodes:")
        for v,c in boundary_viol[:3]:
            print(f"   {v} -> {c}")
