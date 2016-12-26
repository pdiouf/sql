import sqlite3

conn = sqlite3.connect("newnum.db")
cursor = conn.cursor()

prompt = """
Select the operation thatyou want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""

while True:
		# get the user input
	x = input(prompt)

		# if enters any choice from 1-4
	if x in set (["1", "2", "3", "4"]):
			# parse the corresponding operation text
		operation = {1: "avg", 2:"max", 3:"min", 4:"sum"}[int(x)]

			#retrieve data
		cursor.execute("SELECT {}(num) from numbers".format(operation))
            
            #fetchone retriews one record from the query
		get = cursor.fetchone()

			# output result toscreen
		print(operation + ": %f" % get[0])

	elif x == "5":
		print("Exit")

			# exit loop
		break