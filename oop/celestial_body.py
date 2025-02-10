from calculator import Calculator

class CelestialBody(Calculator):
    def __init__(
        self,
        name,
        diameter=None,
        circumference=None,
        distance=None,
        orbital_period=None,
    ):
        self.name = name
        self.diameter = diameter
        self.circumference = circumference
        self.distance = distance
        self.orbital_period = orbital_period

    def calculate_diameter(self):
        if not self.diameter and self.circumference:
            self.diameter = super().calculate_diameter(self.circumference)
        return self.diameter

    def calculate_circumference(self):
        if not self.circumference and self.diameter:
            self.circumference = super().calculate_circumference(self.diameter)
        return self.circumference

    def calculate_orbital_period(self):
        if not self.orbital_period and self.distance:
            self.orbital_period = super().calculate_orbital_period(self.distance)
        return self.orbital_period

    def calculate_distance(self):
        if not self.distance and self.orbital_period:
            self.distance = super().calculate_distance(self.orbital_period)
        return self.distance

    def calculate_volume(self):
        return super().calculate_volume(self.diameter)
