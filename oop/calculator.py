import math

class Calculator:
    def calculate_diameter(self, circumference):
        return round(circumference / math.pi, 2) if circumference else None

    def calculate_circumference(self, diameter):
        return round(diameter * math.pi, 2) if diameter else None

    def calculate_orbital_period(self, distance):
        return round(distance**1.5, 2) if distance else None

    def calculate_distance(self, orbital_period):
        return round(orbital_period ** (2 / 3), 2) if orbital_period else None

    def calculate_volume(self, diameter):
        return round((4 / 3) * math.pi * (diameter / 2) ** 3, 2) if diameter else 0

    def format_number(self, value):
        return f"{value:,}" if value is not None else "Unknown"
