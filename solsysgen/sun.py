class Sun:
    """Simple star with a name and mass (kg)."""
    def __init__(self, name: str = "Sun", mass: float = 1.98847e30):
        self.name = name
        self.mass = mass

    def luminosity(self) -> float:
        # toy placeholder
        return self.mass * 3.8e-27
