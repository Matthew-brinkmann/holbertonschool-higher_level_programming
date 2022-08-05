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
    dbCur = SQLdbConnection.cursor()
    dbCur.execute("SELECT * FROM states\
                   WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    query_rows = dbCur.fetchall()
    if (query_rows is not None):
        for row in query_rows:
            print(row)
    dbCur.close()
    SQLdbConnection.close()
