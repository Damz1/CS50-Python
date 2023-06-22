from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


def main():
    if len(sys.argv) == 1:
        text = input()
        fonts = figlet.getFonts()
        random_font = random.choice(fonts)
        f = Figlet(font=random_font)
        print(f.renderText(text))
    elif len(sys.argv) == 2:
        sys.exit("invalid usage")
    elif len(sys.argv) == 3 and sys.argv[1] not in ['-f', '--font']:
        sys.exit("invalid usage")
    elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
        text = input()
        f = Figlet(font=sys.argv[2])
        print(f.renderText(text))
    else:
        sys.exit("invalid command line arguments")


if __name__ == "__main__":
    main()
