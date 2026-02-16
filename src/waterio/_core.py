"""
Python-facing API for the compiled extension.

This module wraps :mod:`waterio._core` to provide a stable import path and
room for Python-side validation, docs, and future extensions.
"""

from __future__ import annotations

from dataclasses import dataclass

"""
AI Assistance Notice

This module was refactored and polished with the assistance of AI-based tools.
All architectural decisions, implementation logic, testing, and final validation
were reviewed and approved by the project author.
"""


@dataclass
class Counter:
    """A simple integer counter.

    Parameters
    ----------
    start:
        Initial counter value.
    """

    start: int

    def __post_init__(self) -> None:
        self._impl = _core.Counter(self.start)

    def inc(self) -> int:
        """Increment and return the new counter value."""
        return self._impl.inc()
