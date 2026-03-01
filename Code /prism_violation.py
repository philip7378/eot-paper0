
#!/usr/bin/env python3
"""
prism_violation.py

Test the six‑node triangular prism flip on a parity‑correct HCP lattice.
Verifies the Even‑Intersection Lemma: flipping the prism motif violates
local equilibrium for interior nodes with odd boundary degree.

Outputs the number of violations before and after the flip,
with sample violating nodes.
"""

# Offsets for HCP neighbours (corrected for ABAB stacking)
SAME_OFFSETS = [(1,0), (-1,0), (0,1), (0,-1), (1,-1), (-1,1)]
UP_OFFSETS   = [(0,0), (-1,0), (0,-1)]
DOWN_OFFSETS = [(0,0), (1,0), (0,1)]

def build_hcp_patch(R=5, L=6):
    """
    Build a finite HCP patch with horizontal radius R and L layers.
    Returns adjacency dict: node -> set of neighbours.
    Nodes are tuples (i,j,k).
    """
    nodes = [(i,j,k) for k in range(L)
             for i in range(-R, R+1)
             for j in range(-R, R+1)]
    nodeset = set(nodes)
    adj = {n: set() for n in nodes}
    for (i,j,k) in nodes:
        # same layer neighbours
        for di,dj in SAME_OFFSETS:
            nb = (i+di, j+dj, k)
            if nb in nodeset:
                adj[(i,j,k)].add(nb)
        # up layer
        if k+1 < L:
            for di,dj in UP_OFFSETS:
                nb = (i+di, j+dj, k+1)
                if nb in nodeset:
                    adj[(i,j,k)].add(nb)
        # down layer
        if k-1 >= 0:
            for di,dj in DOWN_OFFSETS:
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
    # All nodes possibly affected (motif + neighbours)
    affected = set(motif)
    for v in motif:
        affected.update(adj[v])
    # Only interior nodes (degree 12) are checked
    interior = [v for v in affected if len(adj[v]) == 12]

    # Pre‑flip check
    init_viol = sum(1 for v in interior if count_opposite(adj, state, v) != 6)
    print("Initial violations:", init_viol)

    # Flip motif
    state2 = dict(state)
    for v in motif:
        state2[v] = 1 - state2[v]

    # Collect violations after flip
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
