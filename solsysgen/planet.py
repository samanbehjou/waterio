class Planet:
    """Planet with name, mass (kg), semi-major axis a (m)."""
    def __init__(self, name: str, mass: float, a: float):
        self.name = name
        self.mass = mass
        self.a = a

    def orbital_period(self, mu: float) -> float:
        """Kepler's 3rd law (simplified); mu = G * M_sun. Returns seconds."""
        from math import pi, sqrt
        return 2 * pi * sqrt(self.a**3 / mu)
