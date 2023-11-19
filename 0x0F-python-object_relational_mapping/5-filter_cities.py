#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state, using the database
hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    idx = 0
    lenght = 0
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name\
                FROM cities JOIN states ON cities.state_id = states.id\
                WHERE states.name = '{}'\
                ORDER BY cities.id".format(sys.argv[4]))
    rows = cur.fetchall()
    lenght = len(rows)
    for r in rows:
        if idx != lenght - 1:
            print(r[0] + ", ", end="")
        else:
            print(r[0])
        idx += 1
    cur.close()
    conn.close()
