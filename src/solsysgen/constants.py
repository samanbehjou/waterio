# solsysgen/constants.py
from __future__ import annotations

import math

# Physical constants
G = 6.67430e-11  # m^3 kg^-1 s^-2

# Convenience units
AU_M = 1.495978707e11  # meters
DAY_S = 86_400.0
YEAR_S = 365.25 * DAY_S

TAU = 2.0 * math.pi

__all__ = ["G", "AU_M", "DAY_S", "YEAR_S", "TAU"]
