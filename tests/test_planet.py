import numpy as np

from solsysgen.planet import Planet


def test_planet_attributes() -> None:
    """
    Test that basic Planet attributes are stored correctly.

    Verifies that the `name` attribute is correctly assigned
    during initialization.
    """
    p: Planet = Planet(name="Earth", mass=5.97, radius=6371)
    assert p.name == "Earth"


def test_planet_init() -> None:
    """
    Test full Planet initialization.

    Ensures that all constructor parameters are assigned correctly
    and that the initial orbital position is computed as expected.
    """
    planet: Planet = Planet(
        name="Earth",
        mass=1.0,
        radius=1.0,
        distance=1.0,
        velocity=1.0,
        angle=0.0,
    )

    assert planet.name == "Earth"
    assert planet.mass == 1.0
    assert np.allclose(planet.position, [1.0, 0.0])


def test_update_position() -> None:
    """
    Test that updating the planet position changes its coordinates.

    The planet's position after a time step should differ
    from its initial position.
    """
    planet: Planet = Planet()
    old_pos: np.ndarray = planet.position.copy()

    planet.update_position(dt=1.0)

    assert not np.allclose(planet.position, old_pos)
