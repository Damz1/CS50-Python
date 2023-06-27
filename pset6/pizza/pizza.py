import sys
import csv
from tabulate import tabulate

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    sys.exit("Please provide exactly one command-line argument.")

# Get the filename from the command-line argument
filename = sys.argv[1]

# Check if the file extension is .csv
if not filename.endswith(".csv"):
    sys.exit("The specified file should have a .csv extension.")

try:
    # Open the CSV file
    with open(filename, "r") as file:
        # Read the CSV file using DictReader
        reader = csv.DictReader(file)
        # Convert the data to a list of dictionaries
        data = list(reader)

    # Print the table using tabulate
    table = tabulate(data, headers="keys", tablefmt="grid")
    print(table)

except FileNotFoundError:
    sys.exit("The specified file does not exist.")
