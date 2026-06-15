class GardenError(Exception):
    pass


class GardenManager:

    def __init__(self) -> None:
        self.plants = {}

    def add_plant(self, name, water, sun) -> None:

        if not name:
            raise ValueError("Plant name cannot be empty!")

        self.plants[name] = {"water": water, "sun": sun}
        print(f"Added {name} successfully")

    def water_plants(self) -> None:

        print("Opening watering system")

        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")

        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, name) -> None:

        if name not in self.plants:
            raise GardenError("Plant not found")

        plant = self.plants[name]
        water = plant["water"]
        sun = plant["sun"]

        if water < 1 or water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")

        if sun < 2 or sun > 12:
            raise ValueError(f"Sunlight hours {sun} invalid")

        print(f"{name}: healthy (water:  {water}, sun:  {sun})")


def test_garden_management() -> None:

    print("=== Garden Management System ===\n")

    garden = GardenManager()

    print("Adding plants to garden...")

    try:
        garden.add_plant("tomato", 5, 8)
        garden.add_plant("lettuce", 15, 6)
        garden.add_plant("", 5, 8)
    except ValueError as e:
        print("Error adding plant: ", e)

    print("\nWatering plants...")

    garden.water_plants()

    print("\nChecking plant health...")

    try:
        garden.check_health("tomato")
        garden.check_health("lettuce")
    except ValueError as e:
        print("Error checking lettuce: ", e)

    print("\nTesting error recovery...")

    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print("Caught GardenError: ", e)
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


test_garden_management()
