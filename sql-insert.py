import sqlite3
import random

with sqlite3.connect("newnum.db") as connection :
	c = connection.cursor()
    
    # delete databases table if exist
	c.execute("DROP TABLE if exists  numbers ")
	# create database table
	c.execute("CREATE TABLE numbers(num int)")

	for i in range(100):
		c.execute("INSERT INTO numbers values(?)", (random.randint(0, 100),))