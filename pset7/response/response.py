import validators


def main():
    print(is_valid(input("what's your email address? ")))


def is_valid(email):
    result = validators.email(email)
    if result:
        return 'Valid'
    else:
        return 'Invalid'


if __name__ == '__main__':
    main()
