# SolsysGen & WaterIO

**SolsysGen** is a small Python library for building and simulating simple
heliocentric planetary systems using **2D circular Keplerian orbits**.  
**WaterIO** is a lightweight helper module for checkpointing NumPy arrays to
compressed `.npz` files.

The project is intentionally minimal and educational:

- no N-body gravity  
- no orbital perturbations  
- no external physics engines  

It focuses on **clarity**, **determinism**, and **reproducibility**, rather than
physical completeness.


---

## Project structure

```text
SolsysGen/
├── src/
│   ├── solsysgen/          # Core simulation & data model
│   └── waterio/            # Optional checkpoint / I/O helpers
├── docs/                   # MkDocs API documentation
├── examples/               # Runnable example scripts
├── tests/                  # Pytest test suite
├── mkdocs.yml
├── pyproject.toml
└── README.md
```


### Notes

- Optional native or Cython-based acceleration lives alongside the Python code.
- Build artifacts (`build/`, `*.so`, `__pycache__/`, `*.egg-info/`) are intentionally excluded from version control.
- The project functions fully in **pure Python** and does not require compiled extensions.

---

## SolsysGen

SolsysGen provides a small set of building blocks for heliocentric simulations.

## Core concepts

### Sun
Represents the central body (e.g. a star), defined by:

- mass  
- radius  
- luminosity  

All quantities are stored internally in **SI units**.

---

### Planet
A planet on a **2D circular orbit**, defined by:

- orbital distance  
- phase angle (initial position)  
- orbital period and orbital speed (derived from **Kepler’s third law**)  

The planet model is intentionally simple, stable, and deterministic.

---

### SolarSystem
A container holding:

- one `Sun`  
- a list of `Planet` objects  

It provides:

- explicit time stepping  
- access to current positions  
- JSON-friendly serialization  

---

## Orbital mechanics

SolsysGen uses **Kepler’s third law** for circular two-body orbits to compute:

- orbital period from distance  
- circular orbital speed  

Implementation details:

- implemented in **pure Python**  
- optional native or accelerated backends may be used if available  
- this is **not** an N-body integrator  

---

## Procedural generation

SolsysGen can generate deterministic, visually plausible systems using:

- logarithmically spaced orbital distances  
- simple planet type classification:
  - rocky  
  - gas giant  
  - ice giant  
  - dwarf  
- rough mass and radius heuristics per type  

This functionality is intended for **demos, testing, and visualization**, not scientific realism.

---

## I/O and checkpoints

### JSON export
Solar systems can be exported and reloaded via JSON for reproducibility, including:

- system structure  
- planet ordering  
- orbital parameters  

This allows generated systems to be saved and reused.

---

### NPZ checkpoints (optional)
The `waterio` module provides helpers to:

- save NumPy arrays to compressed `.npz` files  
- reload them safely for analysis or visualization  

This is especially useful for storing time-series data, such as planet positions over time.

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



Each example demonstrates a **single focused concept**.

---

## Tutorial notebook

A full guided walkthrough is provided as a Jupyter notebook:


**solsysgen_tutorial.ipynb**


---

### It demonstrates:

- system generation
- time stepping
- Kepler helper functions
- JSON export/import
- NumPy checkpointing with WaterIO

This notebook is suitable for:

- a short technical presentation
- self-guided learning
- grading or review

---

## Installation

### Requirements

- Python ≥ 3.10
- pip
- (optional) C/C++ compiler for native extension

### Basic Installation (Pure Python)

```bash
pip install cython
```

Development Installation

```bash
pip install -e .
pip install -r requirements.txt
```

Optional:

```bash
pre-commit install
```

---

### Optional native acceleration

If a native or Cython backend is present, it will be used automatically.
The project functions fully **without** it.

---

## Building Documentation

API documentation is generated from docstrings using MkDocs:

```bash
mkdocs serve
```

Then open:

http://127.0.0.1:8000/

---

## Testing

Run the test suite with:

```bash
pytest
```

### Tests cover:

- Kepler formulas
- model behavior
- procedural generation
- system stepping
- JSON and checkpoint roundtrips
- NumPy checkpointing

---
## Intended use

SolsysGen and WaterIO are suitable for:

- educational demos
- teaching orbital mechanics basics
- visualization experiments
- lightweight simulations where clarity matters more than realism

They are **not** intended for high-precision astrophysical modeling.

---
## Acknowledgement


This README was generated and prepared with the help of **AI** tools. The content was tailored to provide a clear and concise overview of the installation steps and project setup for users and developers.

