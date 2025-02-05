import json
import math

def calculate_diameter_from_circumference(circumference):
    return round(circumference / math.pi, 2) if circumference else None

def calculate_circumference_from_diameter(diameter):
    return round(diameter * math.pi, 2) if diameter else None

def calculate_orbital_period(distance):
    return round(distance ** 1.5, 2) if distance else None

def calculate_distance_from_orbital_period(orbital_period):
    return round(orbital_period ** (2/3), 2) if orbital_period else None

def calculate_volume(diameter):
    return round((4/3) * math.pi * (diameter / 2) ** 3, 2) if diameter else 0

def format_number(value):
    return f"{value:,}" if value is not None else "Unknown"

def process_solar_system(data):
    print(f"Sun: {data['Name']}")
    sun_diameter = data.get("Diameter")
    sun_circumference = data.get("Circumference")
    
    if not sun_diameter and sun_circumference:
        sun_diameter = calculate_diameter_from_circumference(sun_circumference)
    elif not sun_circumference and sun_diameter:
        sun_circumference = calculate_circumference_from_diameter(sun_diameter)
    
    print(f"Diameter: {format_number(sun_diameter)} km")
    print(f"Circumference: {format_number(sun_circumference)} km\n")
    
    total_planet_volume = 0
    for planet in data["Planets"]:
        print(f"Planet: {planet['Name']}")
        distance = planet.get("DistanceFromSun")
        orbital_period = planet.get("OrbitalPeriod")
        diameter = planet.get("Diameter")
        circumference = planet.get("Circumference")

        if distance is None and orbital_period:
            distance = calculate_distance_from_orbital_period(orbital_period)
        elif orbital_period is None and distance:
            orbital_period = calculate_orbital_period(distance)

        if not diameter and circumference:
            diameter = calculate_diameter_from_circumference(circumference)
        elif not circumference and diameter:
            circumference = calculate_circumference_from_diameter(diameter)
        
        total_planet_volume += calculate_volume(diameter)

        print(f"Distance from sun: {format_number(distance)} au")
        print(f"Orbital period: {format_number(orbital_period)} yr")
        print(f"Diameter: {format_number(diameter)} km")
        print(f"Circumference: {format_number(circumference)} km")
        
        if "Moons" in planet:
            for moon in planet["Moons"]:
                print(f"Moon: {moon['Name']}")
                moon_diameter = moon.get("Diameter")
                moon_circumference = moon.get("Circumference")
                
                if not moon_diameter and moon_circumference:
                    moon_diameter = calculate_diameter_from_circumference(moon_circumference)
                elif not moon_circumference and moon_diameter:
                    moon_circumference = calculate_circumference_from_diameter(moon_diameter)
                
                print(f"Diameter: {format_number(moon_diameter)} km")
                print(f"Circumference: {format_number(moon_circumference)} km")
        print()
    
    sun_volume = calculate_volume(sun_diameter)
    print(f"All the planets’ volumes added together could fit in the Sun: {total_planet_volume < sun_volume}")

# Load dataset from file
def load_solar_system_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# File path to JSON dataset
file_path = "JSONPrettyPrint.txt"
solar_system_data = load_solar_system_data(file_path)

process_solar_system(solar_system_data)
