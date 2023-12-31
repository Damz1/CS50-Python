def main():
    grocery_list = {}

    try:
        while True:
            item = input().upper()
            grocery_list[item] = grocery_list.get(item, 0) + 1
    except EOFError:
        pass

    sorted_items = sorted(grocery_list.items())

    for item, count in sorted_items:
        print(f"{count} {item}")


main()
