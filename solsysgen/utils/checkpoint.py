import numpy as np
from pathlib import Path

def save_checkpoint(path: str | Path, data: dict) -> None:
    """Save dictionary of arrays/scalars to a .npz file."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(path, **data)

def load_checkpoint(path: str | Path) -> dict:
    """Load dictionary from a .npz file."""
    with np.load(path, allow_pickle=False) as f:
        return {k: f[k] for k in f.files}
