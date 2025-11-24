from solsysgen.sun import Sun
from solsysgen.planet import Planet
from solsysgen.solar_system import SolarSystem


def test_solar_system():
    sun = Sun()
    earth = Planet(name="Earth", distance=1.0, velocity=1.0)
    system = SolarSystem(sun)
    system.add_planet(earth)
    system.update(dt=0.1)
    assert len(system.planets) == 1
    assert system.planets[0].name == "Earth"

