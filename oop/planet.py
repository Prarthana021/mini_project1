from celestial_body import CelestialBody
class Planet(CelestialBody):
    def __init__(
        self,
        name,
        diameter=None,
        circumference=None,
        distance=None,
        orbital_period=None,
    ):
        super().__init__(name, diameter, circumference, distance, orbital_period)
