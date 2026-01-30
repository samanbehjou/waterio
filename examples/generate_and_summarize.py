"""
Generate a solar system and print a compact summary table.

Run:
  python3 examples/generate_and_summarize.py
"""

from __future__ import annotations

from solsysgen import SolarSystem, Sun, generate_planets
from solsysgen.constants import AU_M, DAY_S, YEAR_S


def main() -> None:
    sun = Sun()
    planets = generate_planets(sun, 8, seed=7, inner_au=0.4, outer_au=35.0)
    system = SolarSystem(sun=sun, planets=planets)

    print(f"Star: {system.sun.name}")
    print("-" * 86)
    print(
        f"{'name':10} {'kind':10} {'a (AU)':>10} {'T (days)':>10} {'T (years)':>10} {'v (km/s)':>10}"
    )
    print("-" * 86)

    for p in system.planets:
        a_au = p.distance_m / AU_M
        t_days = p.period_s / DAY_S
        t_years = p.period_s / YEAR_S
        v_kms = p.orbital_speed_mps / 1000.0
        print(
            f"{p.name:10} {p.kind:10} {a_au:10.2f} {t_days:10.1f} {t_years:10.2f} {v_kms:10.2f}"
        )

    print("-" * 86)


if __name__ == "__main__":
    main()
