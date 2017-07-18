#!/usr/bin/python3
#
#A function that queries a mysql database and verifies that all animals listed
#have at least one type of food listed as feed
#
#verify.py

import mysql.connector
from database import login_info
eats = {}
db = mysql.connector.Connect(**login_info)
cursor = db.cursor()

def feed_table():
	'''return a list of tuples whos values are obtained by cross referencing 
	TABLEs animal and food'''
	cursor.execute('''SELECT  animal.id, feed
		           FROM animal JOIN food ON animal.id=food.anid
		           ''')
	rows = cursor.fetchall()
	return rows


def animal_inv():
	'''return a list of tuples of all animals in TABLE animal'''
	cursor.execute('''SELECT id, name, family FROM animal''')
	animals = cursor.fetchall()
	return animals

def verify_food():
	'''Verify that every entry with a valid primary key in animal TABLE
	is represented in the food TABLE'''	
	for animal in animal_inv():
		key = animal[0]
		name = animal[1]
		family = animal[2]
		#list of animal primary_keys in food table
		feed_keys = [row[0] for row in feed_table()]		
		if key not in feed_keys:
			if name != None and family != None:
				print('Primary Key: {}, {} the {} is not in the food table\n'.
					format(key,name, family))
			else:
				print("Primary Key: {}, Animal is NOT in food Table,\n \
and is missing other descriptive information\n".format(key))
				
verify_food()







