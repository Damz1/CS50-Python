def main():
    tweet = input("Input: ")
    ommit_vowels(tweet)


def ommit_vowels(str):
    new_str = ''
    vowels = 'aeiou'

    for char in str:
        if char.lower() not in vowels:
            new_str += char
    print("Output:", new_str)


main()
