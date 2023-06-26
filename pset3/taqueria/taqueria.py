menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    bill = 0
    try:
        while True:
            dish = input("Item: ")
            dish = dish.title()
            price = menu.get(dish)
            if price is not None:
                bill += price
                print(f"Total: ${bill:.2f}")

    except EOFError:
        print()


main()