# Equilibrium Ordering Theory (EOT) – Paper 0 Code

This repository contains the Python scripts used for numerical verification in the paper  
**"Mathematical Foundations of Equilibrium Ordering Theory (Paper 0)"**.

## Requirements
- Python 3.7 or higher
- No external libraries needed (only standard library)

## Scripts
- `prism_violation.py` – Tests the six‑node triangular prism flip on an HCP lattice.
- `slip_plane_test.py` – Verifies that a slip‑plane shift preserves equilibrium.
- `find_alternating_cycles.py` – Searches for alternating cycles (candidates for loop‑exchange moves).
- `geom_hcp.py` – Alternative geometric HCP builder (uses coordinates and distance cutoff).

## Running the code
Simply execute any script from the command line:
```bash
python prism_violation.py
