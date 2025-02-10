import json
from printer import print_solar_system

def load_solar_system_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def main():
    file_path = "JSONPrettyPrint.txt"
    solar_system_data = load_solar_system_data(file_path)

    print_solar_system(solar_system_data)

if __name__ == "__main__":
    main()
