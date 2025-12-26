import numpy as np


class Planet:
    """
    Represents a planet in the solar system.

    Attributes
    ----------
    name : str
        Name of the planet.
    mass : float
        Planet mass in Earth mass units.
    radius : float
        Planet radius in Earth radius units.
    distance : float
        Orbital radius (AU).
    velocity : float
        Orbital speed (AU/year or arbitrary units).
    position : np.ndarray
        2D position vector in AU.
    """

    def __init__(
        self,
        name="Planet",
        mass=1.0,
        radius=1.0,
        distance=1.0,
        velocity=1.0,
        angle=0.0,
    ):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.distance = distance
        self.velocity = velocity
        self.angle = angle  # orbital phase angle in radians

        # Initial position in 2D (x, y)
        self.position = np.array([distance * np.cos(angle), distance * np.sin(angle)])

    def update_position(self, dt=0.01):
        """
        Update the orbital angle and compute new 2D position.

        Parameters
        ----------
        dt : float
            Time step for orbit integration.
        """
        self.angle += self.velocity * dt
        self.position = np.array(
            [
                self.distance * np.cos(self.angle),
                self.distance * np.sin(self.angle),
            ]
        )

    def __str__(self) -> str:
        return (
            f"Planet {self.name}: "
            f"mass={self.mass:.2f} M⊕, "
            f"radius={self.radius:.2f} R⊕, "
            f"distance={self.distance} AU"
        )

    def orbital_period_kepler(self, mu: float) -> float:
        """
        Compute orbital period from Kepler's third law for a circular orbit.

        Parameters
        ----------
        mu : float
            Standard gravitational parameter G * M_sun in consistent units.

        Returns
        -------
        float
            Orbital period.
        """
        # distance is the semi-major axis a
        if self.distance <= 0:
            raise ValueError("distance must be positive")
        from math import pi, sqrt

        a = self.distance
        return 2 * pi * sqrt(a**3 / mu)
