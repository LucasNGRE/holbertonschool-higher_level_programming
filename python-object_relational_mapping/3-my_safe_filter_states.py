#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    The main entry point of the script.
    Retrieves MySQL username, password, and database name from
    command line arguments and calls list_states function.
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_db)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                   (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
