from solsysgen.planet import Planet
import numpy as np

def test_planet_init():
    planet = Planet(name="Earth", mass=1, radius=1, distance=1, velocity=1, angle=0)
    assert planet.name == "Earth"
    assert planet.mass == 1
    assert np.allclose(planet.position, [1, 0])

def test_update_position():
    planet = Planet()
    old_pos = planet.position.copy()
    planet.update_position(dt=1.0)
    assert not np.allclose(planet.position, old_pos)

