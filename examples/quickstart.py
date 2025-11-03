from solsysgen import Sun, Planet, SolarSystem

star = Sun()
earth = Planet("Earth", mass=5.972e24, a=1.496e11)
mars = Planet("Mars", mass=6.39e23, a=2.279e11)

ss = SolarSystem(star, [earth, mars])
print(ss.summary())
