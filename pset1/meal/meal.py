def main():
    time = input("Time: ")
    hours = convert(time)

    if 7 <= hours < 8:
        print("Breakfast time")
    elif 12 <= hours <= 13:
        print("Lunch time")
    elif 18 <= hours < 19:
        print("Dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    total_hours = hours + (minutes/60)
    return total_hours


if __name__ == "__main__":
    main()
