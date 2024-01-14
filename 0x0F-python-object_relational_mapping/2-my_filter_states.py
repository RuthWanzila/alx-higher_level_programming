#!/usr/bin/python3

"""
Lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def main():
    # Get MySQL credentials and state name to search from command-line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # Prepare the SQL query with the user input
    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    cursor.execute(query, (state_name,))

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print the selected states
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
