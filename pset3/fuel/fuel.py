def main():
    while True:
        fuel_fraction = input("fraction: ")
        fuel_percentage = calculate_fuel_percentage(fuel_fraction)
        if fuel_percentage is not None:
            print(fuel_percentage)
            break


def calculate_fuel_percentage(fuel_fraction):
    try:
        x, y = map(int, fuel_fraction.split('/'))
        if y == 0 or x > y:
            return None
        fuel_percentage = (x / y) * 100
        if fuel_percentage <= 1:
            return 'E'
        elif fuel_percentage >= 99:
            return 'F'
        else:
            return str(round(fuel_percentage)) + '%'
    except (ValueError, ZeroDivisionError):
        return None


main()
