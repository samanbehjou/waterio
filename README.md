# SolsysGen

**SolsysGen** is a small Python library for building and simulating simple
heliocentric planetary systems using **2D circular Keplerian orbits**.

The project is intentionally minimal and educational:

- no N-body gravity  
- no orbital perturbations  
- no external physics engines  

It focuses on **clarity**, **determinism**, and **easy experimentation**.

---

## Project layout



SolsysGen/
├── src/
│ ├── solsysgen/ # Core simulation & data model
│ └── waterio/ # Optional checkpoint / I/O helpers
├── examples/ # Runnable example scripts
├── tests/ # Pytest test suite
├── docs/ # MkDocs API documentation
├── mkdocs.yml
├── pyproject.toml
└── README.md


**Notes**
- Optional native / Cython acceleration lives next to the Python code.
- Build artifacts (`build/`, `*.so`, `__pycache__/`, `*.egg-info/`) are not committed.

---

## Core concepts

### Sun
Represents the central body with:
- mass
- radius
- luminosity

All quantities are stored in **SI units**.

---

### Planet
A planet on a **2D circular orbit**, defined by:
- orbital distance
- phase angle (initial position)
- orbital period and speed (derived from Kepler’s third law)

The planet model is intentionally simple and stable.

---

### SolarSystem
A container holding:
- one `Sun`
- a list of `Planet` objects

Provides:
- time stepping
- access to current positions
- JSON-friendly serialization

---

## Orbital mechanics

- Uses **Kepler’s third law** for circular two-body orbits
- Computes:
  - orbital period from distance
  - circular orbital speed
- Implemented in pure Python  
- Optional native / accelerated backends may be used if available

This is **not** an N-body integrator.

---

## Procedural generation

SolsysGen can generate deterministic, visually plausible systems:

- logarithmically spaced orbital distances
- simple planet type classification:
  - rocky
  - gas giant
  - ice giant
  - dwarf
- rough mass and radius heuristics per type

This is intended for demos, testing, and visualization — **not scientific realism**.

---

## I/O and checkpoints

### JSON
Solar systems can be exported and reloaded via JSON for reproducibility.

### NPZ checkpoints (optional)
The `waterio` module provides helpers to:
- save NumPy arrays to compressed `.npz` files
- reload them safely for analysis or visualization

This is useful for storing time-series data such as planet positions.

---

## Examples

Run examples from the project root:

```bash
python examples/generate_and_summarize.py
python examples/track_one_planet.py
python examples/json_roundtrip_check.py
python examples/checkpoint_positions_npz.py
python examples/cython_planet_smoke.py

```

## Testing

### Run the test suite with:

```bash
pytest
```

Tests cover:
- Kepler formulas (Python and native)
- Model behavior
- Procedural generation
- System stepping
- Presets

---


## Intended use

SolsysGen is suitable for:

- educational demos,
- teaching orbital mechanics basics,
- visualization experiments,
- lightweight simulations where clarity matters more than realism.

It is not intended for high-precision astrophysical modeling.
