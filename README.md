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
```
# Paper 1 Code: Finite Sensitivity and Emergent Geometry

This directory contains Python scripts to reproduce the numerical experiments and figures for Paper 1 of Equilibrium Ordering Theory.

## Requirements

- Python 3.8+
- Required packages: `networkx`, `numpy`, `matplotlib`
- [nauty](http://users.cecs.anu.edu.au/~bdm/nauty/) (for canonical canonical labeling) – specifically the `labelg` program must be in your PATH.

## Scripts

| Script | Description |
|--------|-------------|
| `motif_enumeration.py` | Enumerates all connected subgraphs up to size 12, canonicalizes with nauty, tests admissibility, and outputs a JSON certificate. |
| `propagation_speed.py` | Simulates perturbation spreading and measures propagation speed. **Note:** Requires a list of admissible motifs (from enumeration). |
| `growth_measurement.py` | Measures the ball growth function |B_r| and fits the exponent d. |
| `fig1_conceptual.py` | Generates Figure 1: conceptual diagram of EOT. |
| `fig2_hcp_lattice.py` | Generates Figure 2: HCP lattice with alternating layers. |
| `fig3_prism_motif.py` | Generates Figure 3: triangular prism motif and odd boundary node. |
| `verify_enumeration.py` | Verifies the SHA256 hash of the JSON certificate and optionally re‑tests a few motifs. |

## Usage

1. Ensure nauty is installed and `labelg` is in your PATH.
2. Run each script from the command line:
