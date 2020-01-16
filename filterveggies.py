# By Chevy Lazenby and Ingrid Olea
import csv
import json

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    vegetables = [dict(row) for row in rows] # Convert OrderedDict to regular dict


# filter to green veggies only
greenvegetables = []
for row in rows:
    if row['color'] == 'green':
        greenvegetables.append(row)

print(greenvegetables)

with open('greenveggies.json', 'w') as f:
    json.dump(greenvegetables, f)

with open('greenvegetables.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(['name', 'color'])
    for veg in greenvegetables:
    	writer.writerows([[veg['name']],[veg['color']]])
   