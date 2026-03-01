#!/usr/bin/env python3
"""
find_alternating_cycles.py

Search for simple cycles of even length (≤ Kmax) along which states alternate.
Uses the corrected HCP builder.
"""

import prism_violation as pv

def find_cycles(adj, state, Kmax=12):
    """Find all simple cycles of length ≤ Kmax with alternating states."""
    cycles = []
    nodes = list(adj.keys())
    for start in nodes:
        stack = [(start, [start], {start})]
        while stack:
            cur, path, seen = stack.pop()
            if len(path) > Kmax:
                continue
            for nb in adj[cur]:
                if nb == path[0] and len(path) >= 4:
                    cyc = tuple(path)
                    ok = True
                    for i in range(len(cyc)):
                        if state[cyc[i]] == state[cyc[(i+1) % len(cyc)]]:
                            ok = False
                            break
                    if ok:
                        cycles.append(cyc)
                elif nb not in seen and nb > path[0]:
                    stack.append((nb, path + [nb], seen | {nb}))
    return cycles

if __name__ == "__main__":
    adj = pv.build_hcp_patch(R=4, L=6)
    state = {v: pv.alt_state(v) for v in adj}
    cycles = find_cycles(adj, state, Kmax=12)
    print("Found alternating cycles:", len(cycles))
    if cycles:
        print("First 5 cycles:")
        for cyc in cycles[:5]:
            print(cyc)
