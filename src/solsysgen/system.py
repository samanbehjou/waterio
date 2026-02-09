# solsysgen/system.py
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, Iterator, List, Tuple

import numpy as np
from matplotlib import pyplot as plt

from .constants import AU_M, DAY_S
from .models import Planet, Sun


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

    # Feedback: routine from notebook
    def propagate(self, no_steps=100, step_size=5):
        """ Propagate the planets for a specific amount of time.

            no_steps: number of steps.
            step_size: time step in days.

            returns a NumPy array with the planet coordinates at each step.
        """

        traj = np.zeros((no_steps + 1, len(self.planets), 2), dtype=np.float64)

        dt = step_size * DAY_S

        # Record t=0 first, then step
        for t in range(no_steps + 1):
            for i, p in enumerate(self.planets):
                traj[t, i, :] = p.position_m()
                if t < no_steps:
                    self.step(dt)

        return traj

    def plot(self, no_steps=100, step_size=5):
        """ Plot the trajectory of the planets after propagating.

            no_steps: number of steps.
            step_size: time step in days.
        """
        traj = self.propagate(no_steps, step_size)

        plt.figure()
        for i, p in enumerate(self.planets):
            plt.plot(traj[:, i, 0] / AU_M, traj[:, i, 1] / AU_M, label=p.name)

        dt = step_size * DAY_S
        plt.scatter([0], [0], marker="*", s=120)  # Sun at origin
        plt.xlabel("x (AU)")
        plt.ylabel("y (AU)")
        plt.title(f"Orbit trajectories (2D circular model) — steps={no_steps}, dt={dt/DAY_S:.0f} days")
        plt.axis("equal")
        plt.legend(loc="upper right", fontsize=8)
        plt.show()


__all__ = ["SolarSystem"]
