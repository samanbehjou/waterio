import numpy as np


class Sun:
    """
    Represents a star in the solar system.

    Attributes
    ----------
    mass : float
        Star mass in solar mass units.
    radius : float
        Star radius in solar radius units.
    luminosity : float
        Star luminosity in solar luminosity units.
    name : str
        Name of the star.
    """

    def __init__(self, mass=1.0, radius=1.0, luminosity=1.0, name="Sun"):
        """Initialize a new Sun instance."""
        self.mass = mass
        self.radius = radius
        self.luminosity = luminosity
        self.name = name
        self.position = np.array([0.0, 0.0])

    def __str__(self):
        """Return a readable summary of the star."""
        return (
            f"Star {self.name}: mass={self.mass:.2f} M☉, "
            f"radius={self.radius:.2f} R☉, "
            f"luminosity={self.luminosity:.2f} L☉"
        )
