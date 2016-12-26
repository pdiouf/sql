import sqlite3

with sqlite3.connect("new.db") as connection :
	c = connection.cursor()

	#create a dictionnary of SQL queries

	sql = {'average': "SELECT avg(population) from population",
	       'maximun': "SELECT max(population) from population",
	       'minimum': "SELECT min(population) from population",
	       'sum': "SELECT sum(population) from population",
	       'count': "SELECT count(population) from population"}

    # run each sql query item in the dictionnary
	for keys,  values in sql.items():
		c.execute(values)

		# fetchone() retrieves one record from query
		result = c.fetchone()

		#output the result

		print( keys + ":", result[0])


