from solsysgen import Sun, Planet, SolarSystem

# Create the star (default values for Sun: mass, radius, luminosity)
star = Sun()

# Create planets with (name, mass [kg], orbital radius a [m], planet radius [m])
earth = Planet(
    name="Earth",
    mass=5.972e24,
    a=1.496e11,
    radius=6.371e6
)

mars = Planet(
    name="Mars",
    mass=6.39e23,
    a=2.279e11,
    radius=3.3895e6
)

# Create the solar system with the star and planets
ss = SolarSystem(star, [earth, mars])

# Print a summary (star properties + planet properties)
print(ss.summary())
