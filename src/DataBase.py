import sqlite3
import temperature
class DataBase:
    def __init__(self):
         #connect to a database
        conn = sqlite3.connect('temperature.db')
        #create a cursor
        cursor =  conn.cursor()
        conn.close()

    def createTable(self,tempObj):
    #connect to a database
        conn = sqlite3.connect('temperature.db')
    #create a cursor
        cursor =  conn.cursor()
    #create a Table
        cursor.execute("""CREATE TABLE temperatureTable(
                year PRIMARY KEY,
                median FLOAT,
                upper FLOAT,
                lower FLOAT
            )""")
    #parse list of temp items into table
        cursor.executemany("INSERT INTO temperatureTable VALUES(?,?,?,?)",tempObj)
    #commits commands
        conn.commit()
    #close our connection
        conn.close()

    def fetchYear(self):
        #connect to a database
        conn = sqlite3.connect('temperature.db')
        #create a cursor
        cursor =  conn.cursor()

        cursor.execute("SELECT year FROM temperatureTable")
        items = cursor.fetchall()

        return items

    def fetchMedian(self):
        #connect to a database
        conn = sqlite3.connect('temperature.db')
        #create a cursor
        cursor =  conn.cursor()

        cursor.execute("SELECT median FROM temperatureTable")
        items = cursor.fetchall()

        return items

    def insert(tempObj):
        #connect to a database
        conn = sqlite3.connect('temperature.db')
        #create a cursor
        cursor =  conn.cursor()
        cursor.execute("INSERT INTO temperatureTable VALUES(?,?,?,?)",tempObj)