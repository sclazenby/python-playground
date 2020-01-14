# by Chevy Lazenby and Ingrid Olea

# Reads superheroes.json (in this folder)

import json
import csv

with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)
    
print(superheroes)

# Creates an empty array called powers
powers = []

# Loop thorough the members of the squad, and append the powers of each to the powers array.
members = superheroes['members']

for hero in members: 
	hero_powers = hero['powers']
	powers.append(hero_powers)
# Prints those powers to the terminal
print(powers)

#Write a header to the CSV file
with open('superheroes.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active' ])

#Loop over the members and for each member write a row to the csv file
	members = superheroes['members']

	for hero in members: 
		hero_name = hero['name']
		hero_age = hero['age']
		hero_secretIdentity = hero['secretIdentity']
		hero_powers = hero['powers']
		hero_squadName = superheroes['squadName']
		hero_homeTown = superheroes['homeTown']
		hero_formed = superheroes['formed']
		hero_secretBase = superheroes['secretBase']
		hero_active = superheroes['active']
		writer.writerow([hero_name, hero_age, hero_secretIdentity, hero_powers, hero_squadName, hero_homeTown, hero_formed, hero_secretBase, hero_active])
