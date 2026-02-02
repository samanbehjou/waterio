from __future__ import annotations

import pytest

from solsysgen import SolarSystem, Sun, generate_planets
from solsysgen.constants import AU_M
from solsysgen.generation import add_custom_planet


def test_generate_planets_count_and_sorted():
    sun = Sun()
    planets = generate_planets(sun, 10, seed=42, inner_au=0.5, outer_au=20.0)

    assert len(planets) == 10
    distances = [p.distance_m for p in planets]
    assert distances == sorted(distances)

    assert all(p.period_s > 0 for p in planets)
    assert all(p.orbital_speed_mps > 0 for p in planets)

    # bounds (allow jitter)
    assert distances[0] > 0.4 * AU_M
    assert distances[-1] < 25.0 * AU_M


def test_generate_planets_rejects_bad_args():
    sun = Sun()

    with pytest.raises(ValueError):
        generate_planets(sun, -1)

    with pytest.raises(ValueError):
        generate_planets(sun, 3, inner_au=-1.0, outer_au=10.0)

    with pytest.raises(ValueError):
        generate_planets(sun, 3, inner_au=10.0, outer_au=1.0)


def test_add_custom_planet_increases_count():
    sun = Sun()
    planets = generate_planets(sun, 3, seed=0, inner_au=0.6, outer_au=5.0)
    system = SolarSystem(sun=sun, planets=planets)

    n0 = len(system.planets)
    add_custom_planet(system, name="X", kind="rocky", distance_au=1.5, phase_deg=0.0)
    assert len(system.planets) == n0 + 1
