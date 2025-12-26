.. Solar System Generator documentation master file, created by
   sphinx-quickstart on Fri Dec 26 15:39:30 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Solar System Generator documentation
=====================================

This project implements a Python code to generate a simple solar system model
with a heliocentric model and circular orbits in 2D.

Installation
------------
To install the package, run:

.. code-block:: bash
   python3 -m pip install .

Usage
------
Create a solar system and add planets:

.. code-block:: python
   from solarsystem import SolarSystem, Sun, Planet

   # Create the Sun
   sun = Sun(mass=1.0, radius=1.0, luminosity=1.0)

   # Create the Solar System
   solar_system = SolarSystem(sun)

   # Add a planet
   earth = Planet(name="Earth", mass=1.0, radius=1.0, distance=1.0, velocity=0.01)
   solar_system.add_planet(earth)

   # Update positions of planets
   solar_system.update(dt=0.01)

Features
--------
- Sun with mass, radius, and luminosity.
- Planets with mass, radius, orbital parameters.
- Simple 2D orbital simulation.
- Optional visualization.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   usage
   features
   installation

