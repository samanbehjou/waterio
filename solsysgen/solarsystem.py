from typing import List
from .sun import Sun
from .planet import Planet

G = 6.67430e-11  # m^3 kg^-1 s^-2


class SolarSystem:
    def __init__(self, star: Sun, planets: List[Planet] | None = None):
        self.star = star
        self.planets = planets or []

    @property
    def mu(self) -> float:
        """Standard gravitational parameter μ = G * M_star."""
        return G * self.star.mass

    def add_planet(self, planet: Planet) -> None:
        self.planets.append(planet)

    def summary(self) -> str:
        # Star line now includes mass, radius, luminosity
        lines = [
            (
                f"Star: {self.star.name} "
                f"(mass={self.star.mass:.3e} kg, radius={self.star.radius:.2e} m, "
                f"luminosity={self.star.luminosity:.2e} W)"
            )
        ]
        # Each planet line includes a, radius, and orbital period in days
        for p in self.planets:
            T = p.orbital_period(self.mu)
            lines.append(
                f"- {p.name}: a={p.a:.3e} m, radius={p.radius:.2e} m, T={T/86400:.2f} days"
            )
        return "\n".join(lines)

