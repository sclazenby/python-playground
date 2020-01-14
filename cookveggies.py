# By Chevy Lazenby and Ingrid Olea

import csv

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)
    vegetables = [dict(row) for row in vegetables] # Convert OrderedDict to regular dict

print(vegetables)

import json

with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f, indent = 4)