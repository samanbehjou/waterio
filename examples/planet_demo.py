import planet  # This should import the compiled Cython extension

# Create an instance of the Planet class
p = planet.Planet("Earth", 5.97, 6371)

# Print the attributes of the planet instance
print(p.name, p.mass, p.radius)
