"""
Tests for the waterio checkpoint save/load functionality.

These tests verify that NumPy arrays can be written to disk and
read back correctly using the public waterio API.
"""

from pathlib import Path
from typing import Dict

import numpy as np
import pytest
from numpy.typing import NDArray

from waterio import load_checkpoint, save_checkpoint


def test_save_creates_file(tmp_path: Path) -> None:
    """
    Test that saving a checkpoint creates a file on disk.

    Parameters
    ----------
    tmp_path : Path
        Temporary directory provided by pytest.
    """
    p: Path = tmp_path / "ckpt.npz"
    save_checkpoint(p, a=np.arange(5))
    assert p.exists()


def test_load_returns_expected_arrays(tmp_path: Path) -> None:
    """
    Test that saved arrays are loaded with correct keys and shapes.

    Parameters
    ----------
    tmp_path : Path
        Temporary directory provided by pytest.
    """
    p: Path = tmp_path / "ckpt.npz"
    a: NDArray[np.int_] = np.arange(5)
    b: NDArray[np.float_] = np.ones((2, 3))

    save_checkpoint(p, a=a, b=b)
    data: Dict[str, NDArray] = load_checkpoint(p)

    assert set(data.keys()) == {"a", "b"}
    assert np.array_equal(data["a"], a)
    assert data["b"].shape == (2, 3)


def test_roundtrip_multiple_types_integration(tmp_path: Path) -> None:
    """
    Integration test: verify round-trip integrity for multiple dtypes.

    Parameters
    ----------
    tmp_path : Path
        Temporary directory provided by pytest.
    """
    p: Path = tmp_path / "ckpt.npz"
    rng: np.random.Generator = np.random.default_rng(0)

    x: NDArray[np.float32] = rng.normal(size=(10, 4)).astype(np.float32)
    y: NDArray[np.int64] = np.array([1, 2, 3], dtype=np.int64)

    save_checkpoint(p, x=x, y=y)
    out: Dict[str, NDArray] = load_checkpoint(p)

    assert out["x"].dtype == np.float32
    assert np.allclose(out["x"], x)
    assert np.array_equal(out["y"], y)
