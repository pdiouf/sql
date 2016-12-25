# INSERT Command


# import the SQLite3 library
import sqlite3

with sqlite3.connect("new.db") as connection :
	
	c = connection.cursor()

	c.execute("INSERT INTO population VALUES('Kentuky', \
		  'KT', 8500000)")

	c.execute("INSERT INTO population VALUES('Washington', \
		  'WC', 8800000)")


# close the database connection
c.close()