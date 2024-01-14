#!/usr/bin/python3

"""
This script lists all states with a name starting with 'N' (uppercase) from the 'hbtn_0e_0_usa' database.
"""

import sys
import MySQLdb

# Get MySQL credentials from command-line arguments
mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

# Connect to the MySQL database
db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=mysql_user,
    passwd=mysql_password,
    db=database_name
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Execute the SQL query to select states starting with 'N'
query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
cursor.execute(query)

# Fetch all the rows returned by the query
rows = cursor.fetchall()

# Print the selected states
for row in rows:
    print(row)

# Close the cursor and database connection
cursor.close()
db.close()
