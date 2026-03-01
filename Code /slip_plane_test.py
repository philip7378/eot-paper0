
#!/usr/bin/env python3
"""
slip_plane_test.py

Test a slip‑plane shift on the HCP lattice: translate one whole layer
by a lattice vector and verify that interior nodes still have exactly
6 opposite neighbours.
"""

import prism_violation as pv  # reuse the HCP builder from prism_violation

def shift_plane_state(state, plane_z, shift=(1,0)):
    """
    Shift the whole layer z = plane_z by the vector (shift[0], shift[1], 0).
    Returns a new state dictionary.
    """
    new_state = dict(state)
    shifted_nodes = [(i,j,k) for (i,j,k) in state if k == plane_z]
    for (i,j,k) in shifted_nodes:
        src = (i - shift[0], j - shift[1], k)
        if src in state:
            new_state[(i,j,k)] = state[src]
        else:
            # outside patch – keep original
            new_state[(i,j,k)] = state[(i,j,k)]
    return new_state

if __name__ == "__main__":
    adj = pv.build_hcp_patch(R=6, L=8)
    state = {v: pv.alt_state(v) for v in adj}
    plane = 3
    state2 = shift_plane_state(state, plane, shift=(1,0))

    # Only interior nodes (degree 12) matter
    interior = [v for v in adj if len(adj[v]) == 12]
    viol = [v for v in interior if pv.count_opposite(adj, state2, v) != 6]
    print("Slip plane violations:", len(viol))
    if viol:
        print("First 10 violating nodes:", viol[:10])
    else:
        print("Slip plane preserves equilibrium everywhere (as expected).")
