# Create a SQLite3 databases table


# import the SQLite3 library
import sqlite3

# create a new database if the database doesn't already exist
conn = sqlite3.connect("cars")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

#create a table

cursor.execute("""CREATE TABLE inventory
	           (Make TEXT, Model TEXT, Quantity INT)
               """)

# close the the database connection
conn.close()