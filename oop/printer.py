from sun import Sun
from planet import Planet
from moon import Moon

def print_solar_system(solar_system_data):
    print(f"Sun: {solar_system_data['Name']}")
    sun_name = solar_system_data["Name"]
    sun_diameter = solar_system_data["Diameter"]
    sun_circumference = solar_system_data.get("Circumference")

    sun = Sun(sun_name, sun_diameter, sun_circumference)
    if not sun_diameter and sun_circumference:
        sun_diameter = sun.calculate_diameter()
    elif not sun_circumference and sun_diameter:
        sun_circumference = sun.calculate_circumference()

    print(f"Diameter: {sun.format_number(sun_diameter)} km")
    print(f"Circumference: {sun.format_number(sun_circumference)} km")

    total_planet_volume = 0
    for planet_data in solar_system_data["Planets"]:
        print("\n")
        name = planet_data["Name"]
        print(f"Planet: {name}")
        diameter = planet_data.get("Diameter")
        circumference = planet_data.get("Circumference")
        distance = planet_data.get("DistanceFromSun")
        orbital_period = planet_data.get("OrbitalPeriod")
        planet = Planet(name, diameter, circumference, distance, orbital_period)

        planet.calculate_diameter()
        planet.calculate_circumference()
        planet.calculate_orbital_period()
        planet.calculate_distance()
        total_planet_volume += planet.calculate_volume()

        print(f"Distance from sun: {planet.format_number(planet.calculate_distance())} au")
        print(f"Orbital period: {planet.format_number(planet.calculate_orbital_period())} yr")
        print(f"Diameter: {planet.format_number(planet.calculate_diameter())} km")
        print(f"Circumference: {planet.format_number(planet.calculate_circumference())} km")
        moons = planet_data.get("Moons", [])

        if moons:
            for moon_data in moons:
                moon_name = moon_data["Name"]
                moon_diameter = moon_data.get("Diameter")
                moon_circumference = moon_data.get("Circumference")
                moon = Moon(moon_name, moon_diameter, moon_circumference)

                moon.calculate_diameter()
                moon.calculate_circumference()

                print(f"Moon: {moon_name}")
                print(f"Diameter: {moon.format_number(moon.calculate_diameter())} km")
                print(f"Circumference: {moon.format_number(moon.calculate_circumference())} km")
        

    sun_volume = sun.calculate_volume()
    print(
        f"All the planets’ volumes added together could fit in the Sun: {total_planet_volume < sun_volume}"
    )
