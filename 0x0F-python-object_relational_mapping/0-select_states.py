#!/usr/bin/python3
'''
This module is a basic interaction with
a MYSQL DB
'''

import MySQLdb
import sys

if __name__ == "__main__":
    SQLdbConnection = MySQLdb.connect(host="localhost",
                                      port=3306,
                                      user=sys.argv[1],
                                      passwd=sys.argv[2],
                                      db=sys.argv[3])
    dbCurser = SQLdbConnection.cursor()
    dbCurser.execute('''
                     SELECT * FROM states
                     ORDER BY id ASC
                     ''')
    query_rows = dbCurser.fetchall()
    for row in query_rows:
        print(row)
    dbCurser.close()
    SQLdbConnection.close()
