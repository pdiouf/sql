# import from csv

# import the csv library

import csv

import sqlite3

with sqlite3.connect("new.db") as connection :
	c = connection.cursor()

	# import the csv file and assigne it to a variable

	employees = csv.reader(open("employees.csv", "rU"))

	# create a new table called employees

	c.execute("CREATE TABLE employees(firtname TEXT, lastname TEXT)")

	# inseert data into table

	c.executemany("INSERT INTO employees(firtname, lastname) values (?, ?)", employees)