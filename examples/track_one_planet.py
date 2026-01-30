"""
Track a single planet's (x,y) position over time.

Run:
  python3 examples/track_one_planet.py
"""

from __future__ import annotations

import math

from solsysgen import SolarSystem, Sun, generate_planets
from solsysgen.constants import DAY_S


def main() -> None:
    sun = Sun()
    planets = generate_planets(sun, 6, seed=2, inner_au=0.5, outer_au=15.0)
    system = SolarSystem(sun=sun, planets=planets)

    # Pick a mid-distance planet (more interesting than the innermost)
    target = system.planets[len(system.planets) // 2]
    print("Target:", target.name, f"kind={target.kind}", f"a={target.distance_m:.3e} m")

    steps = 12
    dt = 10 * DAY_S  # 10 days per step

    print("\nstep   t_days      x_m            y_m         r_m")
    t = 0.0
    for i in range(steps + 1):
        x, y = target.position_m()
        r = math.hypot(x, y)
        print(f"{i:>4} {t/DAY_S:>8.1f} {x:>13.3e} {y:>13.3e} {r:>11.3e}")
        system.step(dt)
        t += dt


if __name__ == "__main__":
    main()
