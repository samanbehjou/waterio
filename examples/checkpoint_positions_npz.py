"""
Save a checkpoint of planet positions over time using waterio.

Run:
  python3 examples/checkpoint_positions_npz.py
"""

from __future__ import annotations

import numpy as np

from solsysgen import SolarSystem, Sun, generate_planets
from solsysgen.constants import DAY_S
from waterio import load_checkpoint, save_checkpoint


def main() -> None:
    sun = Sun()
    planets = generate_planets(sun, 4, seed=3, inner_au=0.7, outer_au=6.0)
    system = SolarSystem(sun=sun, planets=planets)

    steps = 20
    dt = 5 * DAY_S

    # positions[t, i, xy]
    pos = np.zeros((steps, len(planets), 2), dtype=np.float64)

    for t in range(steps):
        for i, p in enumerate(system.planets):
            pos[t, i, :] = np.array(p.position_m(), dtype=np.float64)
        system.step(dt)

    save_checkpoint("examples/positions_ckpt.npz", positions=pos)

    out = load_checkpoint("examples/positions_ckpt.npz")
    print("Saved positions:", out["positions"].shape)
    print("Example first planet first frame:", out["positions"][0, 0])


if __name__ == "__main__":
    main()
