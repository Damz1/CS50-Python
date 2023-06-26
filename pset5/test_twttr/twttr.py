def main():
    tweet = input("Input: ")
    shorten(tweet)


def shorten(tweet):
    new_str = ''
    vowels = 'aeiou'

    for char in tweet:
        if char.lower() not in vowels:
            new_str += char
    return new_str


if __name__ == '__main__':
    main()
