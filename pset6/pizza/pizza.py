import sys
import csv
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit("excpect one command line argument")

file_path = sys.argv[1]
if not file_path.endswith('.csv'):
    sys.exit('not a csv file')


def main(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            # convert to a list of dictionaries
            data = list(reader)

        convert_to_asci(data)

    except FileNotFoundError:
        sys.exit('File not found')


def convert_to_asci(data):
    table = tabulate(data, headers="keys", tablefmt="grid")
    print(table)


if __name__ == "__main__":
    main(file_path)
