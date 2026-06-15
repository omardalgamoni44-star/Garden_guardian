def water_plants(plant_list: list[str | None]) -> None:

    print("Opening watering system")
    error_happened = False

    try:
        for plant in plant_list:
            if plant is None:
                error_happened = True
                raise ValueError("Error: Cannot water None - invalid plant!")

            print("Watering", plant)

    except ValueError as e:
        print(e)

    finally:
        print("Closing watering system (cleanup)")

    if not error_happened:
        print("Watering completed successfully!")


def test_watering_system() -> None:

    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")

    good_plant_list = ["tomato", "lettuce", "carrots"]
    water_plants(good_plant_list)

    print("\nTesting with error...")

    bad_plant_list = ["tomato", None, "lettuce"]
    water_plants(bad_plant_list)

    print("\nCleanup always happens, even with errors!")


test_watering_system()
