def check_plant_health(plant_name, water_level, sunlight_hours) -> str:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!\n")
    if water_level > 10:
        raise ValueError(
            f"Water level {water_level} is too high (max 10)\n"
        )
    if water_level < 1:
        raise ValueError(
            f"Water level {water_level} is too low (min 1)"
        )
    if sunlight_hours < 2:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low (min 2)\n"
        )
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)"
        )
    return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks() -> None:

    print("=== Garden Plant Health Checker ===")
    print()
    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 5, 6))
    except ValueError as er1:
        print("Error: ", er1)
    print("Testing empty plant name...")
    try:
        print(check_plant_health("", 5, 7))
    except ValueError as er2:
        print("Error: ", er2)

    print("Testing bad water level...")
    try:
        print(check_plant_health("cactus", 15, 9))
    except ValueError as er3:
        print("Error: ", er3)

    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("oak", 8, 0))
    except ValueError as er4:
        print("Error: ", er4)
    print("All error raising tests completed!")


test_plant_checks()
