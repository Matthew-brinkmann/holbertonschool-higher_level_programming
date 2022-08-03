#!/usr/bin/python3
'''
This module is a basic interaction with
a MYSQL DB
'''

import MySQLdb
import sys

if __name__ == "__main__":
    stateToSearchFor = sys.argv[4]
    seperatorForString = ""
    printCityString = ""
    SQLdbConnection = MySQLdb.connect(host="localhost",
                                      port=3306,
                                      user=sys.argv[1],
                                      passwd=sys.argv[2],
                                      db=sys.argv[3])
    dbCurser = SQLdbConnection.cursor()
    dbCurser.execute(f'''
                      SELECT cities.id, cities.name, states.name
                      FROM cities INNER JOIN states
                      ON cities.state_id=states.id
                      ORDER BY cities.id ASC
                      ''')
    query_rows = dbCurser.fetchall()
    for rowFromDb in query_rows:
        if (stateToSearchFor == rowFromDb[2]):
            printCityString += seperatorForString
            printCityString += rowFromDb[1]
            seperatorForString = ", "
    print(printCityString)
    dbCurser.close()
    SQLdbConnection.close()
