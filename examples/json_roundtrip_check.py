"""
Roundtrip a generated system to JSON and back, then check invariants.

Run:
  python3 examples/json_roundtrip_check.py
"""

from __future__ import annotations

import tempfile
from pathlib import Path

from solsysgen import SolarSystem, Sun, generate_planets
from solsysgen.io import load_json, save_json


def main() -> None:
    sun = Sun()
    planets = generate_planets(sun, 5, seed=10)
    system = SolarSystem(sun=sun, planets=planets)

    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / "system.json"
        save_json(path, system)

        loaded = load_json(path)

        print("Wrote:", path)
        print("Original planets:", len(system.planets))
        print("Loaded planets:  ", len(loaded.planets))

        # Invariants (should match exactly in your dataclass serialization)
        assert loaded.sun.name == system.sun.name
        assert [p.name for p in loaded.planets] == [p.name for p in system.planets]
        assert [p.kind for p in loaded.planets] == [p.kind for p in system.planets]

        print("OK: roundtrip invariants match.")


if __name__ == "__main__":
    main()
