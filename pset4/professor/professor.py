import random



def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = int(input(f"{x} + {y} = "))
        if answer == x + y:
            score += 1
        else:
            mistakes = 1
            while answer != x + y and mistakes < 3:
                print("EEE")
                mistakes += 1
                answer = int(input(f"{x} + {y} = "))
            if mistakes == 3:
                print(f"{x} + {y} =", x + y)
            if answer == x + y:
                score += 1
                break
    print(score)


def get_level():
    while True:
        level = input("What is your level? ")
        if level.isdigit() and int(level) in [1, 2, 3]:
            return int(level)
        else:
            print("Invalid input. Please enter 1, 2, or 3.")


def generate_integer(level):
    if level == 1:
        random_int = random.randint(0,9)
    elif level == 2:
        random_int = random.randint(10, 99)
    elif level == 3:
        random_int = random.randint(100,999)
    else:
        raise ValueError("Invalid value")
    return random_int


if __name__ == "__main__":
    main()