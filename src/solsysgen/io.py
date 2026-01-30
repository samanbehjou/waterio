# solsysgen/io.py
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from .system import SolarSystem


def to_json(system: SolarSystem, *, indent: int = 2) -> str:
    return json.dumps(system.to_dict(), indent=indent)


def save_json(path: str | Path, system: SolarSystem, *, indent: int = 2) -> None:
    path = Path(path)
    path.write_text(to_json(system, indent=indent), encoding="utf-8")


def load_json(path: str | Path) -> SolarSystem:
    path = Path(path)
    data: Dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    return SolarSystem.from_dict(data)
