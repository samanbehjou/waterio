# solsysgen/generation.py
from __future__ import annotations

import math
import random
from typing import List, Optional

# Feedback: DAY_S was unused
from .constants import AU_M
from .kepler import circular_speed_mps, period_s

# Feedback: Planet appears twice!
from .models import Planet, PlanetType, Sun

"""
AI Assistance Notice

This module was refactored and polished with the assistance of AI-based tools.
All architectural decisions, implementation logic, testing, and final validation
were reviewed and approved by the project author.
"""


def _snowline_au(luminosity_w: float) -> float:
    """
    Rough snowline estimate:
      ~ 2.7 AU * sqrt(L/Lsun)
    Using Lsun = 3.828e26 W.
    """
    Lsun = 3.828e26
    return 2.7 * math.sqrt(max(luminosity_w, 0.0) / Lsun)


def _pick_kind(distance_au: float, snowline_au: float) -> PlanetType:
    # Simple, believable rule:
    if distance_au < snowline_au * 0.8:
        return "rocky"
    if distance_au < snowline_au * 2.5:
        return "gas_giant"
    if distance_au < snowline_au * 8.0:
        return "ice_giant"
    return "dwarf"


def generate_planets(
    sun: Sun,
    n_planets: int,
    *,
    seed: Optional[int] = None,
    inner_au: float = 0.4,
    outer_au: float = 40.0,
) -> List[Planet]:
    """
    Generate planets with roughly log-spaced orbital radii and simple type rules.
    """
    if n_planets < 0:
        raise ValueError("n_planets must be >= 0")
    if inner_au <= 0 or outer_au <= 0 or outer_au <= inner_au:
        raise ValueError("inner_au and outer_au must be > 0 and outer_au > inner_au")

    rng = random.Random(seed)
    if n_planets == 0:
        return []

    snow = _snowline_au(sun.luminosity_w)

    # Log spacing for natural-looking orbits
    log_inner = math.log(inner_au)
    log_outer = math.log(outer_au)

    planets: List[Planet] = []
    for i in range(n_planets):
        t = i / max(1, n_planets - 1)
        base_au = math.exp(log_inner + t * (log_outer - log_inner))
        jitter = rng.uniform(0.92, 1.08)
        distance_au = base_au * jitter
        distance_m = distance_au * AU_M

        kind = _pick_kind(distance_au, snow)

        # Rough physical heuristics (SI):
        if kind == "rocky":
            mass_kg = rng.uniform(0.05, 5.0) * 5.972e24
            radius_m = rng.uniform(0.3, 1.6) * 6.371e6
        elif kind == "gas_giant":
            mass_kg = rng.uniform(0.1, 3.0) * 1.898e27
            radius_m = rng.uniform(0.7, 1.3) * 6.9911e7
        elif kind == "ice_giant":
            mass_kg = rng.uniform(0.5, 2.0) * 8.681e25
            radius_m = rng.uniform(0.7, 1.2) * 2.5362e7
        else:
            mass_kg = rng.uniform(0.0001, 0.01) * 5.972e24
            radius_m = rng.uniform(0.05, 0.3) * 6.371e6

        T = period_s(distance_m, sun.mass_kg)
        v = circular_speed_mps(distance_m, sun.mass_kg)
        phase = rng.uniform(0.0, 2.0 * math.pi)

        planets.append(
            Planet(
                name=f"Planet {i+1}",
                kind=kind,
                mass_kg=mass_kg,
                radius_m=radius_m,
                distance_m=distance_m,
                phase_rad=phase,
                period_s=T,
                orbital_speed_mps=v,
            )
        )

    planets.sort(key=lambda p: p.distance_m)
    return planets


def add_custom_planet(
    system,
    *,
    name: str,
    kind: PlanetType,
    distance_au: float,
    phase_deg: float = 0.0,
    mass_kg: float = 5.972e24,  # default ~ Earth mass
    radius_m: float = 6.371e6,  # default ~ Earth radius
    allow_overlap: bool = False,
) -> None:
    """
    Add a single user-defined planet to an existing SolarSystem.

    Constraints:
    - 2D circular orbit
    - distance_au must be > 0
    - phase_deg is wrapped into [0, 360)
    - period and orbital speed are derived from Kepler using the system Sun mass
    """

    if distance_au <= 0:
        raise ValueError("distance_au must be > 0")

    distance_m = distance_au * AU_M

    # Optional: avoid identical orbital radius
    if not allow_overlap:
        existing_m = [p.distance_m for p in system.planets]
        if any(abs(distance_m - d) < 1e-3 for d in existing_m):
            raise ValueError("A planet with the same orbital distance already exists.")

    # Wrap phase into [0, 360)
    phase_rad = math.radians(phase_deg % 360.0)

    # Kepler-derived values
    T = period_s(distance_m, system.sun.mass_kg)
    v = circular_speed_mps(distance_m, system.sun.mass_kg)

    # Create and append
    p = Planet(
        name=name,
        kind=kind,
        mass_kg=mass_kg,
        radius_m=radius_m,
        distance_m=distance_m,
        phase_rad=phase_rad,
        period_s=T,
        orbital_speed_mps=v,
    )

    system.planets.append(p)
    system.planets.sort(key=lambda pl: pl.distance_m)
