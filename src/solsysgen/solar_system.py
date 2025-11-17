import numpy as np

from .sun import Sun
from .planet import Planet


class SolarSystem:
    """
    Represents a simple 2D heliocentric solar system.

    Attributes
    ----------
    sun : Sun
        The central star.
    planets : list[Planet]
        List of planet objects orbiting the star.
    """

    def __init__(self, sun: Sun):
        """Initialize a SolarSystem with one central star."""
        self.sun = sun
        self.planets: list[Planet] = []

    def add_planet(self, planet: Planet):
        """Add a planet to the solar system."""
        self.planets.append(planet)

    def update(self, dt: float = 0.01):
        """
        Update the positions of all planets.

        Parameters
        ----------
        dt : float
            Time step for orbital motion.
        """
        for planet in self.planets:
            planet.update_position(dt)

    def __str__(self):
        """Return a readable summary of the solar system."""
        s = f"Solar System with star: {self.sun.name}\n"
        s += "Planets:\n"
        for p in self.planets:
            s += f"  - {p.name} at {p.position}\n"
        return s
