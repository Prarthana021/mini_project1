from celestial_body import CelestialBody

class Sun(CelestialBody):
    def __init__(self, name, diameter=None, circumference=None):
        super().__init__(name, diameter, circumference)
    def calculate_diameter(self):
        return super().calculate_diameter() if self.circumference else None
    
    def calculate_circumference(self):
        return super().calculate_circumference() if self.diameter else None
    
    def calculate_volume(self):
        return super().calculate_volume() if self.diameter  or self.circumference else None

