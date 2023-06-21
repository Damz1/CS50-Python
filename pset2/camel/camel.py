def main():
    camelCase = input("camelCase: ")
    snake_case = camelCase[0].lower()

    for letter in camelCase[1:]:
        if letter.islower():
            snake_case += letter
        else:
            snake_case += '_' + letter.lower()

    print('snake_case:', snake_case)


main()
