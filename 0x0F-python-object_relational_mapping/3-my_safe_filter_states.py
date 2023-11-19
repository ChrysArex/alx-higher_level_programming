#!/usr/bin/python3
"""This script that lists all states from the database hbtn_0e_0_usa"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY\
            states.id".format(sys.argv[4])
    cur.execute(query.split(";")[0])
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    conn.close()
