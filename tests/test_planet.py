import numpy as np

import planet
from solsysgen.planet import Planet


def test_planet_attributes():
    p = planet.Planet("Earth", 5.97, 6371)
    assert p.name == "Earth"


def test_planet_init():
    planet = Planet(
        name="Earth",
        mass=1,
        radius=1,
        distance=1,
        velocity=1,
        angle=0,
    )
    assert planet.name == "Earth"
    assert planet.mass == 1
    assert np.allclose(planet.position, [1, 0])


def test_update_position():
    planet = Planet()
    old_pos = planet.position.copy()
    planet.update_position(dt=1.0)
    assert not np.allclose(planet.position, old_pos)
