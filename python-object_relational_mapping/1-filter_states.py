#!/usr/bin/python3
"""
This script lists all states from
the database hbtn_0e_0_usa whith a name starting with N.
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

    db = MySQLdb.connect(
        host='localhost',
        port=3306, user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
