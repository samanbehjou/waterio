from Cython.Build import cythonize
from setuptools import Extension, setup

ext_modules = [
    Extension(
        name="planet",  # Name of the Cython extension
        sources=["src/solsysgen/planet.pyx"],  # Path to planet.pyx file
    )
]

setup(
    name="YourPackageName",
    ext_modules=cythonize(ext_modules),
)
