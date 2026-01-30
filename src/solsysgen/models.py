from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any, Dict, Literal, Tuple

PlanetType = Literal["rocky", "gas_giant", "ice_giant", "dwarf"]


@dataclass(frozen=True, slots=True)
class Sun:
    """
    Physical attributes are in SI:
    - mass_kg: kilograms
    - radius_m: meters
    - luminosity_w: watts
    """

    name: str = "Sun"
    mass_kg: float = 1.9885e30
    radius_m: float = 6.9634e8
    luminosity_w: float = 3.828e26

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "mass_kg": self.mass_kg,
            "radius_m": self.radius_m,
            "luminosity_w": self.luminosity_w,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Sun":
        return Sun(
            name=d.get("name", "Sun"),
            mass_kg=float(d["mass_kg"]),
            radius_m=float(d["radius_m"]),
            luminosity_w=float(d.get("luminosity_w", 0.0)),
        )


@dataclass(slots=True)
class Planet:
    """
    Circular 2D orbit around the Sun (heliocentric).
    SI units:
    - mass_kg, radius_m
    - distance_m: orbital radius
    - phase_rad: orbital angle
    - period_s: derived by Kepler
    - orbital_speed_mps: derived
    """

    name: str
    kind: PlanetType

    mass_kg: float
    radius_m: float

    distance_m: float
    phase_rad: float

    period_s: float
    orbital_speed_mps: float

    def position_m(self) -> Tuple[float, float]:
        return (
            self.distance_m * math.cos(self.phase_rad),
            self.distance_m * math.sin(self.phase_rad),
        )

    def angular_speed_rad_s(self) -> float:
        if self.period_s <= 0:
            raise ValueError("period_s must be > 0")
        return (2.0 * math.pi) / self.period_s

    def step(self, dt_s: float) -> None:
        if dt_s < 0:
            raise ValueError("dt_s must be >= 0")
        self.phase_rad = (self.phase_rad + self.angular_speed_rad_s() * dt_s) % (
            2.0 * math.pi
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "kind": self.kind,
            "mass_kg": self.mass_kg,
            "radius_m": self.radius_m,
            "distance_m": self.distance_m,
            "phase_rad": self.phase_rad,
            "period_s": self.period_s,
            "orbital_speed_mps": self.orbital_speed_mps,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Planet":
        return Planet(
            name=str(d["name"]),
            kind=d["kind"],
            mass_kg=float(d["mass_kg"]),
            radius_m=float(d["radius_m"]),
            distance_m=float(d["distance_m"]),
            phase_rad=float(d.get("phase_rad", 0.0)),
            period_s=float(d["period_s"]),
            orbital_speed_mps=float(d["orbital_speed_mps"]),
        )


__all__ = ["Sun", "Planet", "PlanetType"]
