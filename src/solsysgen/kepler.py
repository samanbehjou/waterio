# solsysgen/kepler.py
from __future__ import annotations

import math

from .constants import TAU, G


# Feedback: it would be good to document in the docstrings
# the parameters used by these routines:
# distance_m: the distance from the planet to the sun in m
# central_mass_kg: the mass of the sun in kg
# etc.
def period_s(distance_m: float, central_mass_kg: float) -> float:
    """
    Kepler's 3rd law (two-body approx, circular orbit):
        T = 2π * sqrt(r^3 / (G*M))
    """
    if distance_m <= 0:
        raise ValueError("distance_m must be > 0")
    if central_mass_kg <= 0:
        raise ValueError("central_mass_kg must be > 0")
    return TAU * math.sqrt((distance_m**3) / (G * central_mass_kg))


def circular_speed_mps(distance_m: float, central_mass_kg: float) -> float:
    """
    Circular orbit speed:
        v = sqrt(G*M / r)
    """
    if distance_m <= 0:
        raise ValueError("distance_m must be > 0")
    if central_mass_kg <= 0:
        raise ValueError("central_mass_kg must be > 0")
    return math.sqrt((G * central_mass_kg) / distance_m)
