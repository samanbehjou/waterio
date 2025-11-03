class Planet:
    """
    Represents a planet orbiting a star.

    Parameters
    ----------
    name : str
        Planet name
    mass : float
        Mass in kg
    a : float
        Semi-major axis (orbital radius) in meters
    radius : float
        Planet radius in meters
    """

    def __init__(self, name: str, mass: float, a: float, radius: float):
        self.name = name
        self.mass = mass
        self.a = a          # orbital radius
        self.radius = radius

    def orbital_period(self, mu: float) -> float:
        """Kepler's 3rd law (simplified); mu = G * M_sun. Returns seconds."""
        from math import pi, sqrt
        return 2 * pi * sqrt(self.a**3 / mu)

