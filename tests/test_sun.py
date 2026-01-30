from __future__ import annotations

from solsysgen.models import Sun


def test_sun_defaults():
    s = Sun()
    assert s.name == "Sun"
    assert s.mass_kg > 0
    assert s.radius_m > 0
    assert s.luminosity_w >= 0


def test_sun_custom_values():
    s = Sun(name="Star", mass_kg=2.0, radius_m=3.0, luminosity_w=4.0)
    assert s.name == "Star"
    assert s.mass_kg == 2.0
    assert s.radius_m == 3.0
    assert s.luminosity_w == 4.0
