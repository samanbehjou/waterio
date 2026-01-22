# cython: language_level=3

cdef class Planet:
    cdef public str name
    cdef public double mass
    cdef public double radius

    def __init__(self, name, mass, radius):
        self.name = str(name)
        self.mass = float(mass)
        self.radius = float(radius)
        # Optional: remove this print if you don’t want noisy output
        # print(f"Initialized Planet: {self.name}, {self.mass}, {self.radius}")

    def get_name(self):
        print(f"Accessing name: {self.name}")
        return self.name

    def get_mass(self):
        print(f"Accessing mass: {self.mass}")
        return self.mass

    def get_radius(self):
        print(f"Accessing radius: {self.radius}")
        return self.radius

