# by Chevy Lazenby and Ingrid Olea 

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

# 1.Loops through each vegetable

import csv

with open('vegetables.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'color', 'length'])
	for x in range (0,6):
		writer.writerow([vegetables[x]["name"],vegetables[x]["color"],len(vegetables[x]["name"])])
