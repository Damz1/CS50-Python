def main():
    while True:
        try:
            fuel_fraction = input("fraction: ")
            fuel_percentage = convert(fuel_fraction)
            print(gauge(fuel_percentage))
            break
        except ValueError as e:
            print("Invalid fraction")
        except ZeroDivisionError:
            print("Zero division error")


def convert(fraction):
    x, y = map(int, fraction.split('/'))
    if not (isinstance(x, int) and isinstance(y, int)):
        raise ValueError("X and Y must be integers.")
    if y == 0:
        raise ZeroDivisionError("Y cannot be zero.")
    if x > y:
        raise ValueError("X cannot be greater than Y.")
    fuel_percentage = (x / y) * 100
    return round(fuel_percentage)


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return str(percentage) + '%'


if __name__ == "__main__":
    main()
