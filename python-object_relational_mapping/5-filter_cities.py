#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    The main entry point of the script.
    Retrieves MySQL username, password, and database name from
    command line arguments and calls list_cities function.
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
    cursor.execute("SELECT cities.name FROM cities "
                   "JOIN states ON cities.state_id = states.id "
                   "WHERE states.name = %s "
                   "ORDER BY cities.id ASC", (state_name,))
    rows = cursor.fetchall()
    if rows:
        print(", ".join(row[0] for row in rows))
    else:
        print("")
    cursor.close()
    db.close()
