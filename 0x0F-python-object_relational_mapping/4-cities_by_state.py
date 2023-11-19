#!/usr/bin/python3
"""script that takes in the name of a state as
an argument and lists all cities of that state using the database
hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id")
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    conn.close()
