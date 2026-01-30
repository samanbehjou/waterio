"""
Smoke test for the optional Cython extension.

Goal:
- If the compiled Cython Planet exists and supports the legacy signature:
    Planet(name, mass, radius)
  then instantiate it.
- Otherwise, fall back to the pure-Python dataclass Planet signature used by solsysgen.models.

Run:
  python3 examples/cython_planet_smoke.py
"""

from __future__ import annotations


def main() -> None:
    # 1) Try to import the extension module explicitly (if it exists).
    try:
        import importlib

        planet_mod = importlib.import_module("solsysgen.planet")
    except Exception as e:
        print("Cython extension not available (this is OK).")
        print("Reason:", repr(e))
        return

    Planet = getattr(planet_mod, "Planet", None)
    if Planet is None:
        print("solsysgen.planet imported but has no Planet symbol.")
        return

    # 2) Try legacy (Cython) signature first: (name, mass, radius)
    try:
        p = Planet("Earth", 5.97, 6371)
        print("Loaded Planet (legacy signature):", p.name, p.mass, p.radius)
        return
    except TypeError:
        pass

    # 3) Fall back to the dataclass signature used by the SI-model
    try:
        p = Planet(
            name="Earth",
            kind="rocky",
            mass_kg=5.972e24,
            radius_m=6.371e6,
            distance_m=1.496e11,
            phase_rad=0.0,
            period_s=365.25 * 86400.0,
            orbital_speed_mps=29780.0,
        )
        print(
            "Loaded Planet (dataclass signature):",
            p.name,
            p.kind,
            p.mass_kg,
            p.radius_m,
        )
        return
    except Exception as e:
        print("Planet exists but could not be instantiated by either known signature.")
        print("Reason:", repr(e))


if __name__ == "__main__":
    main()
