def main():
    answer = input('Greeting: ')
    answer = answer.lower().strip()

    if answer.startswith('hello'):
        print('$0')
    elif answer.startswith('h'):
        print("$20")
    else:
        print('$100')


main()
