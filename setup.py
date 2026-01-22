from __future__ import annotations

from setuptools import Extension, setup

try:
    from Cython.Build import cythonize
except ImportError:
    cythonize = None

import numpy as np

extensions = [
    Extension(
        name="waterio._fast",
        sources=["src/waterio/_fast.pyx"],
        include_dirs=[np.get_include()],
        language="c++",  # use "c" if your .pyx is pure C
    )
]

if cythonize is None:
    raise RuntimeError(
        "Cython is required to build the extension (install build deps)."
    )

setup(
    ext_modules=cythonize(
        extensions,
        compiler_directives={"language_level": "3"},
    ),
)
