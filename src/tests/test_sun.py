from solsysgen.sun import Sun

def test_sun_init():
    sun = Sun(mass=1.1, radius=1.2, luminosity=1.3)
    assert sun.mass == 1.1
    assert sun.radius == 1.2
    assert sun.luminosity == 1.3
    assert sun.name == "Sun"

def test_sun_str():
    sun = Sun()
    s = str(sun)
    assert "Star Sun:" in s
