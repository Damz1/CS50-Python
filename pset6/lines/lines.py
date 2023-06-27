import sys

if len(sys.argv) != 2:
    sys.exit("invalid numbers of arguments")

file_path = sys.argv[1]
if not file_path.endswith('.py'):
    sys.exit('not a py file')


def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            number_of_lines = 0
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    number_of_lines += 1
            return number_of_lines
    except FileNotFoundError:
        sys.exit('file not found')


print(count_lines(file_path))
