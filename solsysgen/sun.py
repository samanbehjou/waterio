class Sun:
    """
    Represents a star (default: our Sun).

    Parameters
    ----------
    name : str
        Star name
    mass : float
        Mass in kg
    radius : float
        Radius in meters
    luminosity : float
        Luminosity in watts
    """

    def __init__(
        self,
        name: str = "Sun",
        mass: float = 1.98847e30,         # kg
        radius: float = 6.9634e8,         # meters
        luminosity: float = 3.828e26      # watts
    ):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.luminosity = luminosity

    def surface_gravity(self) -> float:
        """Return surface gravity in m/s^2"""
        G = 6.67430e-11
        return G * self.mass / self.radius**2

