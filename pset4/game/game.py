import random
import sys

def main():
    n = 0
    while n < 1:
        n = get_positive_integer_input("level: ")
    random_number = random.randint(1, n)

    guess = 0
    while guess < 1:
        guess = get_positive_integer_input("Guess: ")

    while guess < random_number:
        print("Too small!")
        guess = get_positive_integer_input("Guess: ")

    while guess > random_number:
        print("Too large!")
        guess = get_positive_integer_input("Guess: ")
    if guess == random_number:
        print("Just right!")
        sys.exit()

def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print("Invalid input. Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
