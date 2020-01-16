# By Chevy Lazenby and Ingrid Olea
import csv
import json
from pprint import pprint

#1 read vegetables.csv into a variable called vegetables

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    vegetables = [dict(row) for row in rows]

#2 group vegetables by color as variable vegetables_by_color

vegetables_by_color = {}
for veg in vegetables:
    color = veg['color']
    if color in vegetables_by_color:
        vegetables_by_color[color].append(veg)
    else:
        vegetables_by_color[color] = [veg]

pprint(vegetables_by_color)

# output to json
with open('vegetables_by_color.json', 'w') as f:
    json.dump(vegetables_by_color, f, indent = 4)