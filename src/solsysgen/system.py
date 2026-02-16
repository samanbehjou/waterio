# solsysgen/system.py
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, Iterator, List, Tuple

from .models import Planet, Sun

"""
AI Assistance Notice

This module was refactored and polished with the assistance of AI-based tools.
All architectural decisions, implementation logic, testing, and final validation
were reviewed and approved by the project author.
"""


@dataclass(slots=True)
class SolarSystem:
    """One Sun + many planets (2D circular orbit model)."""

    sun: Sun
    planets: List[Planet]

    def step(self, dt_s: float) -> None:
        if dt_s < 0:
            raise ValueError("dt_s must be >= 0")
        for p in self.planets:
            p.step(dt_s)

    def state_m(self) -> Dict[str, Tuple[float, float]]:
        return {p.name: p.position_m() for p in self.planets}

    def __len__(self) -> int:
        return len(self.planets)

    def __iter__(self) -> Iterator[Planet]:
        return iter(self.planets)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "sun": self.sun.to_dict(),
            "planets": [p.to_dict() for p in self.planets],
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SolarSystem":
        sun = Sun.from_dict(d["sun"])
        planets = [Planet.from_dict(p) for p in d.get("planets", [])]
        return SolarSystem(sun=sun, planets=planets)

    @staticmethod
    def from_planets(sun: Sun, planets: Iterable[Planet]) -> "SolarSystem":
        return SolarSystem(sun=sun, planets=list(planets))


__all__ = ["SolarSystem"]
