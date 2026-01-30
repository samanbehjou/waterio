# solsysgen/iodata.py
from __future__ import annotations

from pathlib import Path
from typing import Dict

import numpy as np


def save_checkpoint(path: str | Path, **arrays: np.ndarray) -> None:
    """Save one or more NumPy arrays to a compressed NPZ checkpoint."""
    path = Path(path)
    if not arrays:
        raise ValueError("Provide at least one array as a keyword argument.")
    for k, v in arrays.items():
        if not isinstance(v, np.ndarray):
            raise TypeError(f"'{k}' must be a numpy.ndarray, got {type(v)}")
    np.savez_compressed(path, **arrays)


def load_checkpoint(path: str | Path) -> Dict[str, np.ndarray]:
    """Load arrays from a compressed NPZ checkpoint created by save_checkpoint()."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)
    with np.load(path, allow_pickle=False) as data:
        return {key: data[key] for key in data.files}
