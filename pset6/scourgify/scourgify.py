import sys
import csv

if len(sys.argv) != 3:
    sys.exit('wrong number of arguments')

input_file = sys.argv[1]
try:
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
except FileNotFoundError:
    sys.exit('file not found')

new_rows = []
for row in rows:
    name = row['name'].split(', ')
    first_name = name[1]
    last_name = name[0]
    house = row['house']
    new_row = {'first': first_name, 'last': last_name, 'house': house}
    new_rows.append(new_row)

output_file = sys.argv[2]
with open(output_file, 'w') as file:
    fieldnames = ['first', 'last', 'house']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_rows)
