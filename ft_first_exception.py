def check_temperature(temp_str: str) -> int:
    try:
        degree = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number")

    if degree < 0:
        raise ValueError(f"{degree}°C is too cold for plants (min 0°C)")

    if degree > 40:
        raise ValueError(f"{degree}°C is too hot for plants (max 40°C)")

    print(f"Temperature {degree}°C is perfect for plants!")
    return degree


def test_temperature_input() -> None:
    values = ["25", "abc", "100", "-50"]

    for test in values:
        print("Testing temperature:", test)
        try:
            check_temperature(test)
        except ValueError as error:
            print("Error:", error)
        print()


print("=== Garden Temperature Checker ===\n")
test_temperature_input()
print("All tests completed - program didn’t crash!")
