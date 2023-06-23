import inflect

p = inflect.engine()

def main():
    list_of_names = []
    try:
        while True:
            name = input("Name: ")
            list_of_names.append(name)
    except EOFError:
        output = p.join(list_of_names)
        print()
        print("Adieu, adieu, to", output)

if __name__ == "__main__":
    main()