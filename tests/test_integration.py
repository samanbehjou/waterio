from __future__ import annotations

from solsysgen import SolarSystem, Sun, generate_planets
from solsysgen.constants import DAY_S


def test_generate_and_step_system():
    sun = Sun()
    planets = generate_planets(sun, 5, seed=1)
    system = SolarSystem(sun=sun, planets=planets)

    before = [p.phase_rad for p in system.planets]
    system.step(DAY_S)
    after = [p.phase_rad for p in system.planets]

    assert before != after
