from __future__ import annotations

import pytest

from solsysgen.models import Planet


def test_planet_basic_fields():
    p = Planet(
        name="Earth",
        kind="rocky",
        mass_kg=5.972e24,
        radius_m=6.371e6,
        distance_m=1.0e11,
        phase_rad=0.0,
        period_s=3.154e7,
        orbital_speed_mps=3.0e4,
    )
    assert p.name == "Earth"
    assert p.kind == "rocky"
    assert p.mass_kg > 0
    assert p.radius_m > 0


def test_planet_position_returns_tuple():
    p = Planet(
        name="X",
        kind="dwarf",
        mass_kg=1.0,
        radius_m=1.0,
        distance_m=10.0,
        phase_rad=0.0,
        period_s=100.0,
        orbital_speed_mps=0.0,
    )
    x, y = p.position_m()
    assert isinstance(x, float)
    assert isinstance(y, float)


def test_planet_angular_speed_requires_positive_period():
    p = Planet(
        name="X",
        kind="dwarf",
        mass_kg=1.0,
        radius_m=1.0,
        distance_m=10.0,
        phase_rad=0.0,
        period_s=0.0,
        orbital_speed_mps=0.0,
    )
    with pytest.raises(ValueError):
        p.angular_speed_rad_s()
